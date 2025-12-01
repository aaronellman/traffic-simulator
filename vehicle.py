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

    def get_valid_next_step(self, road_map, WIDTH, HEIGHT):
        options = ["up", "down", "left", "right"]
        ROAD_CHARS = {"─", "+", "|"}

        x,y = self.POSITION

        if x == WIDTH - 1:
            options.remove("right")
        if x == 0:
            options.remove("left")
        if y == HEIGHT - 1:
            options.remove("down")
        if y == 0:
            options.remove("up")

        if road_map[x + 1][y] not in ROAD_CHARS:
            options.remove("right")
        if road_map[x - 1][y] not in ROAD_CHARS:
            options.remove("left")
        if road_map[x][y + 1] not in ROAD_CHARS:
            options.remove("down")
        if road_map[x][y - 1] not in ROAD_CHARS:
            options.remove("up")
        
        

