from . import get
from .data import Data

class CaesarChiper:

    def __init__(self,shift: int):
        self.shift = shift

    def encrypt(self,plaintext: str):
        chipertext = ""
        explain = ""
        explain += "\nPlaintext : {}\n".format(str(plaintext.upper()))
        
        for text in plaintext:
            index = get.index(text)
            if index is not None:
                i = (index + self.shift) % 26
                c = get.upper(i)
                chipertext += c
                explain += f"{text} -> {str(index)}\n= ({str(index)} + {str(self.shift)}) mod 26\n= {str((index + self.shift) % 26)}\n= {str(i)} -> {c}\n\n"
            
            else:
                print("(skip) -> {} karena bukan alphabet\n".format(text))
                continue

        # add result
        explain += f"= {chipertext}"
        return Data(chipertext=chipertext,explain=explain)

    def decrypt(self,chipertext: str):
        plaintext = ""
        explain = ""
        explain += "\nChipertext : {}\n".format(chipertext.upper())

        for text in chipertext:
            index = get.index(text)
            if index is not None:
                i = (index - self.shift) % 26
                p = get.upper(i)
                plaintext += p
                explain += f"{text} -> {str(index)}\n= ({str(index)} - {str(self.shift)}) mod 26\n= {str((index - self.shift) % 26)}\n= {str(i)} -> {p}\n\n"
            else:
                print("(skip) -> {} karena bukan alphabet\n".format(text))
        
        # add result
        explain += f"= {plaintext}"

        return Data(plaintext=plaintext,explain=explain)


