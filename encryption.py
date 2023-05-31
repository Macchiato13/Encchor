import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext
import tkinter.constants as constants
import tkinter.font as font
import pyperclip

encryption_rules = {
    'A': '1ca',
    'B': '1lb',
    'C': '1ac',
    'D': '1kd',
    'E': '1de',
    'F': '1cf',
    'G': '1ug',
    'H': '2ch',
    'I': '2ci',
    'J': '2ua',
    'K': '2ea-2',
    'L': '2ub',
    'M': '2oc-2',
    'N': '2ec-2',
    'O': '3af-1',
    'P': '3kg',
    'Q': '3kh',
    'R': '3ui',
    'S': '3ba',
    'T': '3vx',
    'U': '3vb',
    'V': '4vb',
    'W': '4pc-2',
    'X': '4pd-2',
    'Y': '4fe-2',
    'Z': '4ff-2',
    'a': '10ca',
    'b': '10lb',
    'c': '10ac',
    'd': '10kd',
    'e': '10de',
    'f': '10cf',
    'g': '12ug',
    'h': '22ch',
    'i': '22ci',
    'j': '22ua',
    'k': '22ea-2',
    'l': '22ub',
    'm': '23oc-2',
    'n': '23ec-2',
    'o': '33af-1',
    'p': '33kg',
    'q': '33kh',
    'r': '33ui',
    's': '34ba',
    't': '34vx',
    'u': '34vb',
    'v': '44vb',
    'w': '44pc-2',
    'x': '44pd-2',
    'y': '45fe-2',
    'z': '45ff-2',
    '.': '45aa',
    ',': '45bb',
    '1': 'n01',
    '2': 'n02',
    '3': 'n03',
    '4': 'n04',
    '5': 'n05',
    '6': 'n06',
    '7': 'n07',
    '8': 'n08',
    '9': 'n09',
    # More rules to be added
}

def encrypt_text(plaintext):
    encrypted_text = ''
    for char in plaintext:
        if char.upper() in encryption_rules:
            encrypted_text += encryption_rules[char.upper()]
        elif char == ' ':
            encrypted_text += '45cc'
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_button_click():
    plaintext = input_text.get("1.0", "end-1c")
    encrypted_text = encrypt_text(plaintext)
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)
    output_text.configure(state="disabled")

def copy_button_click():
    encrypted_text = output_text.get("1.0", "end-1c")
    pyperclip.copy(encrypted_text)
    messagebox.showinfo("Copy", "Text copied to clipboard!")

# Create the main window
window = tk.Tk()
window.title("Text Encryption")
window.geometry("400x300")

# Input box
input_label = tk.Label(window, text="Enter Text:")
input_label.pack()
input_text = scrolledtext.ScrolledText(window, height=5)
input_text.pack()

# Encrypt button
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_button_click)
encrypt_button.pack()

# Output/Result box
output_label = tk.Label(window, text="Encrypted Text:")
output_label.pack()
output_text = scrolledtext.ScrolledText(window, height=5, state="disabled")
output_text.pack()

# Copy button
copy_button = ttk.Button(window, text="Copy", command=copy_button_click)
copy_button.pack()

# Start the GUI event loop
window.mainloop()