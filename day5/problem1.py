def main():
    with open("input.txt", "r+") as file:
        polymer = file.readline()
    polymer_list = [character for character in polymer]

    i = 0
    while True:
        if i >= polymer_list.__len__()-1:
            if not removed_unit:
                break
            removed_unit = False
            i = 0

        unit1 = polymer_list[i]
        unit2 = polymer_list[i+1]

        if unit1.lower() == unit2.lower():
            if (unit1.isupper() and unit2.islower()) or (unit1.islower() and unit2.isupper()):
                polymer_list.pop(i)
                polymer_list.pop(i)
                removed_unit = True
        i += 1

    print(polymer_list.__len__())


if __name__ == '__main__':
    main()
