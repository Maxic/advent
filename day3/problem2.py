import re


def main():
    with open("input.txt", "r+") as file:
        claims = file.readlines()

    coordinates_list = []
    max_xpos = 0
    max_ypos = 0

    for claim in claims:
        # Parse claim
        match = re.match(r"(.*)@ (.*),(.*): (.*)x(.*)", claim.rstrip())
        xpos = int(match.group(2))
        ypos = int(match.group(3))
        width = int(match.group(4))
        length = int(match.group(5))

        # create coordinate list
        coordinates_list.append(get_coordinates(xpos, ypos, width, length))

        # get boundaries
        if xpos > max_xpos:
            max_xpos = xpos
        if ypos > max_ypos:
            max_ypos = ypos

    coordinates_id = 0
    grid = [[0 for j in range(0, 1000)] for i in range(0, 1000)]

    # fill coordinates
    for coordinates in coordinates_list:
        for coordinate in coordinates:
            if grid[coordinate[0]][coordinate[1]] == 0:
                grid[coordinate[0]][coordinate[1]] = 1
            else:
                grid[coordinate[0]][coordinate[1]] = 8

    # check grid again for overlap
    for coordinates in coordinates_list:
        coordinates_id += 1
        coordinates_overlap = False
        for coordinate in coordinates:
            if grid[coordinate[0]][coordinate[1]] == 8:
                coordinates_overlap = True
        if not coordinates_overlap:
            print(coordinates_id)
            break


def print_grid(grid):
    for list in grid:
        print(list)


def get_coordinates(xpos, ypos, width, length):
    coordinates = []
    for i in range(ypos,ypos+length):
        for j in range(xpos, xpos+width):
            coordinates.append((j, i))
    return coordinates


if __name__ == "__main__":
    main()
