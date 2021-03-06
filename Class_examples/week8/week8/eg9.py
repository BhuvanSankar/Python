# Using fill

import tkinter as tk 

class App(object):
    
    def __init__(self, master):   
        master.title("Example 9")
        master.geometry("300x200")
        self._label = tk.Label(master, text="A label", bg="green")
        # pack it
        self._label.pack() 
        # create a frame - a container whose parent is master
        self._frame = tk.Frame(master, bg = 'yellow')
        # don't forget to pack the frame
        # try fill=tk.X and fill=tk.Y and removing the expand
        self._frame.pack(fill=tk.BOTH, expand=1)
        # put two buttons in frame - frame is their parent
        self._button1 = tk.Button(self._frame, text="Press Me",fg="green",
                                  command=self.press1)
        # pack it
        self._button1.pack(side=tk.LEFT, expand=1)
        # Another button
        self._button2 = tk.Button(self._frame, text="No - Press Me",fg="green",
                                  command=self.press2)
        # pack it
        self._button2.pack(side=tk.LEFT, expand=1)
        
        
        self._state = False

    def redraw(self):
        if self._state:
            self._label.config(bg="red")
        else:
            self._label.config(bg="green")
            
        
    def press1(self):
        self._state = True
        self.redraw()

    def press2(self):
        self._state = False
        self.redraw()


root = tk.Tk()
app = App(root)
root.mainloop()
