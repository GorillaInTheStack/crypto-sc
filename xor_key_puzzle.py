
ciphertext = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

known_plaintext = b"crypto{" # the key might be small and repeating since the ct is long and the hint is this
key_guess = bytes([c ^ ciphertext[i] for i, c in enumerate(known_plaintext)])

print(f"Recovered key segment: {key_guess}")
# Recovered key segment: b'myXORke'

possible_key = b'myXORkey'

key_length = len(possible_key)
full_key = (possible_key * (len(ciphertext) // key_length + 1))[:len(ciphertext)]

decrypted_flag = bytes([c ^ full_key[i] for i, c in enumerate(ciphertext)])

print(f"Decrypted flag: {decrypted_flag.decode()}")
