import re
import time


def main():
    with open("input.txt", "r+") as file:
        movements = file.readlines()

    stars = []
    for movement in movements:
        match = re.match(r'position=<(.*),(.*)> velocity=<(.*),(.*)>', movement.rstrip())
        coordinates = (int(match.group(1).lstrip()), int(match.group(2).lstrip()))
        velocity = (int(match.group(3).lstrip()), int(match.group(4).lstrip()))
        star = [coordinates, velocity]
        stars.append(star)

    time_count = -1
    converged = False

    while True:
        max_x, max_y, min_x, min_y, stars = update_stars(stars)

        x_range = max_x - min_x
        y_range = max_y - min_y
        print('x_range: ' + str(x_range))
        print('y_range: ' + str(y_range))
        print()
        time_count += 1
        if x_range < 62 and y_range < 10:
            # create and fill grid
            grid = [['.' for _ in range(0, max_x+1)] for _ in range(0, max_y+1)]
            grid = fill_grid(grid, stars)

            # print grid
            time.sleep(1)
            print_grid(grid)
            converged = True
        elif converged:
            print(time_count)
            break


def fill_grid(grid, stars):
    for star in stars:
        x = star[0][0]
        y = star[0][1]
        grid[y][x] = 'X'
    return grid


def update_stars(stars):
    y_list = []
    x_list = []
    # change coordinates by velocity
    for star in stars:
        star[0] = (star[0][0] + star[1][0], star[0][1] + star[1][1])
        y_list.append(star[0][1])
        x_list.append(star[0][0])
    max_x = max(x_list)
    max_y = max(y_list)
    min_y = min(y_list)
    min_x = min(x_list)
    return max_x, max_y, min_x, min_y, stars


def print_grid(grid):
    for row in grid:
        print(row)
    print()


if __name__ == '__main__':
    main()
