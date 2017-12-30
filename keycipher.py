from ciphers import Cipher

class Keyword(Cipher):
    """Encrypts or decrypts text using the Atbash cipher method."""

    def __init__(self, key):
        """
        Creates an instance of the class
        """
        
        self.alphabet = [chr(i) for i in range(65, 91)] # list comprehension to create alphabet list, more comments in Affine
        self.cipher_list = []

        # create cipher list from the test word
        for letter in key:
            self.cipher_list.append(letter)
        
        # add all of alphabet
        # everything above 26 characters will be dropped 
        # key can be over 26 characters as well, and will be dropped
        self.cipher_list = self.cipher_list = (self.cipher_list + self.alphabet)[:26]

    def encrypt(self, text):
        """Encrypts a string (text) message"""

        encrypted_list = []
        text = text.upper()
        for letter in text:
            try: # characters in alphabet are encrypted 
                letter_idx = self.alphabet.index(letter)
                
                encrypted_l = self.cipher_list[letter_idx]
                encrypted_list.append(encrypted_l)
            except ValueError: 
                # characters outside of range (of alphabet) stay the same
                encrypted_list.append(letter)
     
        return "".join(encrypted_list)

    def decrypt(self, text):
        """Decrypts a string (text) message"""
        
        decrypted_list = []
        text = text.upper()
        
        for letter in text:
            try:
                letter_idx = self.cipher_list.index(letter)
                decrypted_l = self.alphabet[letter_idx]
                decrypted_list.append(decrypted_l)
            except ValueError:
                decrypted_list.append(letter)
        
        return "".join(decrypted_list)