from ciphers import Cipher


class Affine(Cipher):
    """Encrypts or decrypts text using the Affine cipher method."""

    def __init__(self, alpha, beta):
        """
        Creates an instance of the class using given values for alpha and beta.
        The cipher shift formula is: (alpha * letter_index + beta) % 26
        """
        possible_alpha_values = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

        self.alpha = alpha
        self.beta = beta
        self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                         "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                         "W", "X", "Y", "Z"]
        self.cipher_list = []
        for idx in range(len(self.alphabet)):
            self.cipher_list.append((self.alpha * idx + self.beta) % 26)

    def encrypt(self, text):
        """Encrypts a string (text) message"""

        encrypted_list = []
        text = text.upper()
        for letter in text:
            try: # characters in alphabet are encrypted 
                letter_idx = self.alphabet.index(letter)
                encrypted_l = self.alphabet[self.cipher_list[letter_idx]]
                encrypted_list.append(encrypted_l)
            except ValueError: 
                # characters outside of range (of alphabet) stay the same
                encrypted_list.append(letter)
     
        return "".join(encrypted_list)

    def decrypt(self, text):
        """Decrypts a string (text) message"""
        
        decrypted_list = []
        text = text.lower()
        
        for letter in text:
            try:
                letter_idx = self.alphabet.index(letter)
                decrypted_l = self.alphabet[self.cipher_list.index(letter_idx)]
                decrypted_list.append(decrypted_l)
            except ValueError:
                decrypted_list.append(letter)
        
        return "".join(decrypted_list)
