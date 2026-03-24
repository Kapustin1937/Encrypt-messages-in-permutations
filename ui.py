import tkinter
from tkinter import ttk
from string_encoder import encode_in_permutation, decode_from_permutation, factorial
from math import log2
import sv_ttk # https://github.com/rdbende/Sun-Valley-ttk-theme

def encode():
    "Encodes the text in the message box using the sequence box order and inserts it into the encoded box"
    text_encoded.delete("1.0", 'end-1c')
    try:
        sequence = text_sequence.get("1.0",'end-1c')
        message = text_message.get("1.0",'end-1c')

        encoded_message = "".join(encode_in_permutation(sequence, message))

        text_encoded.insert("1.0", encoded_message)

        if encoded_message == "":
            text_encoded.insert("1.0", "Encoded message is empty!")
    except ValueError:
        text_encoded.insert("1.0", "ERROR: sequence contains repeated elements")   
    except IndexError:
        text_encoded.insert("1.0", "ERROR: sequence not long enought for amount of information")
        
def decode():
    "Decodes the text in the encoded box using the sequence box order and inserts it into the decoded box"
    text_decoded.delete("1.0", 'end-1c')

    sequence = text_sequence.get("1.0",'end-1c')
    encoded = text_encoded.get("1.0",'end-1c')
    if sequence == "":
        text_decoded.insert("1.0", "Original sequence is not defined!")
        return
    elif encoded == "":
        text_decoded.insert("1.0", "Encoded message is not defined!")
        return
    try:
        decoded_message = "".join(decode_from_permutation(encoded, sequence))
    except:
        text_decoded.insert("1.0", "Original sequence does not correspond to the encrypted message!")

    text_decoded.insert("1.0", decoded_message)



def update_limit_info(event = ""):
    "Updated all 3 of the labels with the bit usage information"
    sequence = text_sequence.get("1.0",'end-1c')
    message = text_message.get("1.0",'end-1c')
    
    max_info = int(log2(factorial(len(sequence)+1)))
    current_info = len(message) * 8

    label_max_info.config(text=f"{max_info} bits total")
    label_current_info.config(text=f"{current_info} bits used")
    try:
        label_remaining_info.config(text=f"{max_info-current_info} bits available")
    except:
        label_remaining_info.config(text="-")
    return "hi"

root = tkinter.Tk()
root.geometry("900x400")
root.title("Permutation Encoder")

# --- elements --- #

label_intro = ttk.Label(text="IntraPermutation Encoder", font=("Helvetica",20, "bold"))

text_sequence = tkinter.Text(height=1, width = 50, font="Consola", padx=10, pady=5)
label_sequence = ttk.Label(text="Introduce sequence:")
text_sequence.bind("<KeyRelease>", lambda event: update_limit_info())
text_sequence.bind("<FocusOut>", lambda event: update_limit_info())
label_max_info = ttk.Label()

text_message = tkinter.Text(height=1, width = 50, font="Consola", padx=10, pady=5)
label_message = ttk.Label(text="Introduce message:")
text_message.bind("<KeyRelease>", lambda event: update_limit_info())
text_message.bind("<FocusOut>", lambda event: update_limit_info())
label_current_info = ttk.Label()

label_remaining_info = ttk.Label()

button_encode = ttk.Button(text="Encode", command=encode)

label_encoded = ttk.Label(text="Encoded message:")
text_encoded = tkinter.Text(height=1, width = 50, font="Consola", padx=10, pady=5)
text_encoded.insert("1.0", "Here will be the encoded message")


button_decode = ttk.Button(text="Decode", command=decode)

label_decoded = ttk.Label(text="Decoded message:")
text_decoded = tkinter.Text(height=1, width = 50, font="Consola", padx=10, pady=5)

label_intro.grid(row=0,column=0, columnspan=2,padx=20,pady=10)

# --- positioning --- #

text_sequence.grid(row=1, column=1,pady=20, padx=10)
label_sequence.grid(row=1, column=0,pady=20, padx=10)
label_max_info.grid(row=1, column=2,pady=20, padx=10)

label_remaining_info.grid(row=1, column=2, rowspan=2)

text_message.grid(row=2, column=1,pady=5, padx=10)
label_message.grid(row=2, column=0,pady=5, padx=10)
label_current_info.grid(row=2, column=2,pady=5, padx=10)


button_encode.grid(row=3, column=1, padx=10)

label_encoded.grid(row=4,column=0,pady=5, padx=10)
text_encoded.grid(row=4,column=1,pady=5, padx=10)

button_decode.grid(row=5, column=1, padx=10)

label_decoded.grid(row=6, column=0, pady=5, padx=10)
text_decoded.grid(row=6, column=1, pady=5, padx=10)

# This is where the magic happens # Lmao
sv_ttk.set_theme("dark")
update_limit_info()
root.mainloop()