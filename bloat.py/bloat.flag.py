import sys

# alphabet
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
						"[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

def check_user_key(user_key):
    key = a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]
    print("the key is: %s" % key)
	if user_key == flag:
		return True
	else:
        # That password is incorrect
		print(a[51]+a[71]+a[64]+a[83]+a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+\
a[81]+a[67]+a[94]+a[72]+a[82]+a[94]+a[72]+a[77]+a[66]+a[78]+a[81]+\
a[81]+a[68]+a[66]+a[83])
		sys.exit(0)
		return False

def decrypt_key(encrypted_key):
    decryption_bytes = a[81]+a[64]+a[79]+a[82]+a[66]+a[64]+a[75]+a[75]+a[72]+a[78]+a[77] # rapscallion
    return deobfuscate_key(encrypted_key.decode(), decryption_bytes)

# this is the function to take a password
def get_key_from_user():
    # "Please enter correct password for flag: "
	return input(a[47]+a[75]+a[68]+a[64]+a[82]+a[68]+a[94]+a[68]+a[77]+a[83]+\
a[68]+a[81]+a[94]+a[66]+a[78]+a[81]+a[81]+a[68]+a[66]+a[83]+\
a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+a[81]+a[67]+a[94]+\
a[69]+a[78]+a[81]+a[94]+a[69]+a[75]+a[64]+a[70]+a[25]+a[94])

def read_enc_key():
	return open('flag.txt.enc', 'rb').read()

def show_success_message():
    # Welcome back... your flag, user:
	print(a[54]+a[68]+a[75]+a[66]+a[78]+a[76]+a[68]+a[94]+a[65]+a[64]+a[66]+\
a[74]+a[13]+a[13]+a[13]+a[94]+a[88]+a[78]+a[84]+a[81]+a[94]+a[69]+\
a[75]+a[64]+a[70]+a[11]+a[94]+a[84]+a[82]+a[68]+a[81]+a[25])

def deobfuscate_key(user_key, flag):
		arg433 = flag
		i = 0
		while len(arg433) < len(user_key):
				arg433 = arg433 + flag[i]
				i = (i + 1) % len(flag)				
		return "".join([chr(ord(arg422) ^ ord(arg442)) for (arg422,arg442) in zip(user_key,arg433)])


# this was taken from #'user_key
#   a straight string comparison, no bit math of any kind
print("flag: "+a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68])

# reading in the file as bytes
encrypted_key = read_enc_key()

## these first two functions are useless and can be skipped
#user_key = get_key_from_user()
#check_user_key(user_key)

# decryption suite
show_success_message()
flag = decrypt_key(encrypted_key)
print(flag)

sys.exit(0)

