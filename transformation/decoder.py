# you need to realize here that you are dealing with a bunch of hex characters
# not bytes, and that the code:

'''
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
'''

# is how the flag was encoded, not a hint on how to decode it

def read_flag(mode='r'):
    # reading in the flag
    return open("enc", mode).readline()

def print_flag(b = read_flag()):
    # casting to hex then removing the hex prefix
    raw_hex = [hex(ord(x)).lstrip('0x') for x in b]
    # splitting up the hex characters into single byte segments
    split_hex=[(x[:2],x[2:]) for x in raw_hex]
    # flattening the array
    flat_hex= [char for pair in split_hex for char in pair]
    # converting the hex characters to chars and forming a string
    return ''.join([chr(int(x, 16)) for x in flat_hex])

if __name__ == "__main__":
    print(print_flag())
