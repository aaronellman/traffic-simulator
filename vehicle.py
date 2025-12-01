class Vehicle:
    SPEED = 1

    POSITION: tuple = ()

    def __init__(self, vehicle_map):
        POSITION = self.find_pos(vehicle_map)

    def find_pos(vehicle_map):
        for y,row in enumerate(vehicle_map):
            if "V" not in row:
                continue
            for x,cell in enumerate(row):
                if cell == "V":
                    return (x,y)
        

