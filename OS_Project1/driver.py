import sys
import subprocess

def log_message(logger, action, message):
    """Sends a log message to the logger process."""
    logger.stdin.write(f"{action} {message}\n")
    logger.stdin.flush()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py <log_file>")
        return

    log_file = sys.argv[1]

    logger = subprocess.Popen(["python3", "logger.py", log_file], stdin=subprocess.PIPE, text=True)
    encryptor = subprocess.Popen(["python3", "encrypt.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    log_message(logger, "START", "Driver Started.")

    history = []
    while True:
        command = input("\nCommands: password | encrypt | decrypt | history | quit\n> ").strip().lower()

        if command == "password":
            password = input("Enter new password:\n> ").strip().upper()
            if not password.isalpha():
                print("ERROR Password must contain only letters.")
                continue
            encryptor.stdin.write(f"PASS {password}\n")
            encryptor.stdin.flush()  # Ensure input is processed
            response = encryptor.stdout.readline().strip()
            print(response)
            log_message(logger, "PASSWORD", "Passkey set.")

        elif command == "encrypt":
            text = input("Enter text to encrypt:\n> ").strip().upper()
            if not text.isalpha():
                print("ERROR Input must contain only letters.")
                continue
            encryptor.stdin.write(f"ENCRYPT {text}\n")
            encryptor.stdin.flush()  
            response = encryptor.stdout.readline().strip()
            if response:
                print(response)
                if response.startswith("RESULT"):
                    history.append(response.split(" ", 1)[1])
                log_message(logger, "ENCRYPT", response)

        elif command == "decrypt":
            text = input("Enter text to decrypt:\n> ").strip().upper()
            if not text.isalpha():
                print("ERROR Input must contain only letters.")
                continue
            encryptor.stdin.write(f"DECRYPT {text}\n")
            encryptor.stdin.flush()  
            response = encryptor.stdout.readline().strip()
            if response:
                print(response)
                if response.startswith("RESULT"):
                    history.append(response.split(" ", 1)[1])
                log_message(logger, "DECRYPT", response)

        elif command == "history":
            print("\nHistory:")
            for i, item in enumerate(history, start=1):
                print(f"{i}. {item}")
            log_message(logger, "HISTORY", f"Displayed {len(history)} items.")

        elif command == "quit":
            log_message(logger, "STOP", "Driver Stopping.")
            encryptor.stdin.write("QUIT\n")
            encryptor.stdin.flush()
            logger.stdin.write("QUIT\n")
            logger.stdin.flush()
            encryptor.wait()
            logger.wait()
            break

        else:
            print("ERROR Invalid command.")
            log_message(logger, "ERROR", f"Invalid command: {command}")

if __name__ == "__main__":
    main()

