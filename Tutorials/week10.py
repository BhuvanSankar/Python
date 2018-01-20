import tkinter as tk


class SettingsFrame(tk.Frame):
    """A frame which allows users to change settings of the application

    Settings to change are: whether or not a line preview is shown.
    """
    def __init__(self, parent):
        """Initialise the widget, with its subwidgets

        Constructor: SettingsFrame(tk.Widget)
        """
        super().__init__(parent)

        self._pos_lbl = tk.Label(self, text="Current Position:")
        self._pos_lbl.pack(side=tk.LEFT)

        self._preview_btn = tk.Button(self, text="Preview On", bg="green",
                                   command=self._toggle_preview)
        self._preview_btn.pack(side=tk.RIGHT)

    def _toggle_preview(self):
        """Toggle the line preview on/off.

        SettingsFrame._toggle_preview() -> None

        """
        pass  # Replace this with your solution

    def is_preview_on(self):
        """Return True if the Preview setting is on, otherwise False.

        SettingsFrame.is_preview_on() -> bool

        """
        pass  # Replace this with your solution

    def set_position(self, x, y):
        """Change the 'Current Position' label to show new coordinates.

        SettingsFrame.set_position(int, int) -> None

        """
        pass  # Replace this with your solution


class DrawingApp(object):
    """An application for drawing lines.
    """
    def __init__(self, master):
        """Initialise a DrawingApp object, including widget layout.

        Constructor: Drawing(Tk.BaseWindow)
        """
        self._master = master
        master.title("Drawing Application")
        master.minsize(500, 375)

        self._canvas = tk.Canvas(master, bd=2, relief=tk.SUNKEN)
        self._canvas.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self._canvas.bind('<Motion>', self.evt_motion)
        # More Canvas bindings can be added here

        self._settings = SettingsFrame(master)
        self._settings.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        menubar = tk.Menu(master)
        master.config(menu=menubar)

        filemenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Exit", command=self.exit)

        editmenu = tk.Menu(menubar)
        menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Clear All Lines", command=self.clear)

    def evt_motion(self, e):
        """Event handler for Mouse movement on the Canvas

        DrawingApp.evt_motion(Tk.Event) -> None

        """
        print(e.x, e.y)  # Replace this with your solution

    def exit(self):
        """Close the application.

        DrawingApp.exit() -> None

        """
        self._master.destroy()

    def clear(self):
        """Delete all lines from the application.

        DrawingApp.clear() -> None

        """
        self._canvas.delete(tk.ALL)

if __name__ == '__main__':
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
