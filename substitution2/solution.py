import string

fname = "message.txt"
VOID = "_"

def printf(template, *args):
    """
    this function is a rip of the printf function from C
    """
    print(template % args)

def appendUppercase(mapping):
    """
    this function adds the uppercase equivalent of each character
    into the dictionary
    """
    ret = {}
    for char in mapping:
        ret[char] = mapping[char]
        if char.upper() not in mapping:
            ret[char.upper()] = mapping[char].upper()
    return ret

def sliceDict(d, index):
    """
    this function slices a (sorted) dictionary on an index
    """
    ret = {}
    for key in list(dict.keys(d))[:index]:
        ret[key] = d[key]
    return ret

def sortDictByValues(d, reverse = True):
    """
    this function sorts a given dictionary based off of the
    dictionary's values
    """
    return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

def swapKeyValues(d):
    return {v: k for k, v in d.items()}

def printFrequencyTable(d, omit = False, kind = "letters"):
    """
    this function prints a dictionary in the format of a frequency
    table. by stating the amount of times a given key from the dict
    occurs, the occurence is the dictionary's value.

    this function automatically sorts the dictionary based
    on its values
    """
    d2 = sortDictByValues(d)
    if not omit:
        print("there are %d %s" % (len(d2), kind))
    for key in d2:
        print("%s occurs %d times" % (key, d2[key]))
    print()

def printMapping(mapping):
    print("here is the mapping")
    for key in mapping:
        if key.isupper():
            continue
        printf("'%s' binds to '%s'", key, mapping[key])
    print()

def mapEncryptedToChars(sorted_keys, subs, chart):
    """
    this function takes two lists and maps them together in sequence.
    this function also supports injection of values
    """
    ## need to map the keys
    ret = {}

    # doing subs first, they are more important
    for key in subs:
        ret[key] = subs[key]

    # then doing the keys
    for key in sorted_keys:
        if key not in ret:
            ret[key] = sorted_keys[key]

    return appendUppercase(ret)

def countCharacters(lines):
    """
    this function counts the frequency of a given character within
    some text
    """
    freqs = {}
    for line in lines:
        for char in line:
            if not char.isalpha():
                continue
            if char.isupper():
                char = char.lower()
            freqs[char] = line.count(char)
    return freqs

def charFrequency(fname):
    """
    this function counts the frequency of characters within a file
    """
    data = {}
    with open(fname, 'r') as file:
        data = countCharacters(file.readlines())
    return sortDictByValues(data)

def main():
    # vars
    fname = "message.txt"

    # these are directly hardcoded into the file based off of
    # observation and educated guesses
    mapping = {
        # certain, pulled from the end of the file which contains
        # the flag in its proper format
        "p": "p",
        "e": "i",
        "m": "c",
        "z": "o",
        "g": "t",
        "n": "f",
        # chars by observation
        'b': 'm',
        'j': 'e',
        'h': 'n',
        's': 'u',
        'w': 'r',
        'u': 's',
        'q': 'a',
        'v': 'h',
        'c': 'g',
        'x': 'l',
        'i': 'd',
        'f': 'b',
        'r': 'y',
        'a': 'v',
        'd': 'k',
        'k': 'w',
        'o': 'x',
        'l': 'q'
    }
    mapping = appendUppercase(mapping)

    # counting character frequencies
    charFreqs = charFrequency(fname)

    # taking some of the most frequent characters
    mostFreq = sliceDict(charFreqs, 7)

    print("here are the most frequent letters")
    printFrequencyTable(mostFreq, omit = True)

    # looking at the chars which aren't in the mapping, they could
    # probably be mapped
    for char in mostFreq:
        if char not in mapping:
            printf("%s not in mapping", char)
    printMapping(mapping)

    # decoding the file
    with open(fname, 'r') as file:
        # reading in data
        lines = file.readlines()

        # decrypting, keeping track of the decrypted lines
        decrypted = [] # decrypted text
        encrypted = [] # encrypted text
        for line in lines:

            # reading the text, trying to decrypt each char
            e_context, d_context = [], []
            for char in line:
                if not char.isalpha():
                    # random char, impossible to decrypt
                    d_context.append(char)
                    e_context.append(VOID)
                elif char in mapping:
                    # we can decrypt the char
                    d_context.append(mapping[char])
                    e_context.append(VOID)
                else:
                    # we can't decrypt the char
                    d_context.append(VOID)
                    e_context.append(char)

            # adding the contexts to their respective buffers
            encrypted.append(e_context)
            decrypted.append(d_context)

        allVoid = all([char == VOID for l in encrypted for char in l])
        
        # printing out all the unencrypted chars
        if not allVoid: 
            # printing out the encrypted and decrypted texts
            leftover = []
            for line in encrypted:
                for char in line:
                    if char != VOID:
                        if char not in leftover:
                            leftover.append(char)

            # printing
            print("couldn't decrypt %d chars: %s" % (len(leftover), ", ".join(leftover)), "\n")

            # omitting all of the encrypted characters
            print("visualizing the partially decrypted text:")
            for line in decrypted:
                print("".join(line))
            print()

            # merging the texts into one for reading
            print("merging both texts for observation")
            for line_index, line in enumerate(decrypted):
                for char_index, char in enumerate(line):
                    if char == VOID:
                        print(encrypted[line_index][char_index].upper(), end="")
                    else:
                        print(char, end="")
                print()
        else:
            # we've fully decrypted the file
            print("fully decrypted all characters")

            # doing another pass since we're printing in all
            #   uppercase
            for line in lines:
                print(''.join([
                    mapping[char]
                    if char in mapping
                    else char
                    for char in line
                ]))

main()

