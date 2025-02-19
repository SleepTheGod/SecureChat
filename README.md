# SecureChat

SecureChat is a peer-to-peer encrypted chat application with support for secure messaging and file sharing. It uses AES encryption for messages and files, and Diffie-Hellman key exchange for secure key management. This application ensures the confidentiality and integrity of your communication, making it suitable for secure chatting.

# Features

- AES Encryption - Messages and files are encrypted using AES with a secure passphrase.
- Diffie-Hellman Key Exchange - A Diffie-Hellman key exchange mechanism ensures secure key sharing between clients.
- File Encryption - Files are encrypted before being sent to ensure confidentiality.
- Security - Rejects filenames starting with '.' or '/' to prevent path traversal attacks.
- Commands
  - /msg <ip> - Change chat target to a different IP address.
  - /send <filename> - Send a file to the other client.
  - /leave - Exit the chat.
  - /help - Show available commands.

# Installation

1. Clone this repository

   git clone https://github.com/SleepTheGod/SecureChat/
   cd SecureChat

2. Install the required dependencies by using the requirements.txt file

   pip install -r requirements.txt

# Usage

1. Start the chat client by running main.py

   python main.py

2. Follow the prompts to enter the IP address and port for communication.

3. Use the commands to chat securely and send/receive files. The application will automatically encrypt all messages and files exchanged.

# Requirements

- Python 3.6+
- Required Python packages listed in requirements.txt

  cryptography==39.0.0
  pycryptodome==3.15.0

# Notes

- Encryption - AES encryption is used for message encryption, and Diffie-Hellman ensures the secure exchange of keys.
- File Sharing - When sending a file, ensure the filename does not start with a dot (.) or slash (/) to avoid security risks.
- Security - This application follows best practices to ensure that all communication is secure and encrypted.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Contributing

Feel free to fork the repository, submit issues, and send pull requests. Contributions are welcome!

# Author

SleepTheGod - GitHub Profile: https://github.com/SleepTheGod

```
                                                                                
                            █████████████▒████████                              
                        ▓▒██████▒░█░███░░ ▒███████████▒                         
                     ███████████   ▓█████████████████████▒                      
                  ▓████  ▒█████████▒▒░███████████████████████▒                  
              ░▒███████░████████▒██     ▒██████████████████████░                
             ▓███████████████▒██  ░█     ░████████████████████████░             
            ████████████████████▒  ███▒█████████████████████████████            
          ░████████▒██████████████████     ▒█████████████████████████▒          
         ███████████▒████████████     ▒     ███████████████████████████▒        
       ▒██████████▒ ░████████████     ▒██▓  ░▒██████████████████████████▒       
       █████████  ▒███▒   ███████░    ███████████████████████████████████       
      █████████░██████    █████▒██▓ ▓███████▒▒████████████████████████████      
    ▒██████████████████   ████▒▓▒█▒   █████████████████████████████████████     
   ░████████████████████░▓█░    ░█     ░▓███████████████████████████████████    
   ███████████████████▓   ░       █       ░██████████████████████████████████   
  ████████████████████            █▒   ██░▒███████████████████████████████████  
 ▒███████████████████     ▒     ▒▓███▒▓    ███████████████████████████████████  
░██████████████████       █▓▓▓▓█░  █        ████████████░     ░████████████████ 
██████████████████      ▓███       █░       █████████████▓██████████████████  █ 
██████████████████   ░░  ▓█         ▒        ███████████████████████████████  ▓ 
██████████████████░ ▓     █░        █        ███████████████████████████████░   
██████████████████        ██       ▒███      ████████████████████████████████▒█ 
███████████████▒██         █     ░▒▒██      ░▒████████████████████████████ █    
███████████████▒▒▒         ███               ████████████████████████████▒ █░   
█░ ▓▓██████   ░ ▓█      ████▒         █      ████████████████████████████  █▓   
     ██████▒    ▒█     ▒   █▓         █      ▓████████████████████████████ ▒█▒  
▓  ▒▒█▓█▓████   ▒▒██▒                 ██  ▒▒▒░█████████████████████████████▓██  
███▓   █░  ▒██████░         ░       ░▓███▒      ██████████████████████████████░ 
██     █▓   ░████▒▒         ██  ▒  ░▒▒▓█▒        █████████████████████████████  
░      ▓█▓    ██████▓▒      ███        ██         ██▓█▒▓░  ░██████████████████  
▒░     ░███   ████████████▒▒ ▓▓        ▓█░        █         ██████████████████  
█▒    ▒██▒   ██████████████   ░         █▒      ▒▒█▒▓   ▒▒▒░██████████████████  
██   ██ ▒▓  ███████████████████         ██▒ ▒███▒▓██▓       █    ░████████████  
██▓█     █  ███████████████████▒       ███▓       ▓█        █▓    ████████████▓ 
███       ██████████████████████░▒▒█▒   ▒█         █▒       ██     ██████████▓  
█▒█       ████████████████████████       ░░        █▒       ▒      ▓██████████  
▒▒█       ███████████████████████         █        █        ▒      ▒▒█████████▓ 
█▒       ▒███████████████████████▒        █        ██      ██▒     ██  ░███▒ ██ 
██ █   ▒░  ▓███████████████████ ██       ███▒ ▒   ░██      █▒▒    ▒████░░██  ██ 
 █▓███▒     ██▓▒█████████████░   ██ ▓█░░░░██░      █▒      ▒      ░█░   ▓█░░██░ 
  ████▒       █ ▓███████████    ▓███░      █       ▓█      ▒            ▒▓ ███  
  █████       ███  ████████░  ▒█░ ██       █       ██     ▒▓      ▒    ███ ██   
   █▓██▓      ██▒   ▒███████▓      █▒      ▓▓     ░███    ██▒▒▒ ▒█░  ███████▒   
    ▒█░▒     ░ ░█░   ███████▒       ░▓     ▒█████▒███▓░  ▒███▒████░ ███████▒    
    ▒█████░░     ░▒  ░███████       ░█▓  ░░███     █      █    █    ██████▓     
     ▒██████      ▒███████████  ░  ▒▒███    ░▓     █     ░    ░█    █████▒      
      ▒███████▒    ███  ▒██████░███▒▒▒█░      ▒    ▓    █░    █   ░████▓        
        ███████  ░█░ ░▒    ▓██████     █     ▒█    █░  ▓██░░█▒▒  ▒████▒         
         ▓███████     ▒█▒  ░██ ▒██       ▒    ███████ ███░████▓██████           
      /████████    /████████    /██████████████████     /███████████████▄       
     |▒████████    |████████   |▒██████████████████    |▒█████████████████      
     |▒████████    |████████   |▒██████████████████    |▒██████▀▀▀▀▀▀█████      
     |▒█▓▓▓▓▓▓█▄▄▄▄▄█▓▓▓▓▓▓█   |/▒▒▒▒/█▓▓▓▓▓▓█▒▒▒▒/    |▒█▓▓▓▓▓     |▓▓▓██      
     |▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█        |▒█▓▓▓▓▓▓█         |▒█▓▓▓▓▓     |▓▓▓██      
     |▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█        |▒█▒▒▒▒▒▒█         |▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
     |▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█        |▒█▒▒▒▒▒▒█         |▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒██      
     |▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█        |▒█░░░░░░█         |▒█▒▒▒▒▒█▀▀▀▀▀▀▀▀▀       
     |▒█░░░░░░█▀▀▀▀▒█░░░░░░█        |▒█░░░░░░█         |▒█░░░░░█                
     |▒█░░░░░░█   |▒█░░░░░░█        |▒█      █         |▒█░░░░░█                
     |▒█      █   |▒█      █        |▒█▄▄▄▄▄▄█         |▒█     █                
     |▒█▄▄▄▄▄▄█   |▒█▄▄▄▄▄▄█        |/▒▒▒▒▒▒▒/         |▒█▄▄▄▄▄█                
     |/▒▒▒▒▒▒▒/   |/▒▒▒▒▒▒▒/                           |/▒▒▒▒▒▒/  
```
