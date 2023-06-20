import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Function to open a file and insert its contents into the text editor
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text_editor.delete('1.0', tk.END)
            text_editor.insert(tk.END, file.read())

# Function to save the text editor content to a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_editor.get('1.0', tk.END))

# Function to clear the text editor content
def clear_text():
    text_editor.delete('1.0', tk.END)

# Function to display information about the text editor
def about():
    messagebox.showinfo("About", "A Simple Text Editor created using Python and Tkinter.")

# Create the main application window
root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")

# Create the text editor widget
text_editor = tk.Text(root, height=30, width=80, font=("Helvetica", 14))
text_editor.pack()

# Create the menu bar
menu_bar = tk.Menu(root)

# Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create the Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Clear", command=clear_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Create the Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure the root window to use the menu bar
root.config(menu=menu_bar)

# Start the application event loop
root.mainloop()
