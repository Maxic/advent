import re


def main():
    with open("input.txt", "r+") as file:
        coordinates_raw = file.readlines()

    grid = [[0 for j in range(0, 400)] for i in range(0, 400)]
    coordinates = {}
    coordinate_id = 0

    # parse input
    for coordinate in coordinates_raw:
        coordinate_id += 1
        match = re.match(r'(.*), (.*)', coordinate.rstrip())
        xpos = int(match.group(1))
        ypos = int(match.group(2))

        grid[xpos][ypos] = coordinate_id
        coordinates[coordinate_id] = (xpos, ypos)

    region_size = 0

    # fill grid with
    for i in range(0, grid.__len__()):
        for j in range(0, grid[0].__len__()):
            distances = {}
            for coordinate_id in coordinates.keys():
                coordinate = coordinates[coordinate_id]
                distances[coordinate_id] = calc_manhattan_distance(i, j, coordinate[0], coordinate[1])
            if sum(distances.values()) < 10000:
                region_size += 1

    print(region_size)


def calc_manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


if __name__ == '__main__':
    main()
