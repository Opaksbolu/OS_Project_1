Overview
This project implements a Driver, Logger, and Encryptor that work together to encrypt and decrypt messages using the Vigenère cipher. The system allows users to:
•	Set a password (encryption key)
•	Encrypt and decrypt messages
•	Maintain a history of operations
•	Log all actions in a logfile.txt
Files
•	driver.py → Main program that interacts with the user.
•	encrypt.py → Handles encryption and decryption using the Vigenère cipher.
•	logger.py → Logs all user actions in logfile.txt.
Requirements
•	Python 3.x
Running the Project
1.	Open a terminal in the project directory.
2.	Run the Driver program:
3.	To run the program type the following: python3 driver.py logfile.txt
Commands
When the driver is running, you can enter the following commands:
Command	Description
password	Set a new encryption password.
encrypt	Encrypt a message.
decrypt	Decrypt a message.
history	View all previous encrypted messages.
quit	Exit the program.
Example Usage
Logging
Every action is logged in logfile.txt with timestamps. Example:
Notes
•	The password is required before encryption and decryption.
•	The history command stores encrypted messages only.
•	The logger keeps track of all actions in logfile.txt.
Exiting
Type quit to close the program.

