def main():
    with open('input.txt', '+r') as file:
        content = file.readlines()

    # initialize area map and minutes
    minute = 0
    area = []
    for line in content:
        area.append(list(line.rstrip()))

    # main loop
    while minute < 1000:
        new_area = [[0] * area[0].__len__() for i in range(area.__len__())]

        for y in range(0, area.__len__()):
            for x in range(0, area[0].__len__()):
                # determine new acre by surroundings
                current_acre = area[y][x]

                wooded, lumberyard = count_acre_types(area, x, y)
                new_acre = determine_acre_type(current_acre, lumberyard, wooded)

                new_area[y][x] = new_acre

        minute += 1
        area = new_area

    # count total value
    wooded = 0
    lumberyard = 0

    print_map(area)

    for y in range(0, area.__len__()):
        for x in range(0, area[0].__len__()):
            acre = area[y][x]
            if acre == '|':
                wooded += 1
            elif acre == '#':
                lumberyard += 1
    print(wooded)
    print(lumberyard)
    print(wooded * lumberyard)


def determine_acre_type(current_acre, lumberyard, wooded):
    if current_acre == '.':
        if wooded >= 3:
            return '|'
        else:
            return '.'
    if current_acre == '|':
        if lumberyard >= 3:
            return '#'
        else:
            return '|'
    if current_acre == '#':
        if lumberyard >= 1 and wooded >= 1:
            return '#'
        else:
            return '.'


def count_acre_types(area, x, y):
    wooded = 0
    lumberyard = 0

    x_len = area[0].__len__()-1
    y_len = area.__len__()-1

    # determine list of neighbours in bounds
    neighbours = [(x2, y2) for x2 in range(x - 1, x + 2)
                  for y2 in range(y - 1, y + 2)
                  if (-1 < x <= x_len and
                      -1 < y <= y_len and
                      (x != x2 or y != y2) and
                      (0 <= x2 <= x_len) and
                      (0 <= y2 <= y_len))]

    # count all wooded and lumberyard in neighbours
    for neighbour in neighbours:
        acre = area[neighbour[1]][neighbour[0]]
        if acre == '|':
            wooded += 1
        elif acre == '#':
            lumberyard += 1

    return wooded, lumberyard


def print_map(area):
    for row in area:
        print(''.join(row))
    print()


if __name__ == '__main__':
    main()
