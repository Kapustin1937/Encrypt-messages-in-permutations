"""
Contains functions to convert into and from the factoradic number system
"""

def dec_to_fact(number: int):
    """
    Takes a number in decimal base and returns a list with its factoradic representation
    """
    factoradic = []
    i = 1
    while number != 0:
        factoradic.append(number % i)
        number //= i
        i += 1
    factoradic.reverse()
    return factoradic

def fact_to_dec(factoradic: list):
    """
    Takes a list that represents a factoradic representation and return the corresponding number in decimal base
    """
    number = 0
    n = 1
    factorial = 1
    for i in range(len(factoradic)-2, -1, -1):
        number += factoradic[i] * factorial
        n += 1
        factorial *= n
    return number

if __name__ == "__main__":
    number = int(input("Insert number: "))
    factoradic = dec_to_fact(number)
    print(factoradic)
    number1 = fact_to_dec(factoradic)
    print(number1)
    print(bin(number1))