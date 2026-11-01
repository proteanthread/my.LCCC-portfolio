# Programming Assignment 7 - Strings
# Jeff Wood
# COSC 1010-500 26/FA - Dr. North
# 10-27-2026

# KEYPAD_LETTERS and KEYPAD_NUMBERS form the keypad lookup table:
KEYPAD_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEYPAD_NUMBERS = "22233344455566677778889999"

# PHONE_FORMAT is the pattern an entry must match
PHONE_FORMAT = "XXX-XXX-XXXX"
FORMAT_SLOT = "X"

def is_valid_format(phone_number):

    # Matches XXX-XXX-XXXX
    if len(phone_number) != len(PHONE_FORMAT):
        return False
    for index in range(len(PHONE_FORMAT)):
        expected = PHONE_FORMAT[index]
        character = phone_number[index]
        if expected == FORMAT_SLOT:
            if not (character.isascii() and character.isalnum()):
                return False
        elif character != expected:
            return False
    return True


def translate_number(phone_number):

    # Translate each letter to its keypad digit
    translated = ""
    for character in phone_number:
        if character.isascii() and character.isalpha():
            position = KEYPAD_LETTERS.index(character.upper())
            translated += KEYPAD_NUMBERS[position]
        else:
            translated += character
    return translated


def get_phone_number():

    prompt = f"Enter a telephone number in the format {PHONE_FORMAT}: "
    error = (f"Invalid entry. Use the format {PHONE_FORMAT}, where each "
             f"{FORMAT_SLOT} is a letter or digit.")

    # Prompt for a telephone number and strip spaces
    entry = input(prompt).strip()
    while not is_valid_format(entry):
        # Explain the error
        print(error)
        entry = input(prompt).strip()
    return entry


def main():
    # Request number from the user, translate it, and print the result.
    
    try:
        phone_number = get_phone_number()
    except (EOFError, KeyboardInterrupt):
        # Input ended
        print("\nNo telephone number entered. Goodbye.")
        return

    # Print the translated number
    print(f"Translated telephone number: {translate_number(phone_number)}")


# Program entry point

if __name__ == "__main__":
    main()
