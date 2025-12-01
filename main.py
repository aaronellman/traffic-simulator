import time
from map import Map
from terminal_operations import clear_terminal
from vehicle import Vehicle

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
    vehicle = Vehicle(vehicle_map)
    
    #Game Loop
    while True:
        clear_terminal()
        map.construct_road()
        vehicle.move("right",vehicle_map)
        time.sleep(2)    


if __name__ == "__main__":
    main()
