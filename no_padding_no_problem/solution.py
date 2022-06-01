# need to reverse RSA encryption
"""
we can leverage the fact that the nc shell decrypts FOR us:
    = (c*2^e)^d
    = (c^d*2^(e*d)) because of math: e*d == 1 (mod lambda(n))
    = (c^d*2) and the ciphertext to the power of d is the plaintext
    = p*2
"""

n = int(input("n: "))
e = int(input("e: "))
c = int(input("ciphertext: "))

# need to include the modulus here
print("send in:", c * pow(2, e, n))

p = int(input("paste the result: "))

print("here is the result: {:x}".format(p//2))

# turning the hex into ascii
h = hex(p//2)[2:]
for i in range(0, len(h)-1, 2):
    print(chr(int(h[i:i+2], 16)), end="")
print()

