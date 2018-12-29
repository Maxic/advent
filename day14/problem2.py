from elf import Elf


def main():
    with open("input.txt", "+r") as file:
        score_output = file.readlines()[0]

    match_check = [int(char) for char in score_output]

    # Expanding on initial state prevents having to check for length each round
    scoreboard = [3, 7, 1, 0, 1, 0, 1]
    elf1 = Elf(4)
    elf2 = Elf(6)

    # main update loop
    while True:

        # Calculate next recipe and append to scoreboard
        next_recipe = scoreboard[elf1.current_index] + scoreboard[elf2.current_index]

        if next_recipe > 9:
            scoreboard.append(1)
            if scoreboard[scoreboard.__len__() - match_check.__len__():] == match_check:
                break
            scoreboard.append(next_recipe-10)
        else:
            scoreboard.append(next_recipe)

        if scoreboard[scoreboard.__len__()-match_check.__len__():] == match_check:
            break

        # set new current recipes for both elves
        elf1.cycle(scoreboard)
        elf2.cycle(scoreboard)

    print(scoreboard.__len__()-match_check.__len__())


if __name__ == '__main__':
    main()
