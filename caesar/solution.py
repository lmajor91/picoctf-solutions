# decrypt the ciphertext

CIPHERFILE = "ciphertext"

enc_flag = open(CIPHERFILE, 'r').readline()

parts = [
        enc_flag[:enc_flag.index('{')],
        '{',
        enc_flag[enc_flag.index('{')+1:enc_flag.index('}')],
        '}'
        ]
enc = parts[2]

# just a nice way of printing out the flag
assemble = lambda x: "".join([parts[0], parts[1], x, parts[3]])

import string

ALPHABET = string.ascii_lowercase
OFFSET = ord('a')

# making sure the encrypted flag is within the alphabet
assert all([e in ALPHABET for e in enc])

# shift by distance
def shiftd(p, dist, ALPHA=ALPHABET, OFF=OFFSET):
    # shifting the letters to the start of the alphabet
    a = ord(p) - OFF # plaintext

    # returning the shifted character
    return ALPHA[(a + dist) % len(ALPHA)]

# shift by character
def shiftc(p, k, ALPHA=ALPHABET, OFF=OFFSET):
    # shifting the letters to the start of the alphabet
    a = ord(p) - OFF # plaintext
    b = ord(k) - OFF # key

    # returning the shifted character
    return ALPHA[(a + b) % len(ALPHA)]

# string shift
def sshift(s, mod, ALPHA=ALPHABET, OFF=OFFSET):
    move = None
    if isinstance(mod, int):
        move = shiftd
    elif isinstance(mod, str):
        move = shiftc
    else:
        return -1

    # applying the shift
    return "".join(
            list(
                map(lambda x: move(x, mod, ALPHA=ALPHA, OFF=OFF), s)))

# trying to brute force the cipher
for i in range(len(ALPHABET)):
    r = sshift(enc, i)
    print("shift by %2d -> %s" % (i, assemble(r)))

