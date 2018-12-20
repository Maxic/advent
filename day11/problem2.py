def main():
    with open("input.txt", "r+") as file:
        content = file.readlines()

    grid_serial_number = int(content[0])
    coordinates_power_level = {}

    for y in range(1, 301):
        for x in range(1, 301):
            power_level = calculate_power_level(grid_serial_number, x, y)
            coordinates_power_level[(x, y)] = power_level

    square_size_sum = {}
    for square_size in range(1, 301):
        coordinates, max_square_sum = calculate_maximum_sum_square(coordinates_power_level, square_size, 300)
        square_size_sum[coordinates] = max_square_sum
        if max_square_sum < 0:
            break
        print(square_size)
        print(max_square_sum)
        print(coordinates)
        print()

    max_coordinates = max(square_size_sum, key=lambda key: square_size_sum[key])
    print(max_coordinates, square_size_sum[max_coordinates])


def calculate_power_level(grid_serial_number, x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial_number
    power_level *= rack_id
    power_level = int(power_level / 100 % 10)
    power_level -= 5
    return power_level


def calculate_maximum_sum_square(power_level_dict, square_size, grid_size):
    coordinates_square_sum = {}

    # Loop through all top-left coordinates where square with squaresize fits
    for y in range(1, (grid_size+2)-square_size):
        for x in range(1, (grid_size+2)-square_size):
            square_sum = 0

            # Loop through square and sum all power levels
            for j in range(square_size):
                for i in range(square_size):
                    square_sum += power_level_dict[(x+i), (y+j)]

            coordinates_square_sum[(x, y, square_size)] = square_sum
    max_square_key = max(coordinates_square_sum, key=lambda key: coordinates_square_sum[key])
    return max_square_key, coordinates_square_sum[max_square_key]


if __name__ == '__main__':
    main()



