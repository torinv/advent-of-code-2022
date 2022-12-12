from collections import deque

class CrateConfig(object):
    def __init__(self, input: "list[str]"):
        self.stacks = _read_stacks(input)
        self.instructions = _read_instructions(input)

        @staticmethod
        def _read_stacks(input: "list[str]") -> "list[deque]":
            for line in input: pass

        @staticmethod
        def _read_instructions(input: "list[str]") -> "list[list[int]]":
            pass
