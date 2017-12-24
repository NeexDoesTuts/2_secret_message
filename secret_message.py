import os

def clear():
    """Clears console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Displays manu of ciphers available for encoding messages"""

    menu = """Welcome! If you have a secret you are in a good place.
Here is a set of great tools to keep you message from unwanted attention:
1. Affine (A)
2. Caesar (C)
3. -
4. -
"""
    return menu

def get_cipher_choice():
    """Validates the user's cipher choice against the available ciphers"""
    
    cipher_code_letters = ["A", "C"] 
    cipher_choice = ""

    while cipher_choice.upper() not in cipher_code_letters:
        cipher_choice = input("Please pick corresponding letter to choose "\
                              "cipher\n>>> ").upper()
        if cipher_choice in cipher_code_letters: # if all OK, return
            return cipher_choice
        # TODO: add a Q for quitting the entire program with sys module
        print("Errrr, something went wrong.") # else, try again
        display_menu()

def encryption_runner():
    """Asks user for choice of cypher and required data.
    Encrypts or decrypts the message and prints out to the screen
    """

    # format display nicely
    clear() # clear screen
    print(display_menu()) # display menu choices
    cipher = get_cipher_choice() # inf. loop to get correct cypher code
    # clear() # clears out
    
    # get from user if it is D or E
    # get the message to D or E
    # run the script
    # print out the E/D message
    # ask for rematch :) ?

    # encode_decode = input(
    #     "I see, you want to use {}.\
    #     Are we encoding (E) or decoding (D) a message?".format(cipher))
    
    # message = input(
    #     "Got it! I see, you want to use {}.\
    #     Are we encoding (E) or decoding (D) a message?".format(cipher))
    

    # encode_message = 

    # encode_choice = validate_encode_choice()
    # message_code = run_cipher(cipher_choice, message, encode_choice)
    # print(message_code.upper())    




if __name__ == "__main__":
    while True: # runs always until told to stop
        encryption_runner()
        run_again = input("Would you like to have another go?\n>>> ").lower()
        if run_again != 'y':
            break
