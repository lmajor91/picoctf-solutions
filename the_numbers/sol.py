# these are the numbers in the image "the_numbers.png"


root = [16, 9, 3, 15, 3, 20, 6] # {
inner= [20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14] # }

alphabet = "abcdefghijklmnopqrstuvwxyz"

if __name__ == "__main__":
    # need to shift the numbers one to the left because of indexing
    #   array indices start at 0, not 1
    
    flag = []
    [flag.append(alphabet[i-1]) for i in root]
    flag.append("{")
    [flag.append(alphabet[i-1]) for i in inner]
    flag.append("}")
    print(''.join(flag))

