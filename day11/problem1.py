def main():
    with open("input.txt", "r+") as file:
        content = file.readlines()

    grid_serial_number = int(content[0])
    power_level_dict = {}

    for y in range(1, 301):
        for x in range(1, 301):
            power_level = calculate_power_level(grid_serial_number, x, y)
            power_level_dict[(x, y)] = power_level

    sum_3x3_grid_dict = {}

    for position in power_level_dict.keys():
        sum_3x3_grid = 0
        x_pos = position[0]
        y_pos = position[1]

        try:
            for y in range(y_pos, y_pos + 3):
                for x in range(x_pos, x_pos + 3):
                    sum_3x3_grid += power_level_dict[(x, y)]
        except:
            pass
        sum_3x3_grid_dict[position] = sum_3x3_grid

    max_key = max(sum_3x3_grid_dict, key=lambda key: sum_3x3_grid_dict[key])
    print(max_key)


def calculate_power_level(grid_serial_number, x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level = power_level + grid_serial_number
    power_level = power_level * rack_id
    power_level = int(power_level / 100 % 10)
    power_level -= 5
    return power_level


if __name__ == '__main__':
    main()
