'''
--- main ---
this is a one time pad, since we have access to the otp we can effectively make it redundant

the reason why the OTP is so good, is that nobody knows the plaintext, because if you did it would become trivial to find the key

--- OTP encryption method ---

the OTP encrypts in the following method
plaintext ^ key = ciphertext

because we have access to the plaintext and the ciphertext;
    we can mathematically figure out the key
key = plaintext ^ ciphertext
key = plaintext ^ plaintext ^ key
key = key

if we xor the plaintext and the ciphertext we obtain the key
then if we xor the key and the encrypted flag, we obtain the
    plaintext flag

--- solution ---

we see that initially, the flag is ran through the OTP and because of the way the script is programmed, we move 32 chars into the key.

we need to be at the starting point of the key to obtain some ciphertext encrypted by the same key as the flag

in order to get the same key which was used on the flag, we need to send 50000-32=49968 chars to be encrypted to get back to the starting position.

then we can run our plaintext through the program to get the part of the key which was used to decrypt the flag

after that, using some math, we xor: the plaintext, the ciphertext and the encrypted flag to produce the plaintext flag

after that we turn the hex into ascii and submit the flag
'''


padhex = lambda char: '0x' + hex(ord(char)).lstrip('0x') * 32

ef =0x51466d4e5f575538195551416e4f5300413f1b5008684d5504384157046e4959
ea =0x03463d190702003d195004133d190356433d1902503d1950563d1900513d1959
pa =padhex('a')
#pa =0x6161616161616161616161616161616161616161616161616161616161616161

def resolve_key(pt, et, ef=ef):
    pt = int(pt, 16)
    r = '{:x}'.format(pt^et^ef)
    pk = ''.join([chr(int(r[i:i+2], 16)) for i in range(0, len(ascii(r))-2, 2)])
    return pk

print("the ascii plaintext flag is: picoCTF{%s}" % resolve_key(pa, ea))
