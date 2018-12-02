import itertools


def main():
    freq = 0
    freq_set = set()

    with open("input.txt", "r+") as file:
        content = itertools.cycle(file.readlines())
        while True:
            freq_set_length = freq_set.__len__()
            freq_set.add(freq)
            line = next(content)

            if freq_set_length == freq_set.__len__():
                break

            if line[:1] == '+':
                freq = freq + int(line[1:])
            else:
                freq = freq - int(line[1:])

        print(freq)


if __name__ == "__main__":
    main()
