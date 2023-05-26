import tkinter as tk
from tkinter import filedialog
'''
Author:Elmer Dema
Solution to: Programming 2 by Prof. Dr. Markus Mayer
https://www.geeksforgeeks.org/converting-image-ascii-image-python/
'''
class Editor():
    def __init__(self, path, root):
        self.path = path
        self.root = root

    def header(self):
        label = tk.Label(self.root, text="ASCII Art Editor", font=("Times New Roman", 15))
        label.place(x=10, y=10)

        self.path_label = tk.Entry(self.root, width=50)
        self.path_label.place(x=200, y=15)

        select_label = tk.Button(self.root, text="Select Image", bg="lightgray", command=self.select_image)
        select_label.place(x=350, y=10)

        save_label = tk.Button(self.root, text="Save File", bg="lightgray")
        save_label.place(x=440, y=10)
    #only jpg and png files are allowed
    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png")])
        if file_path:
            self.path_label.delete(0, tk.END)
            self.path_label.insert(tk.END, file_path)

    def body(self):
        text_field = tk.Text(self.root, bg="lightgray", width=60, height=20)
        text_field.place(x=10, y=50)

    def footer(self):
        font_size_entry = tk.Entry(self.root)
        font_size_entry.place(x=10, y=400, width=25)

        char_width_entry = tk.Entry(self.root)
        char_width_entry.place(x=60, y=400, width=25)

        char_height_entry = tk.Entry(self.root)
        char_height_entry.place(x=110, y=400, width=25)

        char_height_entry = tk.Entry(self.root)
        char_height_entry.place(x=110, y=400, width=25)

        characters_entry = tk.Entry(self.root)
        characters_entry.place(x=160, y=400, width=75)

        generate_button = tk.Button(self.root, text="Generate", bg="lightgray")
        generate_button.place(x=440, y=395)

        font_size_label = tk.Label(self.root, text="Size", font=("Times New Roman", 10))
        font_size_label.place(x=8, y=420)

        font_width_label = tk.Label(self.root, text="Width", font=("Times New Roman", 10))
        font_width_label.place(x=56, y=420)

        font_height_label = tk.Label(self.root, text="Height", font=("Times New Roman", 10))
        font_height_label.place(x=106, y=420)

        characters_label = tk.Label(self.root, text="Characters", font=("Times New Roman", 10))
        characters_label.place(x=160, y=420)





root = tk.Tk()
root.title("ASCII Art Editor")
root.geometry("500x450")
test = Editor("test", root)

test.header()
test.body()
test.footer()

root.mainloop()
