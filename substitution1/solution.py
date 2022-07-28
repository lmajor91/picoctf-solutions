
fname = "message.txt"

# this function uppercases letters and adds them into a dictionary
def appendUppercase(mapping):
    ret = {}
    for char in mapping:
        ret[char] = mapping[char]
        ret[char.upper()] = mapping[char].upper()

    return ret

# these are directly hardcoded into the file based off of
# observation and educated guesses
substitution = {
    # certain, pulled from the end of the file which contains
    # the flag in its proper format
    "z": "p",
    "d": "i",
    "i": "c",
    "f": "o",
    "e": "t",
    "c": "f",
    "j": "s",
    # unsure
    "x": "a",
    "y": "n",
    "r": "m",
    "s": "e",
    "k": "d",
    "u": "r",
    'a': 'g',
    'o': 'l',
    'q': 'h',
    'g': 'v',
    't': 'b',
    'm': 'y',
    'l': 'u',
    'h': 'w',
    'n': 'q',
    'p': 'k'
}

# need to add the uppercase letters to the mapping
mapping = appendUppercase(substitution)

# decoding the file
with open(fname, 'r') as file:
    for line in file.readlines():
        print("".join([
            mapping[char]
            if char in mapping
            else char
            for char in line
        ]))
