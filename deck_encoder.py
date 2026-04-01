"""
Includes functions for encoding a string in the order of a deck of cards
"""
from string_encoder import *

class Deck:
    cards = []

    def __init__(self):
        """
        Starts the deck with 52 cards in Balatro order.
        """
       
        self.cards = self.get_orig_order()

    def get_deck(self):
        """
        Returns the cards in the order of the Deck object
        """
        return self.cards
    
    def get_orig_order(self):
        """
        Returns a list containing all the cards in unshuffled order
        """
        # Lmao I LOVE list comprehension no one is deconding this
        return [item_ for list_ in [[str(number) + suit for number in list(range(2,11))+["J","Q","K","A"]]for suit in "SHCD"] for item_ in list_] #♠♥♣♦

    def print(self):
        """
        Prints out the list of cards inside the deck
        """
        print(f"current deck: {self.cards}\n")

    def encode_in_shuffle(self, message):
        """
        Encodes message inplace in the shuffle of the deck. \\
        Returns error if message contains \\
        more than 225 bits in ascii (28 characters).
        """

        try:
            self.cards = encode_in_permutation(self.get_orig_order(), message)
        except:
            raise ValueError("Message too long")

    def decode_from_shuffle(self, shuffle = []):
        """
        Decodes message from shuffle of deck. By default uses the deck its called on. \\
        Can receive a list of cards as an argument
        """
        if shuffle == []:
            shuffle = self.cards

        return decode_from_permutation(shuffle, self.get_orig_order())


if __name__ == "__main__":
    deck = Deck()
    deck.print()
    deck.encode_in_shuffle("Wow this is absolutely amazing")
    deck.print()
    print(deck.decode_from_shuffle())