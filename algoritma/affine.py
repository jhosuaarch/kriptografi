from . import get
from .data import Data

class AffineChiper:
    
    def __init__(self,a: int,b: int):
        self.a = a
        self.b = b

    def encrypt(self,plaintext: str):
        chipertext = ""
        explain = ""
        explain = "\nPlaintext : {}\n".format(plaintext)
        for text in plaintext:
            index = get.index(text)
            if index is not None:
                i = ((self.a * index) + self.b) % 26
                c = get.upper(i)
                chipertext += c
                explain += f"{text} -> {index}\n= ({str(self.a)} x {str(index)}) + {str(self.b)} mod 26\n= {str((self.a * index) + self.b)} mod 26\n= {str(i)} -> {c}\n\n"
            else:
                print("(skip) {} karena bukan alphabet".format(text))

        # Add result
        explain += "= " + chipertext
        
        return Data(chipertext=chipertext,explain=explain)
    
    def decrypt(self,chipertext: str):
        plaintext = ""
        explain = ""
        explain = "\nChipertext : {}\n".format(chipertext)
        for text in chipertext:
            index = get.index(text)
            prima = get.inverst(self.a)
            if index is not None:
                i = (prima * (index - self.b)) % 26
                p = get.upper(i)
                plaintext += p
                explain += f"{text} -> {index}\n= {str(prima)} x ({str(index)} - {str(self.b)}) mod 26\n= {str(prima)} x {str(index - self.b)} mod 26\n= {str(prima * (index - self.b))} mod 26 \n= {i} -> {p}\n\n"
            else:
                print("(skip) {} karena bukan alphabet".format(text))
                
        # Add result
        explain += f"= {plaintext}"

        return Data(plaintext=plaintext,explain=explain)


