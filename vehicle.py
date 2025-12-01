class Vehicle:
    SPEED = 1

    POSITION: tuple
    TARGET_POS: tuple
    DESTINATION: str = "B"

    def __init__(self, vehicle_map):
        self.POSITION = self.find_pos(vehicle_map, "V")
        self.TARGET_POS = self.find_pos(vehicle_map,self.DESTINATION)

    def find_pos(vehicle_map, char_to_find):
        for y,row in enumerate(vehicle_map):
            if char_to_find not in row:
                continue
            for x,cell in enumerate(row):
                if cell == char_to_find:
                    return (x,y)
    
    def move(direction):
        directions = ["up", "down", "left", "right"]
        match direction:
            case "up":
                POSITION = POSITION[1] + 1
            case "down":
                POSITION = POSITION[1] - 1
            case "left":
                POSITION = POSITION[0] - 1
            case "right":
                POSITION = POSITION[0] + 1

        

