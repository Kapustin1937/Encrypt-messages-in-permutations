### Encode Messages in order of deck of cards!
run
```
python UI_Deck_Shuffle_Encoding.py
```
to use the program. \
There's also a version with permutations of a sequence of characters. \
below there's a pretty brief explanation of they both work.
### Encode messages in permutations of elements
A sequence of n elements has n! permutations \
We can assign every permutation a specific index using a [Lehmer Code](https://en.wikipedia.org/wiki/Lehmer_code)\
Now, we can interpret this number as a sequence of bits, and this sequence of bits as a binary message. \
***
### Usage:
Introduce a sequence of symbols\
Then a desired message in ascii\
\
The code will encode the message in a permutation of the symbols \
That's like all it does\
\
It can also decrypt them ig lmao go do it already
***
For a sequence of n symbols it can encode $`log_2(n!)`$ bits, which is approximately  $`\frac{log_2(n!)}{8}`$ symbols \
In theory we can calculate the amount of added bits per new element of the permutation using $`log_2((x+1)!)-log_2(x!)`$\
which is:
| new letter at position | bits added |
|------------------------|------------|
| 1 - 2                  | 1          |
| 3 - 6                  | 2          |
| 7-15                   | 3          |
| 16-31                  | 4          |

This isn't that real in practice so try to stick to the number in the program. \
Have fun!!!☻☻☻☻☻
