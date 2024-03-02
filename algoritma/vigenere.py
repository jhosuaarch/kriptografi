from . import get
from .data import Data
from itertools import zip_longest


class VigenereChiper:

    def __init__(self,key: str):
        self.key = key

    def encrypt(self,plaintext: str):
        chipertext = ""
        explain = ""
        explain += "Plaintext  : {}\n".format(plaintext)
        key = get.repeat_key(plaintext,self.key)
        for t,k in zip_longest(plaintext,key):
            text = get.index(t)
            keys = get.index(k)
            if text is not None and keys is not None:
                i = (text + keys) % 26
                c = get.upper(i)
                chipertext += c
                explain += f"{t} -> {text}\n{k} -> {keys}\n= {text} + {keys} mod 26\n= {str(text + keys)} mod 26\n= {str(i)} -> {c}\n\n"
        explain += f"= {chipertext}"

        return Data(chipertext=chipertext,explain=explain)

    def decrypt(self,chipertext: str):
        plaintext = ""
        explain = ""
        explain += "Chipertext  : {}\n".format(chipertext)
        key = get.repeat_key(chipertext,self.key)
        for t,k in zip_longest(chipertext,key):
            text = get.index(t)
            keys = get.index(k)
            i = (text - keys) % 26
            p = get.upper(i)
            plaintext += p
            explain += f"{t} -> {text}\n{k} -> {keys}\n= {text} - {keys} mod 26\n= {str(text - keys)} mod 26\n= {str(i)} -> {p}\n\n"
        explain += f"= {plaintext}"
        
        return Data(plaintext=plaintext,explain=explain)


