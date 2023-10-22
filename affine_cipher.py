import argparse
import string
import os

# Define the alphabet
alphabet = string.ascii_lowercase

# Define the affine cipher function
def affine_cipher_encryption(text, a, b):
    encrypted_text = ""
    for char in text:
        if char.lower() in alphabet:
            if char.isupper():
                encrypted_text += chr(((a * (ord(char.lower()) - 97) + b) % 26) + 65)
            else:
                encrypted_text += chr(((a * (ord(char) - 97) + b) % 26) + 97)
        else:
            encrypted_text += char
    return encrypted_text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Affine Cipher Encryption from a text file")
    parser.add_argument("input_file", help="Path to the input text file")
    parser.add_argument("-k", "--keys", type=str, default="5,8", help="Keys for the Affine Cipher in the format 'a,b'")
    args = parser.parse_args()

    a, b = map(int, args.keys.split(','))

    with open(args.input_file, "r") as file:
        text = file.read()

    # Extract the file name from the input file path
    input_filename, extension = os.path.splitext(args.input_file)
    default_output_file = input_filename + "_encrypted" + extension

    # Encrypt the text using the affine cipher
    encrypted_text = affine_cipher_encryption(text, a, b)

    # Write the encrypted text to a new file
    with open(default_output_file, "w") as file:
        file.write(encrypted_text)

    print(f"Encrypted text has been written to {default_output_file}.")
