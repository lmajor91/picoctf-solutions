
### functions

def printf(template, *args):
    print(template % args)

def moveToBack(l):
    element = l.pop()
    l.insert(0, element)    

### main solution

def main():
    fname = "message.txt"
    DIVIDER = ","

    with open(fname, 'r') as file:
        lines = file.readlines()

        # the hint for this CTF is to divide up the line
        # into block sizes

        sizes = range(2, 5+1)

        for line in lines:
            for size in sizes:
                print("using a block size of %d" % size)
                buffer = []
                shuffled = []
                for index, char in enumerate(line):
                    # appending to the buffer
                    buffer.append(char)
                    if (index+1) % size == 0:
                        # we've reached the buffer size,
                        # manipulating the buffer
                        moveToBack(buffer)
                        [shuffled.append(char) for char in buffer]
                        buffer = []

                # if there are leftover chars which didn't get
                # shuffled, add them to shuffled
                [shuffled.append(char) for char in buffer]

                # printing out the results
                print("".join(shuffled))

main()
