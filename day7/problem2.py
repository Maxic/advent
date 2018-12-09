import re


def main():
    with open("input.txt", "r+") as file:
        steps_raw = file.readlines()

    next_steps = {}
    alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # create a dict with all prerequisites for each state
    for step in steps_raw:
        match = re.match(r'Step (.*) must be finished before step (.*) can begin', step.rstrip())
        first_state = match.group(1)
        second_state = match.group(2)
        if second_state not in next_steps:
            next_steps[second_state] = set()
        if first_state not in next_steps:
            next_steps[first_state] = set()
        next_steps[second_state].add(first_state)

    seconds = -1
    possible_steps = set()
    solution = ''
    solution_length = next_steps.__len__()
    workers = {1: (None, -1), 2: (None, -1), 3: (None, -1), 4: (None, -1)}
    check_possible_steps = True

    while solution.__len__() < solution_length:
        seconds += 1
        # Check if workers are done
        for worker_id in workers.keys():
            if workers[worker_id][1] == seconds:
                step = workers[worker_id][0]
                solution = solution + step
                for prereq in next_steps.values():
                    prereq.discard(step)
                workers[worker_id] = (None, -1)
                check_possible_steps = True

        # get possible steps to work on
        if check_possible_steps:
            for state in next_steps.keys():
                if not next_steps[state]:
                    possible_steps.add(state)
                    check_possible_steps = False

        # start new jobs
        for worker_id in workers.keys():
            if possible_steps and workers[worker_id][0] is None:
                step = sorted(list(possible_steps))[0]
                possible_steps.remove(step)
                del (next_steps[step])
                workers[worker_id] = (step, seconds + 60 + alphabet.find(step))

    print(seconds)


if __name__ == '__main__':
    main()
