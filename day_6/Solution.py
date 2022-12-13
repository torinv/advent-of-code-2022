def find_start_marker(input: str, marker_len: int) -> int:
    for end_char in range(marker_len, len(input)):
        # Stop if we get a unique sequence
        check_set = set(input[end_char - marker_len : end_char])
        if len(check_set) == marker_len:
            return end_char


if __name__ == '__main__':
    with open('./input.txt', 'r') as input:
        line = input.readline()
        print(find_start_marker(line, 4))
        print(find_start_marker(line, 14))
