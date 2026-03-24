from factoradic_converter import *
from math import factorial

string = list("12345678")

def Permutate_with_lehmer(sequence, lehmer_code_prev):
    """
    Permutates a list using its lehmer code
    """

    lehmer_code = ([0]*(len(sequence)-len(lehmer_code_prev)))
    lehmer_code.extend(lehmer_code_prev)
    encoded = [""]*len(sequence)
    for i in range(len(lehmer_code)):
        # Returns the index of the nth empty cell in the list
        position = [i for i, n in enumerate(encoded) if n == ''][lehmer_code[i]]
        encoded[position] = sequence[i]
    return encoded

def encode(sequence, index):
    "Permutates a list using the index of the permutation"
    lehmer_code = dec_to_fact(index)

    return Permutate_with_lehmer(sequence, lehmer_code)

def decode(sequence, index):
    "Permutates a list using the index of the permutation"
    # Figure out how to actually do this!!!
    #fact = factorial(len(sequence))
    #decode_index = (fact - index) % (fact - 1)
    #return encode(sequence, decode_index)

def get_index(sequence, order):
    "Returns the index of a permutated sequence given original order"
    pass

def get_lehmer_code(permutated_sequence, original_sequence):
    "Returns the Lehmer Code of a permutated sequence given original order"

    if original_sequence == []:
        original_sequence = [i for i in range(len(permutated_sequence))]

    dictionary = {letter:i for i, letter in enumerate(original_sequence)}
    indexed_sequence = [dictionary[symbol] for symbol in permutated_sequence]
    lehmer_code = [0]*len(permutated_sequence)
    binary = 0b0

    for i in range(len(permutated_sequence)):
        binary = (binary ^ (1 << (indexed_sequence[i])))
        temp_binary = binary >> (indexed_sequence[i] + 1)
        lehmer_code[indexed_sequence[i]] = temp_binary.bit_count()

    return lehmer_code

if __name__ == "__main__":
    print(get_lehmer_code("0132","0123"))
    print(Permutate_with_lehmer("0123", [0,0,1,0]))
    """
    #print("hola")
    for i in range(10):
        print(dec_to_fact(i))
        print(encode(string,i))
        print(decode(encode(string,i),i))
    print(Permutate_with_lehmer("012", [1,1,0]))
    """