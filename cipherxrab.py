import getpass

# Banner for the program
banner = """
░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░██╗░░██╗  ██████╗░░█████╗░██████╗░
██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗╚██╗██╔╝  ██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝░╚███╔╝░  ██████╔╝███████║██████╦╝
██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗░██╔██╗░  ██╔══██╗██╔══██║██╔══██╗
╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║██╔╝╚██╗  ██║░░██║██║░░██║██████╦╝
░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░
"""
print(banner)
print("----------------------------------- Caesar Cipher Tool By techno-rabit -----------------------------------")
print("")

def analyze_message(message):
    num_letters = sum(c.isalpha() for c in message)
    num_digits = sum(c.isdigit() for c in message)
    num_special = len(message) - num_letters - num_digits

def caesar_cipher(text, shift, action):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            if action == 'e':
                result_char = chr((ord(char) - start + shift) % 26 + start)
            elif action == 'd':
                result_char = chr((ord(char) - start - shift) % 26 + start)
            else:
                raise ValueError("Invalid action. Use 'e' to encrypt or 'd' to decrypt")
            result += result_char
        else:
            result += char
    return result

def main():
    while True:
        action = input("Do you want to encrypt or decrypt a message? Input 'e' for encryption, 'd' for decryption, or 'q' to quit: ").lower()
        if action == 'q':
            print("Exiting the program. Goodbye!")
            return
        elif action in ['e', 'd']:
            break
        else:
            print("Invalid action. Please choose 'e', 'd', or 'q' to quit.")

    if action == 'q':
        return

    # Use of getpass to make the message input invisible
    message = getpass.getpass(prompt="Enter the message (invisible, type carefully): ")

    while True:
        view_message = input("Would you like to view and possibly edit the entered message? (y/n): ").lower()
        if view_message == 'y':
            print("\nEntered Message:", message)
            edit_message = input("Would you like to edit the message? (y/n): ").lower()
            if edit_message == 'y':
                message = input(f"Edit the message (Current message: '{message}'): ") or message
                print("\nEdited Message:", message)
            break
        elif view_message == 'n':
            break
        else:
            print("Invalid choice. Please enter 'y' for yes or 'n' for no.")

    analyze_message(message)
    
    # Use of getpass to make the shift value input invisible
    shift = int(getpass.getpass(prompt="Enter the shift value (invisible, type carefully): "))

    while True:
        view_shift = input("Would you like to view and possibly edit the entered shift value? (y/n): ").lower()
        if view_shift == 'y':
            print("\nEntered Shift Value:", shift)
            edit_shift = input(f"Edit the shift value (Current shift: {shift}): ")
            shift = int(edit_shift) if edit_shift else shift
            print("\nEdited Shift Value:", shift)
            break
        elif view_shift == 'n':
            break
        else:
            print("Invalid choice. Please enter 'y' for yes or 'n' for no.")

    if action == 'e':
        result = caesar_cipher(message, shift, 'e')
        print("\nEncrypted Message:", result)
    elif action == 'd':
        result = caesar_cipher(message, shift, 'd')
        print("\nDecrypted Message:", result)

     # Prompt to follow on GitHub
    print("\nIf you found this tool useful, consider following me on GitHub: https://github.com/techno-rabit")

if __name__ == "__main__":
    main()
