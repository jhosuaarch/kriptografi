import string

alphabet = string.ascii_lowercase

def index(s):
    try:
        return alphabet.index(s.lower())
    except Exception as e:
        return None

def inverst(n):
    for i in range(100):
        if (n * i) % 26 == 1:
            return i

def upper(s):
    return alphabet[s].upper()

def repeat_key(t,k):
    if len(t) != len(k):
        r = len(t) // len(k) + 1 
        b = k * r 
        k = b[:len(t)]

    return k

