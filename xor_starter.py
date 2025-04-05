
string = "label"

num = 13

final = ""
for letter in string:
    final = final + chr(ord(letter) ^ num)

print(final)