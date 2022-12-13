from collections import deque

class CraneInstruction(object):
    def __init__(self, instruction: list):
        self.num_crates = instruction[0]
        self.start_stack = instruction[1]
        self.end_stack = instruction[2]

class CrateStacks:
    def __init__(self, input: list[str]):
        self._stacks = self._read_stacks(input)
        self._instructions = self._read_instructions(input)

    @staticmethod
    def _read_stacks(input: list[str]) -> list[deque]:
        stacks = [deque() for _ in range(9)]
        for line in input:
            # Stop when we get to end of crates
            if not line.startswith('['):
                break

            # Just grab the stuff between the end brackets
            trimmed = line.strip()[1 : -1]

            # Read each crate and push into stack
            for stack_idx, char_num in enumerate(range(0, len(trimmed), 4)):
                if trimmed[char_num] == ' ':
                    continue
                stacks[stack_idx].appendleft(trimmed[char_num])

        return stacks

    @staticmethod
    def _read_instructions(input: list[str]) -> list[CraneInstruction]:
        instructions = []
        found_instructions = False
        for line in input:
            # Read forward until the blank line
            if line == '\n':
                found_instructions = True
                continue

            if not found_instructions:
                continue
            
            # Emplace CraneInstructions for each line after
            split = line.split()
            instruction = CraneInstruction([int(split[1]), int(split[3]), int(split[5].strip())])
            instructions.append(instruction)
        return instructions

    @staticmethod
    def get_top_crates(stacks: list[deque]) -> str:
        out = ''
        for stack in stacks:
            out += stack[-1]
        return out

    def get_top_crates_9000(self) -> str:
        stacks = [stack.copy() for stack in self._stacks]

        # Execute instructions
        for instruction in self._instructions:
            for _ in range(instruction.num_crates):
                stacks[instruction.end_stack - 1].append(
                    stacks[instruction.start_stack - 1].pop()
                )

        # Return top crates
        return self.get_top_crates(stacks)

    def get_top_crates_9001(self) -> str:
        stacks = [stack.copy() for stack in self._stacks]
        print(stacks)

        # Execute instructions
        for instruction in self._instructions:
            temp = deque()
            for _ in range(instruction.num_crates):
                if len(stacks[instruction.start_stack - 1]) != 0:
                    temp.appendleft(stacks[instruction.start_stack - 1].pop())

            for crate in temp:
                stacks[instruction.end_stack - 1].append(crate)

        # Return top crates
        return self.get_top_crates(stacks)



if __name__ == '__main__':
    with open('./input.txt', 'r') as input:
        lines = input.readlines()

        stacks = CrateStacks(lines)
        # Part 1
        print(stacks.get_top_crates_9000())

        # Part 2
        print(stacks.get_top_crates_9001())
