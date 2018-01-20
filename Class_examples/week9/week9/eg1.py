# Using a text widget - with a file menu and filedialog

import tkinter as tk 
from tkinter import filedialog

class App(object):
    
    def __init__(self, master):   
        master.title("Example 10")
        self.master = master
        self._text = tk.Text(master)
        self._text.pack(expand=1, fill=tk.BOTH)
        # File menu
        menubar = tk.Menu(master)
        # tell master what it's menu is
        master.config(menu=menubar)
        filemenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        self.filename = None


    def new_file(self):
        self._text.delete("1.0", tk.END)
        self.filename = None
        self.master.title("New File")

    def save_file(self):
        if self.filename is None:
            filename = filedialog.asksaveasfilename()
            if filename:
                self.filename = filename
        if self.filename:
            self.master.title(self.filename)
            fd = open(self.filename, 'w')
            fd.write(self._text.get("1.0", tk.END))
            fd.close()
            

    def open_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.filename = filename
            self.master.title(self.filename)
            fd = open(filename, 'r')
            self._text.insert(tk.INSERT, fd.read())
            fd.close()
                
root = tk.Tk()
app = App(root)
root.mainloop()

