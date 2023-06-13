#!/usr/bin/env python3
from args import parser
from shift_ciphers import Caesar, Vignere

class Main:
    def __init__(self):
        args = parser.parse_args()
        self.cipher = args.cipher if args.cipher is not None else "c"
        self.key = args.key
        self.msg = args.msg
        self.encrypt = args.encrypt
        self.decrypt = args.decrypt

    def _caesar_encrypt(self):
        """ Default is to encrypt if both are set
        """
        if self.encrypt:
            return Caesar(self.key).encrypt(self.msg)

        elif self.decrypt:
            return Caesar(self.key).encrypt(self.msg)

    def _vignere_encrypt(self):
        if self.encrypt:
            return Vignere(self.key).encrypt(self.msg)

        elif self.decrypt:
            return Vignere(self.key).encrypt(self.msg)
     
    def _run(self):
         if self.cipher.lower() in ("c", "caesar"):
             return self._caesar_encrypt()
         elif self.cipher.lower() in ("v", "vignere"):
             return self._vignere_encrypt()

    def run(self):
         print(self._run())

if __name__ == "__main__":
    Main().run()
