import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Combobox, Button
import threading
import converter
import os
'''
Author:Elmer Dema
Solution to: Programming 2 by Prof. Dr. Markus Mayer
https://www.geeksforgeeks.org/converting-image-ascii-image-python/
https://linuxhint.com/tkinter-scrollbar/
https://www.pythontutorial.net/python-concurrency/python-threading/

P.S. Euclidean.txt uses the euclidean distance to calculate the closest character
 to the pixel rather than comparing them to the grayscale values (bonus task)
Only ascii_euclidean.txt is displayed in the text field, 
even though it does not display it fully,
the other ascii.txt can be found in the folder
'''
class Editor():
    def __init__(self, path, root):
        self.path = path
        self.root = root
        self.selected_option = None  # Instance variable to store selected combobox value

    def header(self):
        label = tk.Label(self.root, text="ASCII Art Editor", font=("Times New Roman", 15))
        label.place(x=10, y=10)

        self.path_label = tk.Entry(self.root, width=50)
        self.path_label.place(x=160, y=15)

        select_label = tk.Button(self.root, text="Select Image", bg="lightgray", command=self.select_image)
        select_label.place(x=500, y=10)

        save_label = tk.Button(self.root, text="Save File", bg="lightgray")
        save_label.place(x=580, y=10)

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png")])
        if file_path:
            self.path_label.delete(0, tk.END)
            self.path_label.insert(tk.END, file_path)

    def body(self):
        self.text_field = tk.Text(self.root,wrap=tk.WORD, bg="lightgray", width=79, height=20)
        self.text_field.place(x=10, y=50)
        # Add horizontal scrollbar
        horizontal_scrollbar = tk.Scrollbar(self.root, orient=tk.HORIZONTAL)
        horizontal_scrollbar.pack(fill=tk.X, side=tk.BOTTOM)
        self.text_field.config(xscrollcommand=horizontal_scrollbar.set)
        horizontal_scrollbar.config(command=self.text_field.xview)

    # Add vertical scrollbar
        vertical_scrollbar = tk.Scrollbar(self.root)
        vertical_scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
        self.text_field.config(yscrollcommand=vertical_scrollbar.set)
        vertical_scrollbar.config(command=self.text_field.yview)
        zoom_frame = tk.Frame(self.root)
        zoom_frame.pack(side=tk.TOP)
    
    
    def insert_text_from_file(self, file_path):
        with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as file:
            content = file.read()
            self.text_field.delete(1.0, tk.END)
            self.text_field.insert(tk.END, content)

    def footer(self):
        self.font_size_entry = tk.Entry(self.root)
        self.font_size_entry.place(x=10, y=400, width=25)
        self.font_size_entry.insert(tk.END, "10")

        self.char_width_entry = tk.Entry(self.root)
        self.char_width_entry.place(x=60, y=400, width=25)
        self.char_width_entry.insert(tk.END, "10")

        self.char_height_entry = tk.Entry(self.root)
        self.char_height_entry.place(x=110, y=400, width=25)
        self.char_height_entry.insert(tk.END, "10")
        self.characters_entry = tk.Entry(self.root)
        self.characters_entry.place(x=160, y=400, width=75)
        self.characters_entry.insert(tk.END, "@%#*+=-:. ")

        options = ["R", "G", "B"]
        select_label = Combobox(self.root, values=options)
        select_label.place(x=250, y=400, width=50)
        select_label.bind("<<ComboboxSelected>>", self.update_selected_option)

        generate_button = tk.Button(self.root, text="Generate", bg="lightgray", command=self.generate)
        generate_button.place(x=580, y=395)

        font_size_label = tk.Label(self.root, text="Size", font=("Times New Roman", 10))
        font_size_label.place(x=8, y=420)

        font_width_label = tk.Label(self.root, text="Width", font=("Times New Roman", 10))
        font_width_label.place(x=56, y=420)

        font_height_label = tk.Label(self.root, text="Height", font=("Times New Roman", 10))
        font_height_label.place(x=106, y=420)

        characters_label = tk.Label(self.root, text="Characters", font=("Times New Roman", 10))
        characters_label.place(x=160, y=420)

    def update_selected_option(self, event):
        combobox = event.widget
        self.selected_option = combobox.get()

    def generate(self):
        generator = converter.Ascii(
            self.path_label.get(),
            self.characters_entry.get(),
            int(self.char_width_entry.get()),
            int(self.char_height_entry.get()),
            255,
            int(self.font_size_entry.get()),
            0,
            self.selected_option,  # Use the stored selected option here
        ) 
        conversion_thread = threading.Thread(target=self.perform_conversion, args=(generator,))
        conversion_thread.start()

        '''
        generator.grayscale()
        generator.create_fontimage()
        generator.create_ascii_simple()
        generator.create_ascii_euclidean()
        file_path = "ascii_euclidean.txt"
        self.text_field.delete(1.0, tk.END)
        self.insert_text_from_file(file_path)
        '''
    def perform_conversion(self, generator):
        # Run the ASCII conversion methods
        generator.grayscale()
        generator.create_fontimage()
        generator.create_ascii_simple()
        generator.create_ascii_euclidean() 

        # Update the file_path to the new ASCII file
        file_path = "ascii_euclidean.txt"

        # Clear the text field and insert the new content
        self.root.after(0, self.insert_text_from_file, file_path)    


root = tk.Tk()
root.title("ASCII Art Editor")
root.geometry("650x450")
test = Editor("test.jpg", root)


test.header()
test.body()
test.footer()


root.mainloop()
