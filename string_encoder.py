from factoradic_converter import *
from permutator import *

def string_to_num(s):
    "Represents a string as a number converting every character to ascii"
    return sum([ord(s[i])<<(i*7) for i in range(len(s))])

def num_to_string(num):
    "Represents a number as a string converting sets of 7 bits to ascii characters"
    string = ""
    while num != 0:
        string += chr(int(num & 0b1111111))
        num = num >> 7
    return string

def encode_in_permutation(sequence, message):
    "Encodes a secret message in a permutation of sequence of DISTINCT elements"
    
    # Check for repeated symbols
    if len(set(sequence)) != len(sequence):
        print("ERROR: sequence contains repeated elements")
        raise(ValueError)
    
    # Transorm the string into a number
    index = string_to_num(message)

    # Check if the number is representable with the amount of elements in the sequence
    if index > factorial(len(sequence)+1):
        print("ERROR: sequence not long enought for amount of information")
        raise(IndexError)
    
    permutated_sequence = encode(sequence, index)
    return permutated_sequence
    
def decode_from_permutation(permutated_sequence, original_sequence):
    "Decodes secret message from the permutation of a sequence of DISTINCT elements given original order"

    # Calculate the lehmer code of the permutates sequence
    try:
        lehmer_code = get_lehmer_code(permutated_sequence, original_sequence)
    except:
        raise(ValueError)

    # Get the index of the permutation from the lehmer code and convert it into a string
    index = fact_to_dec(lehmer_code)
    message = num_to_string(index)

    return message

def test2():
    s = "qwertyuiop"
    message = input("introduce secret message: ")
    encoded = "".join(encode_in_permutation("qwertyuiop", "hii"))
    print(f"permutated sequence: {encoded}")
    decoded = "".join(decode_from_permutation(encoded, s))
    print(f"decoded: {decoded}")
    print(Permutate_with_lehmer("0123",get_lehmer_code("0132","0123")))

def test1():
    s = "Hello gays"
    print(s)
    num = string_to_num(s)
    print(num)
    fact = dec_to_fact(num)
    print(fact)

    llista = [chr(int(ord("a")+i)) for i in range(len(fact))]

    print(llista)
    permutat1 = Permutate_with_lehmer(llista, fact)
    #permutat2 = encode(llista, num)
    print(permutat1)
    #print(permutat2)
    decoded = get_lehmer_code(permutat1, [chr(ord("a")+i) for i in range(len(fact))])
    print(decoded)
    decoded_num = fact_to_dec(decoded)
    print(decoded_num)
    decoded_string = num_to_string(decoded_num)
    print(decoded_string)

if __name__ == "__main__":
    test2()