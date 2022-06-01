import string

# this is the encrypted flag
encflag = "mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj"

LOWERCASE_OFFSET = ord("a")						 # 97
ALPHABET = string.ascii_lowercase[:16]	# abcedfghijklmnop

def b16_encode(plain):
	global ALPHABET

	enc = ""
	for c in plain:
		# takes a digit and divides it into it's upper and lower bounds
		#	 casts to a char based off of this
		binary = "{0:08b}".format(ord(c))
		a = ALPHABET[int(binary[:4], 2)] # lower
		b = ALPHABET[int(binary[4:], 2)] # upper
		enc += a
		enc += b
		print("'%c' -> '%c%c'" % (c, a, b))

		# len(enc) == len(plain)*2
	return enc

def b16_decode(encoded):
	global ALPHABET

	dec = ""
	for i in range(0, len(encoded)-1, 2):
		a = encoded[i]
		b = encoded[i+1]

		binary = "{0:04b}{1:04b}".format(
				ALPHABET.index(a),
				ALPHABET.index(b))

		dec += chr(int(binary, 2))

	return dec

def shift(c, k):
		global LOWERCASE_OFFSET
		
		t1 = ord(c) - LOWERCASE_OFFSET
		t2 = ord(k) - LOWERCASE_OFFSET
		
		index = (t1 + t2) % len(ALPHABET)
		
		ret = ALPHABET[index]
		#print("(%c + %c) -> ALPHABET[%d] = %c" % (c, k, index, ret))
		return ret

def unshift(c, mod='a'):
		global LOWERCASE_OFFSET

		# we're given a letter from the base 16 alphabet, we need
        #   to do the inverse of the shifting function

		# c = ALPHABET[index]
		index = ALPHABET.index(c)

		# index = (t1 + t2) % len(ALPHABET)
		t2 = ord(mod) - LOWERCASE_OFFSET
		t1 = (index - t2) % len(ALPHABET)
		# print(t1)

		# t1 = ord(c) - LOWERCASE_OFFSET
		# t2 = ord(k) - LOWERCASE_OFFSET
		ret = chr(t1 + LOWERCASE_OFFSET)

		#print("%c = (%c + %c) -> %c" % (c, chr(t1), chr(t2), ret))
		return ret
		

# weird assertions
flag = "redacted"
# key = "redacted" # old
key = "a" # new

# these are clues about the key, these assertions tell us that;
#   - the key must be within the alphabet
#   - the key must have a length of one
#   we can leverage both of these clues in `brute_caesar()'
assert all([k in ALPHABET for k in key])
assert len(key) == 1

def brute_caesar(flag=encflag):
    global ALPHABET

    collection = []

    # we can leverage a clue about the key, the fact that there is an
    #   assertion for len(key) == 1, which means the key is one character
    #   and that the key must be within the base16 letter alphabet
    for k in ALPHABET:
        enc = "".join([unshift(e, mod=k) for e in flag])
        # encoding the result so that it looks better
        #   we can pick the correct answer from the rest from the one
        #   that looks the most normal
        res = b16_decode(enc).encode('utf-8')
        print("flag with %c -> %s" % (k, res))
        collection.append(res)

    return collection

def do_caesar(flag=flag, key=key):
    # encoding the flag
    b16 = b16_encode(flag)
    enc = ""
    for i, c in enumerate(b16):
    	enc += shift(c, key[i % len(key)])

    return enc

