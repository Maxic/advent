def main():
    with open("input.txt", "r+") as file:
        logs = file.readlines()

    for log in logs:
        print(log)


if __name__ == '__main__':
    main()