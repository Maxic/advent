def main():
    with open("input.txt", "r+") as file:
        tree = file.readlines()[0]
    split_tree = [int(i) for i in tree.split(' ')]
    total, _ = parse_tree(split_tree)
    print(total)
    # example: 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2


def parse_tree(tree):
    children_quantity = tree[0]
    metadata_quantity = tree[1]

    if children_quantity == 0:
        metadata_sum = sum(tree[2:2+metadata_quantity])
        return metadata_sum, tree[2+metadata_quantity:]

    metadata_sum = 0
    rest = tree[2:]
    for child in range(1, children_quantity+1):
        metadata_count, rest = parse_tree(tree[2:])
        metadata_sum += metadata_count
    metadata_sum += sum(rest[:metadata_quantity])
    return metadata_sum, rest[metadata_quantity:]


if __name__ == '__main__':
    main()
