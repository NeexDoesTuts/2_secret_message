class Atbash(Cipher):
    """Encrypts or decrypts text using the Atbash cipher method."""

    def __init__(self):
        """
        Creates an instance of the class
        """

        self.alphabet = [chr(i) for i in range(65, 91)] # list comprehension to create alphabet list, more comments in Affine
        self.cipher_list = [chr(i) for i in range(90, 64, -1)] # and reversed one, more comments in Affine

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
        text = text.lower()
        
        for letter in text:
            try:
                letter_idx = self.cipher_list(letter)
                decrypted_l = self.alphabet.index(letter_idx)
                decrypted_list.append(decrypted_l)
            except ValueError:
                decrypted_list.append(letter)
        
        return "".join(decrypted_list)