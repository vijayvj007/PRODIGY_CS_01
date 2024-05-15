def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            shifted = (ord(char) - base + shift_amount) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue
        
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value (an integer): "))
        
        if choice == 'e':
            encrypted_text = caesar_cipher(text, shift, 'encrypt')
            print("Encrypted text:", encrypted_text)
        else:
            decrypted_text = caesar_cipher(text, -shift, 'decrypt')
            print("Decrypted text:", decrypted_text)
        
        again = input("Do you want to try again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
