# rail-fence

this CTF was decently challenging, not the hardest. what stumped me the most was working around an example, applying the code which worked on the example and then watching it fail trying to decrypt the flag.

## Solution

the solution was instead of doing some math and trying to divide the string up into specific sizes, it was to recreate what the rails would have looked like during encryption of the plaintext.

the solution reflects this, the decryption function counts the amount of characters which should be on each rail.

then it creates indices to split up the ciphertext into parts.

finally, it turns the parts into plaintext by reading the parts in a zig-zag like format.

