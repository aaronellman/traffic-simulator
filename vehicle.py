class Vehicle:
    SPEED = 1

    POSITION: tuple
    TARGET_POS: tuple
    DESTINATION: str = "B"

    def __init__(self, vehicle_map):
        self.POSITION = self.find_pos(vehicle_map, "V")
        self.TARGET_POS = self.find_pos(vehicle_map,self.DESTINATION)

    def find_pos(self,vehicle_map, char_to_find):
        for y,row in enumerate(vehicle_map):
            if char_to_find not in row:
                continue
            for x,cell in enumerate(row):
                if cell == char_to_find:
                    return (x,y)
    
    def move(self, direction, vehicle_map):
        prev_x, prev_y = self.POSITION
        
        match direction:
            case "up":
                self.POSITION = (prev_x, prev_y - 1)
            case "down":
                self.POSITION = (prev_x, prev_y + 1)
            case "left":
                self.POSITION = (prev_x - 1, prev_y)
            case "right":
                self.POSITION = (prev_x + 1, prev_y)
        
        new_y,new_x = self.POSITION

        #print(f"Previous X: {prev_x}, Previous Y: {prev_y}")
        #print(f"New X: {new_x}, New Y: {new_y}")

        vehicle_map[prev_y][prev_x] = " "
        vehicle_map[new_x][new_y] = "V"
        

