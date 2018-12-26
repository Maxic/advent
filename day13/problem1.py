from cart import Cart


def main():
    with open("input.txt", "r+") as file:
        cart_map = file.readlines()

    for i in range(0, cart_map.__len__()):
        cart_map[i] = list(cart_map[i].replace('\n', ''))

    with open("clean_map.txt", "r+") as file:
        clean_map = file.readlines()

    # initialize all cart objects
    cart_list = []
    for y in range(0, cart_map.__len__()):
        for x in range(0, cart_map[0].__len__()):
            # fuck this, pycharm automatically trims the output, which sucks, don't open input.txt
            if cart_map[y][x] in ['^', '<', '>', 'v']:
                cart_list.append(Cart(x, y, cart_map[y][x]))

    # set crashed flag
    crashed = False
    tick = 0

    # main loop
    while not crashed:
        print_map(cart_map)
        cart_map, crashed, tick = update(cart_map, clean_map, cart_list, tick)
        print(tick)


def update(cart_map, clean_map, cart_list, tick):
    tick += 1
    # set crash flag
    crashed = False

    # order cart list
    cart_dict = {}
    for cart in cart_list:
        cart_dict[(cart.x, cart.y)] = cart
    sorted_car_keys = sorted(cart_dict.keys())

    # loop through all ordered carts
    for key in sorted_car_keys:
        cart = cart_dict[key]
        # remove cart from map
        cart_map[cart.y][cart.x] = clean_map[cart.y][cart.x]

        # do step
        position, direction, state = cart.step(cart_map)

        # check for crashes
        if state == 'crashed':
            print('Cart crashed!')
            print(position)
            crashed = True
            break

        # draw cart on map
        cart_map[position[1]][position[0]] = direction

    return cart_map, crashed, tick


def print_map(cart_map):
    for line in cart_map:
        line_str = ''.join(line)
        print(line_str)
    print()


if __name__ == '__main__':
    main()
