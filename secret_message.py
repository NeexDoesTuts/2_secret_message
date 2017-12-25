import os

from affine import Affine
from caesar import Caesar

def clear():
    """Clears console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Displays manu of ciphers available for encoding messages"""

    menu = "Welcome! If you have a secret you are in a good place."\
            "\nHere is a set of great tools to keep you message"\
            " from unwanted attention:"\
            "\n1. Affine (A)"\
            "\n2. Caesar (C)"\
            "\n3. -"\
            "\n4. -"
    return menu

def get_cipher_choice(cipher_code_letters):
    """Asks for user's cipher choice against the available ciphers given
    as a list of code letters
    """
    
    cipher_choice = ""

    while cipher_choice.upper() not in cipher_code_letters:
        cipher_choice = input("Please pick corresponding letter to choose "\
                              "cipher\n>>> ").upper()
        if cipher_choice in cipher_code_letters: # if all OK, return
            return cipher_choice
        # TODO: add a Q for quitting the entire program with sys module
        print("Errrr, something went wrong.") # else, try again
        display_menu()

def run_cipher(cipher_object, message, encode_decode):
    """Runs encryption according to chosen cipher"""
    if encode_decode == "E":
        return cipher_object.encrypt(message)
    elif encode_decode == "D":
        return cipher_object.decrypt(message)


def main():
    """Asks user for choice of cypher and required data.
    Encrypts or decrypts the message and prints out to the screen
    """
    # available ciphers and their corresponding code names
    CIPHER_CODE_NAMES = {
        "A" : "Affine",
        "C" : "Ceasar"
    }
    CIPHER_CODE_LETTERS = []
    # names are created on the fly, from the given dictionary
    for key in CIPHER_CODE_NAMES:
        CIPHER_CODE_LETTERS.append(key)

    while True:
        clear() # clear screen
        print(display_menu()) # display menu choices
        cipher = get_cipher_choice(CIPHER_CODE_LETTERS) # get correct cypher code
        clear()
        # what cipher is it? assign instance to cipher
        if cipher == "A":
            # ask for required parameters
            alpha = int(input("Enter an alpha value. Available values:" \
                              ": 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25"\
                              "\n>>> "))
            while True:
                if alpha not in [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
                    clear()
                    print('Alpha value is not accepted. Please try again.\n')
                    alpha = int(input("Enter an alpha value. Available values:" \
                                      ": 3, 5, 7, 9, 11, 15, 17, 19, 21, 23,"\
                                       " 25\n>>> "))
                clear()
                break
            
            beta = input("Enter a beta value. Integers only.\n>>> ")
 
            while True:
                try:
                    beta = int(beta)
                    clear()
                    break
                except ValueError:
                    clear()
                    beta = input("Enter a beta value. Integers ONLY.\n>>> ")
                    continue
            cipher_object = Affine(alpha, beta)
        elif cipher == "C":
            cipher_object = Caesar()
        elif cipher == "":
            pass
        elif cipher == "":
            pass
        else:
            pass # TODO: fill in after working happy path

        clear()
        encode_decode = input(
            "I see, That is a good choice."\
            "\nAre we encoding (E) or decoding (D) a message?\n>>> ")
        
        clear()
        message = input(
            "Got it! I see what you are doing there.\n"\
            "What is the secret message?\n>>> ")

        # decrypt or encrypt the message
        en_de_message = run_cipher(cipher_object, message, encode_decode)

        # display secret message
        clear()
        print("This is your secret message:\n{}\nKeep it safe!\n".format(en_de_message))
        
        # run again or quit        
        run_again = input("Would you like to have another go? [N/y]\n>>> ").lower()
        if run_again != 'y':
            clear()
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
