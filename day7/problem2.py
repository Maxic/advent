import re


def main():
    with open("input.txt", "r+") as file:
        steps_raw = file.readlines()

    next_steps = {}

    for step in steps_raw:
        match = re.match(r'Step (.*) must be finished before step (.*) can begin', step.rstrip())
        first_state = match.group(1)
        second_state = match.group(2)
        if second_state not in next_steps:
            next_steps[second_state] = set()
        if first_state not in next_steps:
            next_steps[first_state] = set()
        next_steps[second_state].add(first_state)


if __name__ == '__main__':
    main()
