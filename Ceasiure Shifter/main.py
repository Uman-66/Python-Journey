import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def cipher(start_text, shift_number, directions):
    end_text = ""

    if directions == "decode":
        shift_number *= -1
    for i in start_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = (position + shift_number) % 26
            end_text += alphabet[new_position]
        else:
            end_text += i
    print(f"Your {directions}d is {end_text}")


condition = True

while condition:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cipher(start_text=text, shift_number=shift, directions=direction)

    again = input("Do you wanna play again,, Yes or no")
    if again == "no":
        condition = False

print("Good Bye")