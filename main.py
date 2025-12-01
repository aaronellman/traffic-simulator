import time
from map import Map
from terminal_operations import clear_terminal

def main():

    road_map = [
    ['A', '─', '─', '─', '+'],
    [' ', ' ', ' ', ' ', '|'],
    ['B', '─', '─', '─', '+']
    ]

    vehicle_map = [
    [' ', 'V', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
    ]

    map = Map(road_map, vehicle_map)
    map.construct_road()

    #Game Loop
    while False:
        clear_terminal()
        #map.display_traffic()
        time.sleep(0.2)    


if __name__ == "__main__":
    main()
