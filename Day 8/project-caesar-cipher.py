alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(cipher_text, shift_amount, cipher_direction):

    encrypted_or_decrypted_text = ""

    #Angela solution
    # if cipher_direction == "decode":
    #       shift_amount *= -1
    # new_position = position += shift_amount
    
    for char in cipher_text:

        if char in alphabet:       
            position = alphabet.index(char)
            if cipher_direction == "encode":
                position = position + shift_amount
            elif cipher_direction == "decode":
                position = position - shift_amount
            encrypted_or_decrypted_text += alphabet[position]
        else:
            encrypted_or_decrypted_text += char

    print(f"The {cipher_direction}d text is {encrypted_or_decrypted_text}")

from art import logo
print(logo)

should_continue = True
while should_continue:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(cipher_text=text, shift_amount=shift, cipher_direction=direction)
    
    user_choice = input("Type 'yes' if you would you like to continue or 'no' if you don't want to continue.").lower()
    if user_choice == "no":
        should_continue = False
        print("Goodbye")


