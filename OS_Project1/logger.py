import sys
import datetime

def log_message(log_file, message):
    """Writes a log entry to the specified log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    parts = message.split(" ", 1)
    action = parts[0] if len(parts) > 0 else "UNKNOWN"
    msg = parts[1] if len(parts) > 1 else "No message provided."
    
    with open(log_file, "a") as file:
        file.write(f"{timestamp} [{action}] {msg}\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 logger.py <log_file>")
        return

    log_file = sys.argv[1]
    log_message(log_file, "START Logging Started.")

    while True:
        try:
            line = sys.stdin.readline().strip()
            if not line:
                continue
            if line == "QUIT":
                log_message(log_file, "STOP Logging Stopped.")
                break
            log_message(log_file, line)
        except Exception as e:
            log_message(log_file, f"ERROR Logger encountered an error: {e}")

if __name__ == "__main__":
    main()

