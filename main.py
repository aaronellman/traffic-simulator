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
    
    #Game Loop
    while True:
        clear_terminal()
        map.construct_road()
        time.sleep(0.15)    


if __name__ == "__main__":
    main()
