from Crypto.Util.number import *

challenge = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for key in range(256):
    decrypted = bytes([b ^ key for b in challenge])
    try:
        decoded_text = decrypted.decode()
        if "crypto" in decoded_text:
            print(f"Key: {key} | Message: {decoded_text}")
    except UnicodeDecodeError:
        pass
