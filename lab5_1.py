cipher = "vppanlwxlyopyncjae"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_decrypt(text, key):
    out = ""
    for ch in text:
        if ch.isalpha():
            idx = alphabet.index(ch)
            out += alphabet[(idx - key) % 26]
        else:
            out += ch
    return out

for k in range(1, 26):
    print(k, caesar_decrypt(cipher, k))
