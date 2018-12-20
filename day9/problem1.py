import re
import itertools


def main():
    with open("input.txt", "r+") as file:
        content = file.readlines()
    match = re.match(r'(.*) players; last marble is worth (.*) points', content[0])
    player_amount = int(match.group(1))
    last_marble = int(match.group(2))

    circle = [0]
    current_index = 1
    score = {}

    # initialize score dict
    for player in range(1, player_amount + 1):
        score[player] = 0

    # setup player cycle
    player_cycle = itertools.cycle(range(1, player_amount+1))

    for marble in range(1, last_marble+1):

        # Get current player to keep score
        player = next(player_cycle)

        # Keep score if the marble is a multiple of 23
        if marble % 23 == 0 and marble != 0:
            # remove 7th counterclockwise marble and add to score
            current_index, removed_marble = cycle_nine_left(current_index, circle)

            # Add current and removed marble to score
            score[player] += marble
            score[player] += removed_marble
        else:
            # place marble
            circle.insert(current_index, marble)

        # get new index
        current_index = cycle_two_right(current_index, circle)

    print(max(score.values()))


def cycle_nine_left(current_index, circle):
    new_index = current_index - 9

    if new_index < 0:
        new_index = circle.__len__() + new_index

    score = circle.pop(new_index)

    return new_index, score


def cycle_two_right(current_index, circle):
    new_index = current_index + 2

    if new_index > circle.__len__():
        return new_index - circle.__len__()
    else:
        return new_index


if __name__ == '__main__':
    main()
