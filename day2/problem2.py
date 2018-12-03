def main():
    with open("input.txt", "r+") as file:
        box_ids = file.readlines()
    counter = 0
    for box_id in box_ids:
        counter += 1
        for i in range(counter, box_ids.__len__()):
            if box_id_differs_by_single_character(box_id, box_ids[i]):
                print('Found one!\nBase_id:  ' + box_id + 'Match_id: ' + box_ids[i])


# returns True if the boxId differs by exactly one character
def box_id_differs_by_single_character(box_id1, box_id2):
    diff_count = 0
    for i in range(0,box_id1.__len__()):
        if box_id1[i] != box_id2[i]:
            diff_count += 1
            if diff_count > 1:
                return False

    if diff_count == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
