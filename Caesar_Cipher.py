alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    cipher_text = ""

    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter

    print(f"the encoded text is {cipher_text}")

def decrypt(encrypted_text, shift_amount):
    decoded_text = ""

    for letter in encrypted_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            decoded_text += alphabet[new_position]
        else:
            decoded_text += letter

    print(f"the decoded text is {decoded_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if(direction == 'encode'):
    encrypt(plain_text = text, shift_amount = shift)

if(direction == 'decode'):
    decrypt(encrypted_text = text, shift_amount = shift)
