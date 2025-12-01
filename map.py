class Map:
    HEIGHT = 3
    WIDTH = 5

    def __init__(self, road_map, vehicle_map):
        self.road_map = road_map
        self.vehicle_map = vehicle_map

    def display_traffic(self):
        for _,row in enumerate(self.road_map):
            print(row)

    def construct_road(self):
        road_dict = {} #coord,char
        for i,row in enumerate(self.road_map):
            for j,cell in enumerate(row):
                road_dict[(i,j)] = cell
                
        line = ""
        count = 1
        for coord,char in road_dict.items():
            if self.vehicle_map[coord[0]][coord[1]] == 'V':
                line += 'V'
            else:
                line+= char

            if count == 5:
                print(line)
                line = ""
                count = 0

            count += 1