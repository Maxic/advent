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

    # fill grid with
    for i in range(0, grid.__len__()):
        for j in range(0, grid[0].__len__()):
            distances = {}
            for coordinate_id in coordinates.keys():
                coordinate = coordinates[coordinate_id]
                distances[coordinate_id] = calc_manhattan_distance(i, j, coordinate[0], coordinate[1])
            min_distance = 2000
            for coordinate_id in distances.keys():
                if distances[coordinate_id] == min_distance:
                    grid_symbol = '.'
                if distances[coordinate_id] < min_distance:
                    min_distance = distances[coordinate_id]
                    grid_symbol = coordinate_id
            grid[j][i] = grid_symbol

    # get all coordinates on grid borders
    infinite_coordinates = set()
    # Horizontal
    for i in [0, 399]:
        for j in range(0, grid[0].__len__()):
            infinite_coordinates.add(grid[i][j])

    # Vertical
    for i in range(0, grid.__len__()):
        for j in [0, 399]:
            infinite_coordinates.add(grid[i][j])

    # count area size for all non-infinite area's
    coordinate_area_size = {}

    for i in range(0, grid.__len__()):
        for j in range(0, grid[0].__len__()):
            if grid[j][i] not in infinite_coordinates:
                if grid[j][i] not in coordinate_area_size:
                    coordinate_area_size[grid[j][i]] = 0
                else:
                    coordinate_area_size[grid[j][i]] += 1

    max_area_size = 0
    for key in coordinate_area_size.keys():
        max_area_size = max(coordinate_area_size[key], max_area_size)

    print(max_area_size+1)


def calc_manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


if __name__ == '__main__':
    main()
