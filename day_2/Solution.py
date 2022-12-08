WIN = 6

def total_score(input_file: str) -> int:
    total_score = 0
    with open(input_file, 'r') as input:
        lines = input.readlines()

        for line in lines:
            split = line.split()
            first = split[0] - 40 # Pull ABC back to ord 123
            second = split[1] - 17 - 40 # Pull XYZ back to ABC then back to ord 123
            # print(first)
            # print(second)

            total_score += ord(second)
            # Draw condition
            if first == second:
                total_score += WIN / 2
            # Win condition
            elif first < second or (first == 3 and second == 1):
                total_score += WIN

    return total_score


if __name__ == '__main__':
    print(total_score('./input.txt'))
