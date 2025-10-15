# Виконання шифру Віженера для українського тексту (видимий користувачу код + вивід)
# Нормалізація: замінюємо латинську 'i' на українську 'і' якщо є.
plaintext = "криптографічнiметодизахистуінформації"
key = "сачовський"

# Український алфавіт (33 літери)
alphabet = list("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя")

# нормалізація: латинська i -> українська і, малі літери
plaintext = plaintext.replace("i", "і").lower()
key = key.lower()

def vigenere_encrypt(pt, key, alphabet):
    n = len(alphabet)
    alph_index = {ch: i for i, ch in enumerate(alphabet)}
    ct = []
    kpos = 0
    for ch in pt:
        if ch in alph_index:
            pi = alph_index[ch]
            ki = alph_index[key[kpos % len(key)]]
            ci = (pi + ki) % n
            ct.append(alphabet[ci])
            kpos += 1
        else:
            # зберігаємо символ без змін (якщо зустрінеться)
            ct.append(ch)
    return "".join(ct)

def vigenere_decrypt(ct, key, alphabet):
    n = len(alphabet)
    alph_index = {ch: i for i, ch in enumerate(alphabet)}
    pt = []
    kpos = 0
    for ch in ct:
        if ch in alph_index:
            ci = alph_index[ch]
            ki = alph_index[key[kpos % len(key)]]
            pi = (ci - ki) % n
            pt.append(alphabet[pi])
            kpos += 1
        else:
            pt.append(ch)
    return "".join(pt)

ciphertext = vigenere_encrypt(plaintext, key, alphabet)
decrypted = vigenere_decrypt(ciphertext, key, alphabet)

print("Нормалізований відкритий текст:")
print(plaintext)
print("\nКлюч:")
print(key)
print("\nЗашифрований текст (шифротекст):")
print(ciphertext)
print("\nРозшифрований назад текст:")
print(decrypted)

# Перевірка відповідності
print("\nПеревірка: розшифрування == початковий текст ->", decrypted == plaintext)
