# Part 1
# A X = rock
# B Y = paper
# C Z = scissors

# Part 2
# X = loss
# Y = draw
# Z = win

WIN = 6

def total_score(input: "list[str]") -> int:
    total_score = 0
    for line in input:
        split = line.split()
        theirs = ord(split[0]) - 64 # Pull ABC back to ord 123
        mine = ord(split[1]) - 23 - 64 # Pull XYZ back to ABC then back to ord 123

        total_score += mine
        # Draw condition
        if theirs == mine:
            total_score += WIN // 2
        # Win condition
        elif theirs % 3 == mine - 1:
            total_score += WIN

    return total_score

def process_outcomes(input: "list[str]") -> "list[str]":
    out = []
    for line in input:
        theirs, condition = line.split()

        mine = ''
        lowered = ord(theirs) - 64
        # Loss
        if condition == 'X':
            mine = lowered - 1 if lowered > 1 else 3
        # Draw
        elif condition == 'Y':
            mine = lowered 
        # Win
        elif condition == 'Z':
            mine = lowered + 1 if lowered < 3 else 1

        # Convert to XYZ
        mine = chr(mine + 23 + 64)
        out.append(' '.join([theirs, mine]))
    return out


if __name__ == '__main__':
    with open('./input.txt', 'r') as input:
        lines = input.readlines()

        # Part 1
        print(total_score(lines))

        # Part 2
        processed_lines = process_outcomes(lines)
        print(total_score(processed_lines))
