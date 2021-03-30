import pprint
def get_data(filename):
    f = open(filename, "r")
    l = []
    for y, line in enumerate(f):
        x_list = []
        for x,seat in enumerate(line.strip()):
            x_list.append(seat)
            # { (0,1): "L", ... }
        l.append(x_list)
    return l

class ShipSeats:
    def __init__(self, data):
        self.data = data
        self.max_x = len(data[0]) - 1
        self.max_y = len(data) - 1



    def get_adj_seats(self, coord):
        (x, y) = coord
        coord_list = []
        if x - 1 >= 0:
            coord_list.append((x-1,y))
        if y - 1 >= 0:
            coord_list.append((x,y-1))
        if x - 1 >= 0 and y - 1 >= 0:
            coord_list.append((x-1,y-1))
        if x + 1 <= self.max_x:
            coord_list.append((x+1,y))
        if y + 1 <= self.max_y:
            coord_list.append((x,y+1))
        if y + 1 <= self.max_y and x + 1 <= self.max_x:
            coord_list.append((x+1,y+1))
        if y + 1 <= self.max_y and x - 1 >= 0:
            coord_list.append((x-1,y+1))
        if x + 1 <= self.max_y and y - 1 >= 0:
            coord_list.append((x+1, y-1))

        return coord_list

    def get_adj_seat_count(self, cord):
        adj_seats = self.get_adj_seats(cord)
        count = 0
        for p,q in adj_seats:
            # p,q = adj_coord
            adj_val = self.data[q][p]
            if adj_val == "#":
                count += 1
        return count

    def compute_next_state(self):
        copy = [sublist[:] for sublist in self.data]
        listChanged = False
        lcount, hashCount = 0, 0
        for x in range(self.max_x + 1):
            for y in range(self.max_y + 1):
                seat = self.data[y][x]
                if seat == ".":
                    continue
                num_adj = self.get_adj_seat_count((x,y))
                if seat == "L" and num_adj == 0:
                    copy[y][x] = "#"
                    lcount += 1
                    listChanged = True
                elif seat == "#" and num_adj >= 4:
                    copy[y][x] = "L"
                    hashCount += 1
                    listChanged = True
        # print(copy)
        self.data = copy
        print(f"lcount: {lcount}, hashCount: {hashCount}")
        return listChanged

    def get_final_state(self):
        pp = pprint.PrettyPrinter(indent=4)
        while self.compute_next_state():
            continue

        total = 0
        for x in range(self.max_x + 1):
            for y in range(self.max_y + 1):
                seat = self.data[y][x]
                if seat == "#":
                    total += 1
        return total






# data = get_data("input_day_11.txt")
# val = ShipSeats(data)
# pp = pprint.PrettyPrinter(indent=4)
# #pp.pprint(next_state)
# pp.pprint(val.get_final_state())

f = open("test_11.txt", "r").readlines()
print(len(f))