import re


def main():
    with open("input.txt", "r+") as file:
        claims = file.readlines()

    coordinates_list = []
    overlap_count = 0

    for claim in claims:
        # Parse claim
        match = re.match(r"(.*)@ (.*),(.*): (.*)x(.*)", claim.rstrip())
        xpos = int(match.group(2))
        ypos = int(match.group(3))
        width = int(match.group(4))
        length = int(match.group(5))

        # create coordinate list
        coordinates_list.append(get_coordinates(xpos, ypos, width, length))

    # fill coordinates
    grid = [[0 for j in range(0, 1000)] for i in range(0, 1000)]
    for coordinates in coordinates_list:
        for coordinate in coordinates:
            if grid[coordinate[0]][coordinate[1]] == 0:
                grid[coordinate[0]][coordinate[1]] = 1
            else:
                grid[coordinate[0]][coordinate[1]] = 8

    # check for overlap
    for list in grid:
        for item in list:
            if item == 8:
                overlap_count += 1

    print(overlap_count)


def get_coordinates(xpos, ypos, width, length):
    coordinates = []
    for i in range(ypos,ypos+length):
        for j in range(xpos, xpos+width):
            coordinates.append((j, i))
    return coordinates


if __name__ == "__main__":
    main()
