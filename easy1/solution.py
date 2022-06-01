import string
table = []

# creating the table

table = {}
for i in string.ascii_uppercase:
    table[i] = {}
    for j in string.ascii_uppercase:
        index = ord(i) + ord(j) - (2*ord('A'))
        table[i][j] = string.ascii_uppercase[index % 26]

enc = "UFJKXQZQUNB"
key = "SOLVECRYPTO"

# using key and enc, we can extract the plaintext

plaintext = ""

'''
reverse this code
for p in plaintext:
    for k in key:
        enc += table[p][k]
        # or
        enc += table[k][p]
'''

for i, k in enumerate(key):
    for p in string.ascii_uppercase:
        if table[k][p] == enc[i]:
            plaintext += p

print("flag: picoCTF{%s}" % plaintext)
