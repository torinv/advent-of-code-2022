class FileTreeNode:
    dir = False
    name = ''
    size = 0
    subnodes = {}

class FileTree:
    def __init__(self, input: list[str]):
        self._tree = self._build_tree(input)

    def _build_tree(self, input: list[str]) -> FileTreeNode:
        root = FileTreeNode
        root.name = '/'
        cursor = root
        self._build_recursive(cursor, 2, input)
        return root

    def _build_recursive(self, node: FileTreeNode, current_line: int, input: list[str]):
        # Fill out current node's tree
        while not input[current_line].startswith('$'):
            split = input[current_line].strip().split()
            # Create a new node
            new_node = FileTreeNode()

            # Directory case
            if split[0] == 'dir':
                new_node.dir = True
            # File case
            else:
                new_node.size = int(split[0])

            # Add node's name and append to current node's dict
            new_node.name = split[1]
            node.subnodes[new_node.name] = new_node

            # Advance
            current_line += 1

        split = input[current_line].strip().split()
        # Base case if we cd up
        if split[-1] == '..':
            return
        # Recurse into next dir
        else:
            self._build_recursive(node.subnodes[split[-1]], current_line + 2, input)


if __name__ == '__main__':
    with open('./day_7/input.txt', 'r') as input:
        lines = input.readlines()
        tree = FileTree(lines)
