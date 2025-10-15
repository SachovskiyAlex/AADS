import random
from math import gcd

def is_probable_prime(n, k=8):
    """Імовірнісна перевірка простоти методом Міллера–Рабіна."""
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits=16):
    while True:
        p = random.getrandbits(bits) | (1 << bits - 1) | 1  # непарне число з ведучим бітом
        if is_probable_prime(p):
            return p

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception("Оберненого не існує!")
    return x % m

BITS = 20  

p = generate_prime(BITS)
q = generate_prime(BITS)
while q == p:
    q = generate_prime(BITS)

n = p * q
phi = (p - 1) * (q - 1)
e = 65537
if gcd(e, phi) != 1:
    e = 3
    while gcd(e, phi) != 1:
        e += 2

d = modinv(e, phi)
M = 100
C = pow(M, e, n)
M_dec = pow(C, d, n)

print("=== RSA Демонстрація ===")
print(f"p = {p}")
print(f"q = {q}")
print(f"n = {n}")
print(f"phi(n) = {phi}")
print(f"e (публічний ключ) = {e}")
print(f"d (приватний ключ) = {d}")
print("\n--- Шифрування/Розшифрування ---")
print(f"Відкритий текст M = {M}")
print(f"Шифротекст C = M^e mod n = {C}")
print(f"Розшифрований текст M_dec = C^d mod n = {M_dec}")
print("\nПеревірка:", M == M_dec)
