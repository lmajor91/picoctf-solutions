#!/usr/bin/python3 -u
import os.path

KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"

# it reads and encrypts the key and flag on startup

def startup(key_location):
	global FLAG_FILE

	# key_len doesn't matter here

	flag = open(FLAG_FILE).read()
	kf = open(KEY_FILE, "rb").read()

	start = key_location # 0
	stop = key_location + len(flag) # 0 + ???

	key = kf[start:stop]
	key_location = stop

    # xor inverse is: (a^b)^b == a
    # or, for the statement below: (p ^ k) ^ k == p
    # the length of the flag will have to equal the length of the key
	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
	print("This is the encrypted flag!\n{}\n".format("".join(result)))

	return key_location

def encrypt(key_location):
	global KEY_FILE, KEY_LEN

	ui = input("What data would you like to encrypt? ").rstrip()
	if len(ui) == 0 or len(ui) > KEY_LEN:
		return -1

	start = key_location
	stop = key_location + len(ui)

	kf = open(KEY_FILE, "rb").read()

	if stop >= KEY_LEN:
        stop = stop % KEY_LEN
		key = kf[start:] + kf[:stop]
	else:
		key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

	print("Here ya go!\n{}\n".format("".join(result)))

	return key_location


print("******************Welcome to our OTP implementation!******************")
c = startup(0)
print(c)
while c >= 0:
	c = encrypt(c)
