# need to decrypt a message from RSA

# we have n, e and the ciphertext

n, e, ciphertext = 0, 0, 0

with open("ciphertext", "r") as f:
    lines = f.readlines()
    n = int(lines[0].split(' ')[1])
    e = int(lines[1].split(' ')[1])
    ciphertext = int(lines[2].split(' ')[2])

def nth_root(x, n):
    # Start with some reasonable bounds around the nth root.
    upper_bound = 1
    while upper_bound ** n <= x:
        upper_bound *= 2
    lower_bound = upper_bound // 2
    # Keep searching for a better result as long as the bounds make sense.
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** n
        if lower_bound < mid and mid_nth < x:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > x:
            upper_bound = mid
        else:
            # Found perfect nth root.
            return mid
    return mid + 1

target = "".join([hex(ord(c)).lstrip("0x") for c in "pico"])
plaintext = ""
for i in range(4000):
    s = "{:x}".format(nth_root(ciphertext + (i * n), e))
    if target in s:
        print(s)
        plaintext = s

# converting hex to ascii
import binascii
# removing the white space
print("flag: %s" % binascii.unhexlify(plaintext.lstrip("20")))

