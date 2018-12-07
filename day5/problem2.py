def main():
    with open("input.txt", "r+") as file:
        polymer = file.readline()
    polymer_list = [character for character in polymer]

    polymer_character_length = {}

    for character in 'abcdefghijklmnopqrstuvwxyz':
        print(character)
        polymer_list_filtered = list(filter(lambda x: x.lower() != character, polymer_list))
        polymer_character_length[character] = fully_react(polymer_list_filtered).__len__()

    shortest_polymer = min(polymer_character_length, key=lambda key: polymer_character_length[key])
    print(shortest_polymer)


def fully_react(polymer_list):
    i = 0
    removed_unit = False

    while True:
        if i >= polymer_list.__len__() - 1:
            if not removed_unit:
                break
            removed_unit = False
            i = 0
        if not polymer_list:
            break
        unit1 = polymer_list[i]
        unit2 = polymer_list[i + 1]

        if unit1.lower() == unit2.lower():
            if (unit1.isupper() and unit2.islower()) or (unit1.islower() and unit2.isupper()):
                polymer_list.pop(i)
                polymer_list.pop(i)
                removed_unit = True
        i += 1
    return list(polymer_list)


if __name__ == '__main__':
    main()
