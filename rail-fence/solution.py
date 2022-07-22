def unrail(text, rails):
    ## implementing decryption from wikipedia
    period = 2 * (rails - 1) # setting the period
    L = len(text) # length of the ciphertext
    ciphertext = text

    # need to map an index to a rail number (they zigzag)
    # this creates a number pyramid which is exactly what we need
    # to properly index the rails and create the plaintext
    def rail_index(x, period=period, rails=rails):
        ret = x % period
        modrail = rails - 1
        if ret > modrail:
            amount = (ret - modrail) * 2
            ret -= amount
        return ret

    ## need to think diagonally, we need to think about reconstructing
    ## the rails themselves, then we can figure out the plaintext

    # forming the number of letters that are in each rail
    indicies = [rail_index(index) for index in range(L)]
    rail_counts = []
    for rail in range(rails):
        rail_counts.append(indicies.count(rail))

    ## calculating indices to split the ciphertext up into strings
    ## which correspond to each rail during encryption

    # forming indices
    rolling_rails = [sum(rail_counts[:index+1]) for index, _ in enumerate(rail_counts)]

    # splitting up the strings into parts
    #    given by the calculated indices
    last = 0
    railed = []
    for index in rolling_rails:
        if last != 0:
            railed.append(ciphertext[last:index+1])
        else:
            railed.append(ciphertext[:index])
        last = index

    ## forming the plaintext
    plaintext = ""
    counts = [0 for _ in range(L)] # tracking an index per rail
    for index in range(L):
        # creating an index
        i = rail_index(index)

        # pulling the proper character from the proper rail
        plaintext += railed[i][counts[i]]

        # updating the rail's index
        counts[i] += 1
    
    # returning the plaintext
    return plaintext

flag = "Ta _7N6D49hlg:W3D_H3C31N__A97ef sHR053F38N43D7B i33___N6"
test1 = "WECRUOERDSOEERNTNEAIVDAC"
test2 = "WVOEOETNACRACRSENEEIDUDR"

# making sure that the decryption funtion works
assert unrail(test1, 3) == "WEAREDISCOVEREDRUNATONCE"
assert unrail(test2, 6) == "WEAREDISCOVEREDRUNATONCE"

# need to split the text since there is beginning text that says
# "The flag is:"
print("picoCTF{%s}" % unrail(flag, 4).split(" ")[3])

