import os
from algoritma import CaesarChiper
from algoritma import AffineChiper
from algoritma import VigenereChiper



support = False


def banner():
    print("""┓┏┓  •           ┏•
┃┫ ┏┓┓┏┓╋┏┓┏┓┏┓┏┓╋┓
┛┗┛┛ ┗┣┛┗┗┛┗┫┛ ┗┻┛┗ 
      ┛     ┛
 > script by jhosua""")


def show_select(menu,home = True):
    print()
    for i,m in enumerate(menu):
        print(f"{i+1}). {m}")
    
    if home:
        print("0). exit")
    else:
        print("0). back")
    while True:
        try:
            choice =int(input("\n(pilih) > "))
            if choice <= len(menu):
                return choice - 1
        except ValueError:
            pass

def back():
    input("\n[!] press enter to continue... ")
    main()

def clear():
    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")
    else:
        pass

def show_answer(func,text,mode):
    if mode:
        answer = func.encrypt(text)
    else:
        answer = func.decrypt(text)
    
    # support check
    if support:
        print(answer.explain)
    else:
        print("[>] chipertext  : " + answer.chipertext if mode else "[>] plaintext   : " + answer.plaintext)
    back()

def input_text(mode):
    while True:
        text = input("\n[?] plaintext   : ") if mode else input("\n[?] chipertext  : ")
        if len(text) != 0:
            return text

def caesar_menu(mode):
    text = input_text(mode)
    shift = int(input("[?] shift       : "))
    func = CaesarChiper(shift)
    show_answer(func,text,mode)

def vigenere_menu(mode):
    text = input_text(mode)
    key = input("[?] key         : ")
    func = VigenereChiper(key)
    show_answer(func,text,mode)

def affine_menu(mode):
    text = input_text(mode)
    key_a = int(input("[?] key a       : "))
    key_b = int(input("[?] key b       : "))
    func = AffineChiper(key_a,key_b)
    show_answer(func,text,mode)


def main():
    clear()
    banner()
    func = [caesar_menu,vigenere_menu,affine_menu]
    pilih = show_select([
        "caesar",
        "vigenere",
        "affine",
    ])

    if pilih < 0: exit()

    mod = show_select([
        "encrypt",
        "decrypt"
    ],home=False)

    if mod < 0: main()

    if mod == 0: mode = True
    else: mode = False

    func[pilih](mode)


if __name__ == "__main__":
    main()
