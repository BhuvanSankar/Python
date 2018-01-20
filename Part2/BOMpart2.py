
###################################################################
#
#   CSSE1001/7030 - Assignment 2
#
#   Student Number:
#
#   Student Name:
#
###################################################################

#####################################
# Support given below - DO NOT CHANGE
#####################################

from assign2_support import *

#####################################
# End of support 
#####################################

# Add your code here

class TemperatureData(object):
    """
    Model for temperature data from multiple stations.
    """
    def __init__(self):
        """
        Constructor
        """

        self._data = {}
        self._station_names = []
        self._station_toggles = []
        self._min_year = None
        self._max_year = None
        self._min_temp = None
        self._max_temp = None

    def load_data(self, filename):
        """
        Loads in data from the given filename (of the form StationName.txt).
        Returns the name of the station loaded, or None if that station has
        already been loaded.

        Precondition: filename has not already been loaded into this
            TemperatureData.

        load_data(self, str) -> str
        """

        # load the station
        station = Station(filename)

        # Don't load a station that has already been loaded
        name = station.get_name()
        if name in self._station_names:
            return

        self._data[name] = station

        # add name/toggle to appropriate lists
        self._station_names.append(name)
        self._station_toggles.append(True)

        # regenerate ranges
        first_station = self._data[self._station_names[0]]
        self._min_temp, self._max_temp = first_station.get_temp_range()
        self._min_year, self._max_year = first_station.get_year_range()

        for station in self._data.values():
            min_year, max_year = station.get_year_range()
            min_temp, max_temp = station.get_temp_range()
            
            self._min_year = min(self._min_year, min_year)
            self._max_year = max(self._max_year, max_year)
            
            self._min_temp = min(self._min_temp, min_temp)
            self._max_temp = max(self._max_temp, max_temp)

        return name

    def get_data(self, name = None):
        """
        Returns the dictionary of station data.

        get_data(self) -> dict(str:Station)
        """

        return self._data

    def toggle_selected(self, i):
        """
        Toggles the flag for displaying the station at index i.

        Precondition: i is a non-negative integer that is less than the number
            of loaded stations
            i.e. 0 <= i < len(get_stations())

        toggle_selected(self, bool) -> None
        """

        self._station_toggles[i] = not self._station_toggles[i]

    def is_selected(self, i):
        """
        Returns true iff the station at index i is currently visible.

        Precondition: i is a non-negative integer that is less than the number
            of loaded stations
            i.e. 0 <= i < len(get_stations())

        is_selected(self, int) -> bool
        """

        return self._station_toggles[i]

    def get_stations(self):
        """
        Returns the list of loaded station names in the order they were loaded.

        get_stations(self) -> list(str)
        """

        return self._station_names

    def get_ranges(self):
        """
        Returns a 4-tuple of the form (min_year, max_year, min_temp, max_temp).
        This information is used to translate between data values and canvas
        coordinates.

        Precondition: At least one station has been loaded.
            i.e. len(get_stations()) > 0

        get_stations(self) -> (int, int, float, float)
        """

        return (self._min_year, self._max_year, self._min_temp, self._max_temp)


class Plotter(tk.Canvas):
    """
    Plots station data in a coloured line graph.
    """

    def __init__(self, master, temperature_data, colours,
            year_selected = (lambda year: None), bg = "white"):
        """
        Constructor
        """

        super().__init__(bg = bg)

        self._temperature_data = temperature_data
        self._colours = colours
        self._translator = None

        self._width = 1
        self._height = 1

        self._line_year = None
        self._line = None

        self._year_selected = year_selected

        # Bind GUI events
        self.bind("<Configure>", self._resize)
        self.bind("<Button-1>", self._click_or_drag)
        self.bind("<B1-Motion>", self._click_or_drag)

        # CSSE7030 task
        self._start_year = None
        self._end_year = None
        self.bind_all("<Key>", self._keypress)

    def _keypress(self, ev):
        # CSSE7030 task
        """
        Handles keypress event on this plotter.

        _keypress(self, ev) -> None
        """
        if self._line_year is None:
            return

        if self._start_year is not None and self._end_year is None:
            self._end_year = self._line_year
            if self._start_year > self._end_year:
                self._start_year, self._end_year = \
                        self._end_year, self._start_year
        else:
            self._start_year = self._line_year
            self._end_year = None

        self.redraw()

    def _click_or_drag(self, ev):
        """
        Handles click/drag event on the plotter.

        _click_or_drag(self, tk.Event) -> None
        """
        if not self._translator:
            return

        if not(0 <= ev.x < self._width):
            self._line_year = None
        else:
            self._line_year = self._translator.get_year(ev.x)

        self._draw_line()

    def _draw_line(self):
        """
        Draws the vertical line on a given plot year.
        """

        self.delete(self._line)

        if not self._line_year:
            self._line = None
        else:
            x, _ = self._translator.temperature_coords(self._line_year, 0)
            self._line = self.create_line([x, 0, x, self._height])

        self._year_selected(self._line_year)

    def _resize(self, ev):
        """
        Handles resizing of this widget.

        _resize(self, tk.Event) -> None
        """

        self._width = ev.width
        self._height = ev.height

        if self._translator is not None:
            self._translator.resize(ev.width, ev.height)

        self.redraw()

    def refresh(self):
        """
        Refreshes the station plot(s) and updates the range of years/temps to
        match the data.
        """

        min_year, max_year, min_temp, max_temp = \
                self._temperature_data.get_ranges()
        self._translator = CoordinateTranslator(self._width, self._height,
                min_year, max_year, min_temp, max_temp)

        self.redraw()

    def redraw(self):
        """
        Redraws the station plot(s).

        redraw(self) -> None
        """

        self.delete(tk.ALL)

        data = self._temperature_data.get_data()

        for i, name in enumerate(self._temperature_data.get_stations()):
            if not self._temperature_data.is_selected(i):
                continue

            station = data[name]
            coords = []
            for year, temp in station.get_data_points():
                coords.append(self._translator.temperature_coords(year, temp))

            colour = self._colours[i % len(self._colours)]
            self.create_line(coords, fill = colour)

            # CSSE7030 task
            if self._start_year is not None and self._end_year is not None:
                # get coords in range
                coords = []
                for year, temp in station.get_data_points():
                    if self._start_year <= year <= self._end_year:
                        coord = self._translator.temperature_coords(year, temp)
                        coords.append(coords)

                fit = best_fit(coords)
                self.create_line(fit, fill = colour)

        self._draw_line()


class SelectionFrame(tk.Frame):
    """
    Displays the visibility toggle for each station.
    """

    def __init__(self, master, temperature_data, colours, toggle = None,
            **kwargs):
        """
        Constructor
        """

        super().__init__(master, **kwargs)

        self._temperature_data = temperature_data

        self._toggle = toggle or (lambda i, selected: None)

        self._label = tk.Label(self, text = "Station Selection: ")
        self._label.pack(side = tk.LEFT)

    def add_toggle(self, label, colour = None, command = None,
                selected = True):
        c = tk.Checkbutton(self, text = label, command = command, fg = colour)
        if selected:
            c.select()
        c.pack(side = tk.LEFT)


class DataFrame(tk.Frame):
    """
    Displays the temperatures for visible stations.
    """

    def __init__(self, master, temperature_data, colours, **kwargs):
        """
        Constructor
        """

        super().__init__(master, **kwargs)

        self._temperature_data = temperature_data

        self._colours = colours

        self._label = tk.Label(self, text = "")
        self._label.pack(side = tk.LEFT)

        self._labels = []

        self._year = None

    def set_year(self, year):
        """
        Sets the year to be used.

        set_year(self, int) -> None
        """

        self._year = year
        self.refresh()

    def add_label(self, label, colour = None):
        """
        Adds a new label to this data frame.

        add_label(self, str, str) -> None
        """

        i = len(self._labels)
        label = tk.Label(self, text = "", fg = colour)
        label.pack(side = tk.LEFT, padx = (10, 0))
        self._labels.append(label)

    def refresh(self):
        """
        Refreshes the labels in the data frame.

        refresh(self) -> None
        """

        if self._year is None:
            self._label.config(text = "")

        text = "Data for: {}".format(self._year)

        self._label.config(text = text if self._year is not None else "")

        data = self._temperature_data.get_data()
        for i, name in enumerate(self._temperature_data.get_stations()):
            label = self._labels[i]

            station = data[name]

            temp = station.get_temp(self._year)
            if not self._temperature_data.is_selected(i):
                temp = None
            label.config(text = temp or "")


class TemperaturePlotApp(object):
    def __init__(self, master):
        """
        Constructor
        """

        master.title("Max Temperature Plotter")

        # Build GUI layout
        self._data = TemperatureData()

        self._plotter = Plotter(master, self._data, COLOURS,
                year_selected = self.year_selected)
        self._data_frame = DataFrame(master, self._data, COLOURS)
        self._selection_frame = SelectionFrame(master, self._data, COLOURS,
                toggle = self.toggle)

        self._plotter.pack(expand = True, fill = tk.BOTH, side = tk.TOP)
        self._data_frame.pack(side = tk.TOP, fill = tk.X)
        self._selection_frame.pack(side = tk.TOP, fill = tk.X)

        # Build Menu
        menubar = tk.Menu(master)
        master.config(menu=menubar)

        filemenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open", command=self.open_file)

    def year_selected(self, year):
        """
        Handles the a year being selected by the user on the plotter.

        If year is None, then this is treated as deselecting the year.

        year_selected(int) -> None
        """

        self._data_frame.set_year(year)

    def toggle(self, i):
        """
        Handles a station being toggled in the SelectionFrame

        toggle(self, int) -> None
        """

        self._data.toggle_selected(i)
        self._data_frame.refresh()
        self._plotter.refresh()

    def add_station(self, filename):
        """
        Adds a new station.

        add_station(self, str) -> None
        """

        if not filename:
            return

        if not filename.endswith('.txt'):
            # Improper file extension
            messagebox.showerror(
                title="Error Opening File",
                message="The file {} does not have the correct extension." \
                    .format(filename))
            return

        try:
            name = self._data.load_data(filename)
        except:
            messagebox.showerror(
                title="Error Opening File",
                message="The file {} is unreadable or contains bad data." \
                    .format(filename))

        if name is not None:
            i = len(self._data.get_stations()) - 1
            self._selection_frame.add_toggle(name, colour = COLOURS[i],
                    command = lambda: self.toggle(i))
            self._data_frame.add_label(name, colour = COLOURS[i])
            self._data_frame.refresh()
            self._plotter.refresh()

    def open_file(self):
        """
        Handles the File->Open menu command

        open_file(self) -> None
        """

        filename = tk.filedialog.askopenfilename()

        self.add_station(filename)




##################################################
# !!!!!! Do not change (or add to) the code below !!!!!
###################################################

def main():
    root = tk.Tk()
    app = TemperaturePlotApp(root)
    root.geometry("800x400")
    root.mainloop()

if __name__ == '__main__':
    main()
