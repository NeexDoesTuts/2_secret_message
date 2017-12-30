import os

from affine import Affine
from caesar import Caesar
from atbash import Atbash
from keycipher import Keyword

def clear():
    """Clears console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu(cypher_dict):
    """Displays manu of ciphers available for encoding messages"""

    # create message from given Cyphers
    menu = "Welcome! If you have a secret you are in a good place."\
            "\nHere is a set of great tools to keep you message"\
            " from unwanted attention:"

    idx = 1
    for key, value in cypher_dict.items():
        menu += "\n{}. {} - ({})".format(idx, value, key)
        idx += 1
    return menu

def get_cipher_choice(cipher_dict):
    """Asks for user's cipher choice against the available ciphers given
    as a list of code letters
    """
    # create codes on the fly
    cipher_code_letters = []

    for key in cipher_dict:
        cipher_code_letters.append(key)

    cipher_choice = ""

    while cipher_choice.upper() not in cipher_code_letters:
        cipher_choice = input("Please pick corresponding letter to choose "\
                              "cipher\n>>> ").upper()
        if cipher_choice in cipher_code_letters: # if all OK, return
            return cipher_choice
        # TODO: add a Q for quitting the entire program with sys module
        print("Errrr, something went wrong.") # else, try again
        display_menu(cipher_dict)

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
        "AT" : "Atbash",
        "C" : "Ceasar",
        "K" : "Keyword"
    }

    while True:
        clear() # clear screen
        print(display_menu(CIPHER_CODE_NAMES)) # display menu choices
        cipher = get_cipher_choice(CIPHER_CODE_NAMES) # get correct cypher code
        clear()
        # what cipher is it? assign instance to cipher

        if cipher == "A":
            # ask for required parameters
            alpha = input("Enter an alpha value. Available values:" \
                          ": 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25"\
                          "\n>>> ")
            while True:
                try:
                    alpha = int(alpha)
                    break
                except ValueError:
                    clear()
                    alpha = input("I do not think it is an integer. Try again."\
                                  " Available values: 3, 5, 7, 9, 11, 15, 17,"\
                                  " 19, 21, 23, 25\n>>> ")
                    continue

            while True:
                if alpha not in [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
                    clear()
                    print('Alpha value is not within the range. Please try again.\n')
                    alpha = int(input("Available values: 3, 5, 7, 9, 11, 15, 17, 19"\
                                      ", 21, 23, 25.\n>>> "))
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

            cipher_object = Affine(alpha, beta)
        elif cipher == "AT":
            cipher_object = Atbash()
        elif cipher == "C":
            cipher_object = Caesar()
        elif cipher == "K":
            # ask for the keyword
            key = input("What keyword word would you like to use to en(de)crypt your message?\n>>> ")
            while True:
                if len(key) > 1: # the key cannot be 0, as this will change nothing, it can be non alphabet characters
                    break
                else:
                    clear()    
                    key = input("You need at least one character, although the more the better.\n>>>")
            cipher_object = Keyword(key)

        clear()
        encode_decode = input(
            "I see, That is a good choice."\
            "\nAre we encoding (E) or decoding (D) a message?\n>>> ").upper()
        
        while encode_decode not in ["E", "D"]:
            clear()
            encode_decode = input ("This is not a valid choice."\
                                   "\nWe can encode (E) or decode (D)\n>>> ").upper()

        clear()
        message = input(
            "Got it! I see what you are doing there.\n"\
            "What is the secret message?\n>>> ")

        # decrypt or encrypt the message
        en_de_message = run_cipher(cipher_object, message, encode_decode)

        # display secret message
        clear()
        print("Your original message: \n{}\n".format(message.upper()))
        print("This is your secret message:\n{}\nKeep it safe!\n".format(en_de_message))
        
        # run again or quit        
        run_again = input("Would you like to have another go? [N/y]\n>>> ").lower()
        if run_again != 'y':
            clear()
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
