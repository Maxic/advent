from cart import Cart


def main():
    with open("input.txt", "r+") as file:
        cart_map = file.readlines()

    for i in range(0, cart_map.__len__()):
        cart_map[i] = list(cart_map[i].replace('\n', ''))

    with open("clean_map.txt", "r+") as file:
        clean_map = file.readlines()

    # initialize all cart objects
    cart_dict = {}
    for y in range(0, cart_map.__len__()):
        for x in range(0, cart_map[0].__len__()):
            # fuck this, pycharm automatically trims the right spaces in the input, which sucks, don't open input.txt
            if cart_map[y][x] in ['^', '<', '>', 'v']:
                cart_dict[(x, y)] = Cart(x, y, cart_map[y][x])

    # set crashed flag
    tick = 0

    # main loop
    while cart_dict.__len__() > 1:
        #print_map(cart_map)
        cart_map, cart_dict, tick = update(cart_map, clean_map, cart_dict, tick)

    # results
    print(cart_dict)
    print(list(cart_dict.values())[0].x, list(cart_dict.values())[0].y)


def update(cart_map, clean_map, cart_dict, tick):
    tick += 1

    # order cart list
    sorted_car_keys = sorted(cart_dict.keys())

    # loop through all ordered carts
    for key in sorted_car_keys:
        # if key is not in dict, it already crashed
        if key in cart_dict:
            cart = cart_dict[key]
            # remove yourself from dict
            cart_dict.pop(key)
        else:
            continue

        # remove cart from map
        cart_map[cart.y][cart.x] = clean_map[cart.y][cart.x]

        # do step
        position, direction, state = cart.step(cart_map)

        # check for crashes
        if state == 'crashed':
            print('Cart crashed!')
            print(position)
            cart_map[position[1]][position[0]] = clean_map[position[1]][position[0]]
            if position in cart_dict:
                cart_dict.pop(position)
        else:
            # add new position to dict
            cart_dict[(position[0], position[1])] = cart
            # draw cart on map
            cart_map[position[1]][position[0]] = direction

    return cart_map, cart_dict, tick


def print_map(cart_map):
    for line in cart_map:
        line_str = ''.join(line)
        print(line_str)
    print()


if __name__ == '__main__':
    main()
