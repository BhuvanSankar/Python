from project_support import *

def load_dates(stations):
    """Return the list of dates in the data for the first station
    in stations.

    load_date_list(str) -> list(str)
    """
    fd = open(stations[0]+".txt", "r")
    dates = []
    for line in fd:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        dates.append(parts[0])
    fd.close()
    return dates
    
def load_station_data(station):
    """Return the list of temps for station data

    load_station_data(str) -> list(float)
    """
    fd = open(station+".txt", "r")
    data = []
    for line in fd:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        data.append(float(parts[1]))
    fd.close()
    return data

def load_all_stations_data(stations):
    """Return a tuple of station data for each station in stations

    load_all_stations_data(list(str)) -> tuple(list(str))
    """
    all_data = []
    for station in stations:
        all_data.append(load_station_data(station))
    return all_data


def display_maxs(stations, dates, data, start_date, end_date):
    """Display a table of temps for all the stations from start_date
    up to and including end_date if both dates are valid dates in order
    and returns True
    If dates are not valid or not in order then return False

    display_maxs(list(str), list(str), list(list(float)), str, str) -> None
    """
    start_index = dates.index(start_date)
    end_index = dates.index(end_date)
    display_stations(stations, "Date")
    stations_size = len(stations)
    
    for index in range(start_index, end_index+1):
        print("{:<12}".format(dates[index]), end='')
        for station_index in range(stations_size):
            display_temp(data[station_index][index])
        print()




def temperature_diffs(data, dates, stations, station1, station2,
                      start_date, end_date):
    """ Return the list of date, temp diff pairs

    Precondition: start_date and end_date are valid dates in range
    and station1 and station2 are in stations

    temperature_diffs(list(list(float)), list(str), list(str), str,
                      str, str, str) ->  list((str, float))

    """
    result = []
    start_index = dates.index(start_date)
    end_index = dates.index(end_date)
    s1_index = stations.index(station1)
    s2_index = stations.index(station2)
    
    for index in range(start_index, end_index+1):
        temp1 = data[s1_index][index]
        temp2 = data[s2_index][index]
        if temp1 == UNKNOWN_TEMP or temp2 == UNKNOWN_TEMP:
            diff = UNKNOWN_TEMP
        else:
            diff = temp1 - temp2
        result.append((dates[index], diff))

    return result

def display_diffs(diffs, station1, station2):
    print("Temperature differences between {0} and {1}".format(station1, station2))
    print()
    print("{0:<10}{1:<5}".format("Date", "Temperature Differences"))
    for d, t in diffs:
        print("{0:<10}".format(d), end='')
        display_temp(t)
        print()


## start CSSE7030 extras
def yearly_averages(dates, data, start_year, end_year):
    """Return the list of yearly averages for each station from start_year
    up to and including end_year together with the list of years

    Precondition: the start to end years are in the data

    yearly_averages(list(str), list(list(float)), str, str) -> 
                        (list(str),list(list(float)))
    """
    years, indicies = get_year_info(dates, start_year, end_year)

    averages = []
    num_stations = len(data)

    averages = []
    for station_index in range(num_stations):
        station_averages = []
        for i in range(len(years)):
            average = get_yearly_average(data[station_index], 
                                    indicies[i], indicies[i+1])
            station_averages.append(average)
        averages.append(station_averages)
    return (years, averages)
    

def display_yearly_averages(years, averages, stations):
    display_stations(stations, "Year")
    num_stations = len(stations)
    for index in range(len(years)):
        print("{:<12}".format(years[index]), end='')
        for station_index in range(num_stations):
            display_temp(averages[station_index][index])
        print()

## end CSSE7030 extras

def interact():
    """The top-level interaction"""

    print('\nWelcome to BOM Data\n')
    
    stations_file = input("Please enter the name of the Stations file: ").strip()
    stations = load_stations(stations_file)
    dates = load_dates(stations)
    data = load_all_stations_data(stations)

    while True:
        cmd = input("\nCommand: ").strip()
        args = cmd.split()
        if len(args) == 3 and args[0] == 'dm':
            print()
            display_maxs(stations, dates, data, args[1], args[2])
        elif len(args) == 5 and args[0] == 'dd':
            print()
            diffs = temperature_diffs(data, dates, stations, 
                                      args[1], args[2], args[3], args[4])
            display_diffs(diffs, args[1], args[2])
        elif len(args) == 3 and args[0] == 'ya':
            # CSSE7030 
            print()
            years, averages = yearly_averages(dates, data, args[1], args[2])
            display_yearly_averages(years, averages, stations)
        elif cmd in 'qQ':
            break
        else:
            print("Unknown command:", cmd)

if __name__ == '__main__':
    interact()
