
def encryption_runner():
    """Asks user for choice of cypher and required data.
    Encrypts or decrypts the message and prints out to the screen
    """

    # format display nicely
    clear() # clear screen
    display_menu() # display menu choices
    cipher = get_cipher_choice() # inf. loop to get correct cypher code
    clear() # clears out
    
    # get from user if it is D or E
    # get the message to D or E
    # run the script
    # print out the E/D message
    # ask for rematch :) ?

    encode_decode = input(
        "I see, you want to use {}.\
        Are we encoding (E) or decoding (D) a message?".format(cipher))
    
    message = input(
        "Got it! I see, you want to use {}.\
        Are we encoding (E) or decoding (D) a message?".format(cipher))
    

    encode_message = 

    encode_choice = validate_encode_choice()
    message_code = run_cipher(cipher_choice, message, encode_choice)
    print(message_code.upper())    




if __name__ == "__main__":
    while True:
        pass  