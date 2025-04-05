from Crypto.Util.number import *

key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key1 = bytes_to_long(key1)

KEY2_xor_KEY1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
KEY2_xor_KEY1 = bytes_to_long(KEY2_xor_KEY1)

KEY2_xor_KEY3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
KEY2_xor_KEY3 = bytes_to_long(KEY2_xor_KEY3)

key2 = key1 ^ KEY2_xor_KEY1

key3 = key2 ^ KEY2_xor_KEY3

FLAG_KEY1_KEY3_KEY2 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
FLAG_KEY1_KEY3_KEY2 = bytes_to_long(FLAG_KEY1_KEY3_KEY2)

flag = FLAG_KEY1_KEY3_KEY2 ^ key1 ^ key2 ^ key3

flag = long_to_bytes(flag)
print(flag.decode())
