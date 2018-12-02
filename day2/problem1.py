def main():
    with open("input.txt", "r+") as file:
        box_ids = file.readlines()

    sum_twos  = 0;
    sum_threes = 0;
    for box_id in box_ids:
        letter_count = {}
        for letter in box_id.rstrip():
            if not letter in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1
        if list(letter_count.values()).count(2) > 0:
            sum_twos += 1
        if list(letter_count.values()).count(3) > 0:
            sum_threes += 1
    print(sum_twos)
    print(sum_threes)
    print(sum_twos * sum_threes)


if __name__ == "__main__":
    main()
