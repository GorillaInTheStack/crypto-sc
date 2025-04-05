import base64

flag_inhex = bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")

flag_inbase64 = base64.b64encode(flag_inhex)

print(flag_inbase64)
