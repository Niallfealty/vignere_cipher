""" Encryption code for Vignere cipher
"""

from cipher import Cipher, Lookup
from reference import ALPHABET
from test_functions import test_result

class Caesar(Cipher):
    def __init__(self, key, alphabet=ALPHABET):
        super().__init__(key)
        self.alphabet = ALPHABET
        self.alpha_len = len(self.alphabet)
        self._build_lookups()

    def _prep_key(self, k):
        try:
            return int(k)
        except ValueError:
            print("Using a Caesar cipher requires an integer key")
            exit(1)

    def _build_lookups(self):
        self.encrypt_lookup = Lookup({
                    letter: ALPHABET[(i + self._key)%self.alpha_len]
                    for i, letter in enumerate(self.alphabet)
                })

        self.decrypt_lookup = Lookup({
                    letter: ALPHABET[(i - self._key)%self.alpha_len]
                    for i, letter in enumerate(self.alphabet)
                })


    def _encrypt(self, pt):
        return "".join(self.encrypt_lookup[letter] for letter in pt)

    def _decrypt(self, ct):
        return "".join(self.decrypt_lookup[letter] for letter in ct)

class Vignere(Cipher):
    def __init__(self, key):
        self.key = str(key) # printable key
        self.key_len = len(key)
        self.alphabet = ALPHABET
        self.alpha_len = len(self.alphabet)
        super().__init__(key)
        self._build_caesars()

    def _prep_key(self, k):
        print("t")
        return [self.alphabet.find(char) for char in k]

    def _build_caesars(self):
        ''' Build a caesar cipher for each key char
        '''
        self._ciphers = [Caesar(shift) for shift in self._key]

    def _prepare_pt(self, pt):
        ''' Join the pt into a continuous string of valid chars
            store the location of any non-valid chars
        '''
        pass

    def _is_encryptable(self, char):
        ''' Check if a character is encryptable
        '''
        return char in self.alphabet

    def _iterator_encrypt(self, pt):
        counter = 0
        encrypted_chars = []
        for char in pt:
            if self._is_encryptable(char):
                encrypted_chars.append(
                        self._ciphers[counter%self.key_len].encrypt(char))
                counter += 1
            else:
                encrypted_chars.append(char)

        return encrypted_chars

    def _encrypt(self, pt):
        return "".join(self._iterator_encrypt(pt))

    def _iterator_decrypt(self, pt):
        counter = 0
        decrypted_chars = []
        for char in pt:
            if self._is_encryptable(char):
                decrypted_chars.append(
                        self._ciphers[counter%self.key_len].decrypt(char))
                counter += 1
            else:
                decrypted_chars.append(char)

        return decrypted_chars

    def _decrypt(self, pt):
        return "".join(self._iterator_decrypt(pt))

#####################################################################
## Testing

def test_caesar():
    test_key = 5
    test_pt = "a test"
    test_ct = "f yjxy"

    caesar = Caesar(test_key)
    test_encrypt = test_result(test_ct == caesar.encrypt(test_pt))
    print(f"Caesar -> encrypt test: {test_encrypt}")
    test_decrypt = test_result(test_pt == caesar.decrypt(caesar.encrypt(test_pt)))
    print(f"Caesar -> decrypt test: {test_decrypt}")

def run_tests():
    test_caesar()

if __name__ == "__main__":
    run_tests()
