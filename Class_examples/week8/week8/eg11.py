# Using a canvas and events

import tkinter as tk 

class App(object):
    
    def __init__(self, master):   
        master.title("Example 11")
        master.geometry("300x200")
        self._canvas = tk.Canvas(master, bg='purple')
        self._canvas.pack()
        self._canvas.bind("<Button-1>", self.press1)
        self._canvas.bind("<B1-Motion>", self.motion1)
        self._canvas.bind("<ButtonRelease-1>", self.release1)
        self._canvas.bind_all("<Key>", self.key_press)

    def press1(self, e):
        print("press", e.x, e.y)

    def motion1(self, e):
        print("motion", e.x, e.y)

    def release1(self, e):
        print("release", e.x, e.y)

    def key_press(self, e):
        print(e.char, e.keysym, e.keycode)


root = tk.Tk()
app = App(root)
root.mainloop()
