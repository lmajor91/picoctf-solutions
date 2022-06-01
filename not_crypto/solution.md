# Issue

after searching the program for strings and opening the program up in Ghidra,

we see that the user's input is being memcmp'd to the flag (this is hinted at via. the response messages)

we have no idea what the flag could be but the `memcmp` instruction is a promising start.

## Solution

if we open the program up in GDB and we sit at the `memcmp` command and we inspect the registers

```sh
(gdb) b memcmp
```

if we inspect the registers `rsi`, `rdi` and `rdx` we see that:

- the flag is in `rdi`
- our input is in `rsi`
- the size for the `memcmp` is in `rdx`

the flag is: "picoCTF{c0mp1l3r_0pt1m1z4t10n_15_pur3_w1z4rdry_but_n0_pr0bl3m?}"

