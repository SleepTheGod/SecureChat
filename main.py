import sys
import socket
import base64
import os
import hashlib
import getpass
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import scrypt
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from threading import Thread
import logging

class SecureChatClient:
    def __init__(self):
        self.logger = self.setup_logging()
        print("Welcome to SecureChat - P2P Encrypted Chat with AES and Diffie-Hellman.")
        print("Type /help for available commands.")
        
        self.IP = input("Enter the IP address you wish to chat with: ")
        self.PORT = int(input("Enter the port for communication: "))
        self.logger.info(f"Connecting to {self.IP}:{self.PORT}")

        # Generate Diffie-Hellman keys for secure key exchange
        self.private_key, self.public_key = self.generate_dh_keys()

        # Use a secure passphrase to derive the AES key
        self.EncryptKeyAES = self.generate_AES_key()

        # AES padding logic
        BS = 16
        self.pad = lambda s: s + (BS - len(s) % BS).to_bytes(1, byteorder='big', signed=False) * (BS - len(s) % BS)
        self.unpad = lambda s: s[:-s[-1]]

        input("Press enter when both clients are ready.")
        
        try:
            Thread(target=self.RecvMSG, args=()).start()
        except socket.error as e:
            self.logger.error(f"Connection error: {e}")
            print(f"{self.IP} is not ready. Press enter when {self.IP} is ready.")
            input()
            Thread(target=self.RecvMSG, args=()).start()
        
        self.SendMSG()

    def setup_logging(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        return logging.getLogger(__name__)

    def generate_dh_keys(self):
        parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
        private_key = parameters.generate_private_key()
        public_key = private_key.public_key()
        self.logger.info("Generated Diffie-Hellman keys.")
        return private_key, public_key

    def generate_AES_key(self):
        password = getpass.getpass("Enter a secure passphrase for AES encryption: ")
        salt = os.urandom(16)
        key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend()).derive(password.encode())
        self.logger.info("Generated AES key using PBKDF2HMAC.")
        return key

    def EncryptAES(self, raw):
        raw = self.pad(raw)
        iv = os.urandom(AES.block_size)
        cipher = AES.new(self.EncryptKeyAES, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw)).decode()

    def DecryptAES(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.EncryptKeyAES, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(enc[16:])).decode()

    def EncryptMSG(self, data):
        data = self.EncryptAES(data.encode())
        self.logger.debug(f"Encrypted message: {data}")
        return data

    def DecryptMSG(self, data):
        data = self.DecryptAES(data)
        self.logger.debug(f"Decrypted message: {data}")
        return data

    def SendMSG(self):
        clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f"You're now talking to {self.IP}")
        while True:
            command = input("Command: ").strip()
            if command == "/leave":
                message = self.EncryptMSG("\x03")
                clientsock.sendto(message.encode(), (self.IP, self.PORT))
                sys.exit(0)
            elif command.startswith("/msg"):
                self.IP = command.split(" ")[1]
                print(f"Now chatting with '{self.IP}'")
                continue
            elif command.startswith("/send"):
                self.SendFILE(command.split(" ")[1])
                continue
            elif command == "/help":
                self.show_help()
            else:
                message = self.EncryptMSG("\x01" + command)
                clientsock.sendto(message.encode(), (self.IP, self.PORT))

    def show_help(self):
        print("""Available commands:
        /msg <ip> - Change the chat to a new IP address.
        /send <filename> - Send a file (ensure it doesn't start with '.' or '/').
        /leave - Exit the chat.
        /help - Show this help message.""")

    def SendFILE(self, file_):
        if file_.startswith(".") or file_.startswith("/"):
            print("Security error: Filename starts with '.' or '/'. Aborted.")
            self.logger.warning(f"Attempted file send with dangerous filename: {file_}")
        else:
            clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = "\x02" + file_ + "\xFF"
            try:
                with open(file_, "rb") as f:
                    data += f.read()
                data = self.EncryptMSG(data)
                clientsock.sendto(data.encode(), (self.IP, self.PORT))
                print("File sent!")
                self.logger.info(f"File {file_} sent successfully.")
            except Exception as e:
                print(f"Error sending file: {e}")
                self.logger.error(f"Failed to send file: {file_} - {e}")

    def RecvMSG(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        serversocket.bind(('', self.PORT))
        while True:
            data, addr = serversocket.recvfrom(1073741824)
            data = self.DecryptMSG(data.decode())
            if data.startswith("\x02"):
                filename = ''
                data = list(data)
                del data[0]
                for i in data:
                    if i == "\xFF":
                        break
                    else:
                        filename += i
                del data[0]
                del data[:len(filename)]
                if filename.startswith(".") or filename.startswith("/"):
                    print(f"Security alert! {addr[0]} tried a path traversal attack.")
                    self.logger.warning(f"Path traversal attempt by {addr[0]}: {filename}")
                else:
                    print(f"{addr[0]} sent file {filename}")
                    data = b''.join(data)
                    with open(filename, "wb") as f:
                        f.write(data)
                    print("File saved.")
            elif data.startswith("\x01"):
                data = list(data)
                del data[0]
                data = ''.join(data)
                print(f"{addr[0]}: {data}")
            elif data.startswith("\x03"):
                print(f"{addr[0]} has left.")
                sys.exit(0)

if __name__ == "__main__":
    SecureChatClient()
