# tkinter is a standard python gui library
from tkinter import *
from tkinter import filedialog

# saves the user chosen folder file path to a variable
# this allows the file path to be used throughout the program
def get_file_path():
    global file_path
    # Open and return file path
    file_path= filedialog.askdirectory()
    Label(window, text = "File path: " + file_path).pack()

window = Tk()

# window and button attributes
window.geometry("450x300")
# Creating a button to search the file
b1 = Button(window, text = "Open File", command = get_file_path).pack()
b2= Button(window, text = "Run", command= window.quit).pack()
window.mainloop()
print(file_path)