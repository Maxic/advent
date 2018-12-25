import re


def main():
    with open("input.txt", "r+") as file:
        content = file.readlines()

    # initialize current state dict
    current_state_list = re.match(r'initial state: (.*)', content[0]).group(1).rstrip()
    current_state = {}
    for pot_index in range(0, current_state_list.__len__()):
        current_state[pot_index] = current_state_list[pot_index]

    # initialize ruleset
    rules = []
    for rule in content[2:]:
        match = re.match(r'(.*) => (.*)', rule)
        rules.append((match.group(1), match.group(2)))

    generations = 50000

    # Generate new state for each generation
    for generation in range(1, generations+1):
        new_state = {}
        plant_indexes = [k for k, v in current_state.items() if v == '#']
        max_plant_index = max(plant_indexes)
        min_plant_index = min(plant_indexes)

        # loop over all plants to check new state against rules
        for plant_index in range(min_plant_index-3, max_plant_index+3):
            # get local state around plant_index
            local_state = get_state(plant_index, current_state)
            new_plant = match_rule(local_state, rules)
            new_state[plant_index] = new_plant
        current_state = new_state

    print(sum([k for k, v in current_state.items() if v == '#']))
    # 50000000000 = 1799999999458


def get_state(plant_index, current_state):
    state = []

    for i in range(plant_index-2, plant_index+3):
        if i in current_state.keys():
            state.append(current_state[i])
        else:
            state.append('.')

    return state


def match_rule(state, rules):
    for rule in rules:
        if list(rule[0]) == state:
            return rule[1]
    return '.'


def print_state(current_state):
    sorted_index = sorted(current_state.keys())
    for i in sorted_index:
        print(current_state[i], end='', flush=True)
    print()


if __name__ == '__main__':
    main()
