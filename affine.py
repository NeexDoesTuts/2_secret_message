import string
import random
ds
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
        self.alphabet = string.ascii_uppercase  # 'abcdefghijklmnopqrstuvwxyz'
        self.cipher_list = []
        for idx in range(len(self.alphabet)):
            self.cipher_list.append((self.alpha * idx + self.beta) % 26)

    def encrypt(self, text):
        pass
        
    def decrypt(self, text):
        pass
