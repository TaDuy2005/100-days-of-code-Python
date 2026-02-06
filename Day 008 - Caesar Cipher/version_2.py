def caesar(direction, original_text, shift_amount):
    modify_text = ''
    for letter in original_text:
        index = alphabet.index(letter)

        if direction == "encode":
            new_index = index + shift_amount
        elif direction == "decode":
            new_index = index - shift_amount

        new_index %= len(alphabet)
        modify_text += alphabet[new_index]
    return modify_text

from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

stop = False

while not stop:
    # --- direction input ---
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction != 'encode' and direction != 'decode':
        direction = input(
            "Invalid input. Please try again.\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    # --- input_text input ---
    input_text = input("Type your message (a-z):\n").lower()
    for text in input_text:
        while text not in alphabet:
            input_text = input("Invalid input. Please try again.\nType your message (a-z):\n").lower()
    
    # --- shift input ---
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except:
            print("Invalid input. Please try again.")

    print(f"Here's the {direction}d result: {caesar(direction, input_text, shift)}")

    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if user_input == 'yes':
        stop = False
    elif user_input == 'no':
        stop = True
    else:
        user_input = input("Invalid input. Type 'yes' if you want to go again. Otherwise type 'no'.\n")
