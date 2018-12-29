from elf import Elf


def main():
    with open("input.txt", "+r") as file:
        recipes = int(file.readlines()[0])

    # set up initial state
    scoreboard = [3, 7]
    elf1 = Elf(0)
    elf2 = Elf(1)
    print(elf1.current_index)

    # main update loop
    while scoreboard.__len__() < recipes + 12:

        # Calculate next recipe and append to scoreboard
        next_recipe = scoreboard[elf1.current_index] + scoreboard[elf2.current_index]

        if next_recipe > 9:
            scoreboard.append(1)
            scoreboard.append(next_recipe-10)
        else:
            scoreboard.append(next_recipe)

        # set new current recipes for both elves
        elf1.cycle(scoreboard)
        elf2.cycle(scoreboard)

    for i in range(recipes, recipes+10):
        print(scoreboard[i], end='', flush=True)


if __name__ == '__main__':
    main()
