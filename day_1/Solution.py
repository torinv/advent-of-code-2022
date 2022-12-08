def greatest_calories(input_file: str) -> int:
    max_cals = 0

    with open(input_file, 'r') as input:
        current_sum = 0
        lines = input.readlines()
        for line in lines:
            # If we hit an empty line
            if line == '\n':
                # Check if we've found the next biggest
                if current_sum > max_cals:
                    max_cals = current_sum

                # Reset to 0 and continue
                current_sum = 0
                continue

            current_sum += int(line)
    return max_cals

def top_three_calories(input_file: str) -> int:
    top_three_cals = 0

    with open(input_file, 'r') as input:
        sums = set()
        current_sum = 0
        lines = input.readlines()
        for line in lines:
            # If we hit an empty line
            if line == '\n':
                # Throw into set and continue
                sums.add(current_sum)
                current_sum = 0
                continue

            current_sum += int(line)

        # Locate the top 3 by maxing and popping sums set
        # NOTE: if there are repeat numbers in the top 3, this will not work (set collision)
        for _ in range(3):
            next_max = max(sums)
            top_three_cals += next_max
            sums.remove(next_max)

    return top_three_cals


if __name__ == '__main__':
    print(greatest_calories('./input.txt'))
    print(top_three_calories('./input.txt'))
