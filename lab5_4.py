import base64
from Crypto.Util import number

def generate_keys(bits=1024):
    p = number.getPrime(bits)
    q = number.getPrime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    m_int = int.from_bytes(message.encode('utf-8'), 'big')
    c_int = pow(m_int, e, n)
    return base64.b64encode(c_int.to_bytes((c_int.bit_length() + 7) // 8, 'big')).decode('utf-8')

def decrypt(ciphertext, private_key):
    d, n = private_key
    c_int = int.from_bytes(base64.b64decode(ciphertext), 'big')
    m_int = pow(c_int, d, n)
    return m_int.to_bytes((m_int.bit_length() + 7) // 8, 'big').decode('utf-8')

public_key, private_key = generate_keys()
M = "Cryptography is fun and educational! Learning RSA encryption and decryption with Python helps understand public key cryptosystems."
ciphertext = encrypt(M, public_key)
plaintext = decrypt(ciphertext, private_key)

print("Ciphertext:", ciphertext)
print("Decrypted:", plaintext)
