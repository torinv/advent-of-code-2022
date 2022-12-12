def _get_ranges_from_line(line: str) -> list:
    elf1, elf2 = line.strip().split(',')
    elf1_range = [int(num) for num in elf1.split('-')]
    elf2_range = [int(num) for num in elf2.split('-')]
    return elf1_range, elf2_range

def count_fully_contained(input: "list[str]") -> int:
    total = 0
    for line in input:
        elf1_range, elf2_range = _get_ranges_from_line(line)

        if (elf1_range[0] >= elf2_range[0] and elf1_range[1] <= elf2_range[1]) \
            or (elf2_range[0] >= elf1_range[0] and elf2_range[1] <= elf1_range[1]):
                total += 1

    return total

def count_overlaps(input: "list[str]") -> int:
    total = 0
    for line in input:
        elf1_range, elf2_range = _get_ranges_from_line(line)
        elf1_set = {num for num in range(elf1_range[0], elf1_range[1] + 1)}
        elf2_set = {num for num in range(elf2_range[0], elf2_range[1] + 1)}
        if len(elf1_set.intersection(elf2_set)) > 0:
            total += 1

    return total


if __name__ == '__main__':
    with open('./input.txt', 'r') as input:
        lines = input.readlines()
        # Part 1
        print(count_fully_contained(lines))
        # Part 2
        print(count_overlaps(lines))
