import sys

def vigenere_cipher(text, key, decrypt=False):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    key_length = len(key)
    result = []
    
    for i, char in enumerate(text):
        if char not in alphabet:
            result.append(char)
            continue
        key_char = key[i % key_length]
        key_index = alphabet.index(key_char)
        text_index = alphabet.index(char)

        if decrypt:
            new_index = (text_index - key_index) % 26
        else:
            new_index = (text_index + key_index) % 26
        
        result.append(alphabet[new_index])

    return "".join(result)

def main():
    password = None
    while True:
        try:
            command = sys.stdin.readline().strip()
            if not command:
                continue
            
            parts = command.split(" ", 1)
            action = parts[0]

            if action == "PASS":
                if len(parts) < 2:
                    print("ERROR Missing password.")
                    sys.stdout.flush()
                    continue
                password = parts[1].strip().upper()
                print("PASS OK")
                sys.stdout.flush()

            elif action == "ENCRYPT":
                if password is None:
                    print("ERROR No password set.")
                elif len(parts) < 2:
                    print("ERROR Missing text to encrypt.")
                else:
                    encrypted_text = vigenere_cipher(parts[1].strip().upper(), password)
                    print(f"RESULT {encrypted_text}")
                
                sys.stdout.flush()

            elif action == "DECRYPT":
                if password is None:
                    print("ERROR No password set.")
                elif len(parts) < 2:
                    print("ERROR Missing text to decrypt.")
                else:
                    decrypted_text = vigenere_cipher(parts[1].strip().upper(), password, decrypt=True)
                    print(f"RESULT {decrypted_text}")
                
                sys.stdout.flush()

            elif action == "QUIT":
                break

            else:
                print("ERROR Invalid command.")
                sys.stdout.flush()
                
        except EOFError:
            break

if __name__ == "__main__":
    main()

