# transposition-trial

This CTF gives you a string which has been manipulated, every block of text has been shifted one to the left (wrapping around)
the goal of this CTF is to find the correct block size and shift the letters back.

## Solution

By iterating over possible block sizes, one can reverse each block and then reassemble the entire string. Then by observation (or
by looking at the hints given by the CTF) you can deduce that the flag is properly decrypted when the block size is `3`

