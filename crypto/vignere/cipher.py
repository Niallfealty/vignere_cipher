""" Base crypto code shared by all/many algorithms
"""

class Cipher:
    """ Base class for encryption
    """
    def __init__(self, key):
        self._key = self._prep_key(key)

    def _prep_key(self, k):
        raise NotImplemented("[****] To be implemented by child classes")

    def _update_key(self, new_key):
        self._key = new_key

    def _encrypt(self, pt):
        raise NotImplemented("[****] To be implemented by child classes")

    def _decrypt(self, ct):
        raise NotImplemented("[****] To be implemented by child classes")

    def encrypt(self, pt):
        return self._encrypt(pt)

    def decrypt(self, ct):
        return self._decrypt(ct)

class Lookup:
    """ Lookup helper class
    """
    def __init__(self, dict_):
        self.dict_ = dict_

    def __getitem__(self, key):
        """ get item or return key if not present """
        return self.dict_.get(key, key)
