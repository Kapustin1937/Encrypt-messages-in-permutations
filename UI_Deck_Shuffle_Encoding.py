"""
Run This!
This is the main UI for the Card Shuffle encoder

"""


import tkinter
from tkinter import ttk
from deck_encoder import Deck
from math import log2, factorial
import sv_ttk # https://github.com/rdbende/Sun-Valley-ttk-theme

global canvas_cards

def update_limit_info(event = ""):
    """
    Updated the label with the letter usage information
    """
    update_card_order()
    message = text_message.get("1.0",'end-1c')

    current_info = len(message)

    label_current_info.config(text=str(32-current_info)+ " letters remaining")
    if current_info > 32:
        label_current_info.config(foreground= "#f00")
    else:
        label_current_info.config(foreground= "#fff")

def update_card_order(event = ""):
    """
    Updates card order image and the encoded text"
    """

    global image_list

    image_list = []
    canvas_cards.delete()

    message = text_message.get("1.0",'end-1c')
    try:
        deck.encode_in_shuffle(message)

        card_order = deck.get_deck()

        image_card = tkinter.PhotoImage(file=f'cards/AC.svg.png')
        width, height = 60, 90

        for i in range(len(card_order)):
            print(card_order[i])
            image_card = tkinter.PhotoImage(file = f'cards/{card_order[i]}.svg.png')
            image_list.append(image_card)
            canvas_cards.create_image((i%13)*width+5,(i//13)*height+5, image=image_card, anchor="nw")

        text_cards.delete("1.0", 'end-1c')   
        for i in range(3,-1,-1):
            text_cards.insert("1.0", " ".join(card_order[(13*i):(13*(i+1))]) + "\n")
        update_decoder_text()
    except:
        print("uy")
        canvas_cards.create_text(30,30,text="The message is too long!",font=("Consola", 40),fill="#fff", anchor="nw")
    
def update_decoder_text(event = ""):
    """
    Updates the decoder text
    """
    encoded_message = text_cards.get("1.0",'end-1c')
    text_decode.delete("1.0",'end-1c')

    try:
        decoded_message = deck.decode_from_shuffle([card.upper() for card in encoded_message.split()])
        text_decode.insert("1.0", decoded_message)
    except:
        text_decode.insert("1.0", "Inserted deck order is incomplete or invalid")

root = tkinter.Tk()
root.geometry("900x600")
root.title("Deck Shuffle Encoder")
deck = Deck()

# --- elements --- #

text_message = tkinter.Text(height=1, width = 50, font="Consola", padx=10, pady=5)
label_message = ttk.Label(text="Introduce message:")
text_message.bind("<KeyRelease>", lambda event: update_limit_info())
text_message.bind("<FocusOut>", lambda event: update_limit_info())
label_current_info = ttk.Label()

canvas_cards = tkinter.Canvas(width=785,height=365)

label_cards = ttk.Label(text="Card order: ")
text_cards = tkinter.Text(height=4, width = 40, font="Consola", padx=10, pady=5)
text_cards.bind("<KeyRelease>", lambda event: update_decoder_text())
label_card_names = ttk.Label(text=
                            "Introduce cards separated \n" \
                            "by spaces or newlines \n" \
                            "Suits: ♠ - S, ♥ - H, ♣ - C, ♦ - D \n" \
                            "Values: 2-10 as is, then J, Q, K, A \n"\
                            "Order: ->left to right->")

label_decode = ttk.Label(text="Decoded message: ")
text_decode = tkinter.Text(height=1, width = 50, font="Consola", padx=10, pady=5)

# --- positioning --- #

text_message.grid(row=1, column=1,pady=5, padx=10)
label_message.grid(row=1, column=0,pady=5, padx=10)

label_current_info.grid(row=1, column=2,pady=10, padx=10, columnspan=2)
canvas_cards.grid(row=2, column = 0,pady = 20, columnspan=3)

label_cards.grid(row=3, column=0,pady=5, padx=10)
text_cards.grid(row=3, column=1,pady=5)
label_card_names.grid(row=3,column=2)

label_decode.grid(row=4, column=0,pady=5, padx=10)
text_decode.grid(row=4, column=1,pady=5, padx=20)

# --- mainloop --- #

sv_ttk.set_theme("dark")
update_limit_info()
root.mainloop()