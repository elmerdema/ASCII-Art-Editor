'''
Write a graphical user interface (GUI) for a ASCII art editor.
ASCII art: https://en.wikipedia.org/wiki/ASCII_art
 The program converts an image to ASCII text.
 The input image is converted to grayscale.
A set of characters is provided as input.
These characters are rendered to little images. The width and
heights of these images can be specified, as well as the font
size for rendering.
For the input image, the dimensions of the character images
are used as step sizes in x and y direction. For each possible
position, a distance (e.g. euclidian) of the original image crop to
all the character images is computed. The character with the
lowest distance is selected for the final ASCII text.

The GUI parameters
The image path is taken from an entry. A file selection
dialogue is provided in addition, that can be accessed by a
button. The result of the dialogue is stored in the entry.
There are entries for the character image width, height and
font size, with proper labels as descriptions.
There is a button for selecting the grayscale conversion
method. Either the button itself changes with the selected
method, or there is a label showing the currently selected
method. Possibilities for grayscale conversion should be at least
the selection of one of the 3 channels of an RGB image.
An entry is present where the user can type in a character set
for the conversion.
All entries and buttons have meaningful default values, such
that a conversion of an image can be instantly tried out.

Main GUI elements
There is a Generate button (the name can be chosen by you),
which starts the conversion with the currently selected options.
There is a Save Text button (naming can be chosen by you),
with which the generated text can be saved to a .txt file. A
file selection dialogue opens when you press the button.
The generated ASCII test is displayed as the main element of the
GUI. When the text does not fit to the window size, scroll bars
appear (or are always present). You can use a fixed font size.

Furthermore: Threads
The conversion (i.e. character images generation and
comparison to the input image) is done in a thread.
 The thread is (at some point in time) joined with the main
thread again.
'''
import tkinter as tk
from tkinter import Text


class Editor():
    def __init__(self, path, root):
        self.path = path
        self.root = root

    def header(self):
        label=tk.Label(self.root, text="ASCII Art Editor", font=("Times New Roman", 15))
        label.place(x=10,y=10)

        path_label=tk.Entry(self.root, text="Path")
        path_label.place(x=200,y=15)

        select_label=tk.Button(self.root,text="Select Image", bg="lightgray")
        select_label.place(x=350,y=10)

        save_label=tk.Button(self.root,text="Save File", bg="lightgray")
        save_label.place(x=440,y=10)

    def body(self):
        text_field=Text(self.root, bg="lightgray",width=60, height=20)
        
        text_field.place(x=10,y=50)

    def footer(self):
        font_size_entry=tk.Entry(self.root)
        font_size_entry.place(x=10,y=400,width=25)

        char_width_entry=tk.Entry(self.root)
        char_width_entry.place(x=60,y=400,width=25)

        char_height_entry=tk.Entry(self.root)
        char_height_entry.place(x=110,y=400,width=25)

        char_height_entry=tk.Entry(self.root)
        char_height_entry.place(x=110,y=400,width=25)

        characters_entry=tk.Entry(self.root)
        characters_entry.place(x=160,y=400,width=75)

        generate_button=tk.Button(self.root,text="Generate", bg="lightgray")
        generate_button.place(x=440,y=395)

        font_size_label=tk.Label(self.root,text="Size", font=("Times New Roman", 10))
        font_size_label.place(x=8,y=420)

        font_width_label=tk.Label(self.root,text="Width", font=("Times New Roman", 10))
        font_width_label.place(x=56,y=420)

        font_height_label=tk.Label(self.root,text="Height", font=("Times New Roman", 10))
        font_height_label.place(x=106,y=420)

        characters_label=tk.Label(self.root,text="Characters", font=("Times New Roman", 10))
        characters_label.place(x=160,y=420)







root = tk.Tk()
root.title("ASCII Art Editor")
root.geometry("500x450")
test = Editor("test", root)

test.header()
test.body()
test.footer()

root.mainloop()