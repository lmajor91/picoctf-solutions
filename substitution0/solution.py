import string

file = "message.txt"

# the encryption key is at the beginning of the file, need to read it

contents = []
key = ""

umapping = {}
lmapping = {}

with open(file, 'r') as f_in:
    key = f_in.readline()
    print("the key is %s" % key)
    for line in f_in.readlines():
        contents.append(line)

## creating mappings
# lowercase
for letter, char in zip(string.ascii_uppercase, key):
    umapping[char] = letter
# uppercase
for letter, char in zip(string.ascii_lowercase, key):
    lmapping[char.lower()] = letter

# decrypting the file
for line in contents:
    if line:
        for char in line:
            if char in umapping:
                print(umapping[char], end="")
            elif char in lmapping:
                print(lmapping[char], end="")
            else:
                print(char, end="")

