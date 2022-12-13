from collections import deque

class CrateStacks(object):
    def __init__(self, input: "list[str]"):
        self.stacks = self._read_stacks(input)
        self.instructions = self._read_instructions(input)

    @staticmethod
    def _read_stacks(input: "list[str]") -> "list[deque]":
        stacks = [deque() for _ in range(9)]
        for line in input:
            # Stop when we get to end of crates
            if not line.startswith('['):
                break

            # Just grab the stuff between the end brackets
            trimmed = line.strip()[1 : -1]
            print(trimmed)

            # Read each crate and push into stack
            for stack_idx, char_num in enumerate(range(0, len(trimmed), 4)):
                if trimmed[char_num] == ' ':
                    continue
                stacks[stack_idx].appendleft(trimmed[char_num])

        return stacks

    @staticmethod
    def _read_instructions(input: "list[str]") -> "list[list[int]]":
        instructions = []
        found_instructions = False
        for line in input:
            if line == '\n':
                found_instructions = True

            if not found_instructions:
                continue

            split = line.split()
            line = [int(split[1]), int(split[3]), int(split[5])]


if __name__ == '__main__':
    with open('./input.txt', 'r') as input:
        lines = input.readlines()
        stacks = CrateStacks(lines)
        print(stacks.stacks)