def _get_priority(char: str) -> int:
    # Lowercase
    if ord(char) > ord('Z'):
        return ord(char) - 96
    # Uppercase
    else:
        return ord(char) - 64 + 26
 
def total_priority(input: "list[str]") -> int:
    total = 0
    for rucksack in input:
        # Throw items into sets and get intersection
        items_1 = set()
        items_2 = set()
        for item_num, item in enumerate(rucksack.strip()):
            if item_num < len(rucksack) // 2:
                items_1.add(item)
            else:
                items_2.add(item)
        overlap = items_1.intersection(items_2).pop()

        # Add priority to total
        total += _get_priority(overlap)
    return total

def badges_priority(input: "list[str]") -> int:
    total_badges = 0
    for rucksack_num in range(0, len(input), 3):
        # Catalog items in sets
        items = [set() for _ in range(3)]
        for idx, rucksack in enumerate(input[rucksack_num : rucksack_num + 3]):
            for item in rucksack.strip():
                items[idx].add(item)

        # Find overlapping item
        intersection = items[0].intersection(items[1]).intersection(items[2])
        total_badges += _get_priority(intersection.pop())
    return total_badges


if __name__ == '__main__':
    with open('input.txt', 'r') as input:
        lines = input.readlines()
        print(total_priority(lines))
        print(badges_priority(lines))
