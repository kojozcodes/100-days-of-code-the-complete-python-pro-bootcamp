alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(cipher_text, shift_amount, cipher_direction):

    encrypted_or_decrypted_text = ""

    #Angela solution
    # if cipher_direction == "decode":
    #       shift_amount *= -1
    # new_position = position += shift_amount
    
    for letter in cipher_text:
        position = alphabet.index(letter)

        if cipher_direction == "encode":
            position = position + shift_amount
        elif cipher_direction == "decode":
            position = position - shift_amount
        encrypted_or_decrypted_text += alphabet[position]

    print(f"The {cipher_direction}d text is {encrypted_or_decrypted_text}")

caesar(cipher_text=text, shift_amount=shift, cipher_direction=direction)