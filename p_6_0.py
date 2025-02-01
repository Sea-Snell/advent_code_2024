

if __name__ == "__main__":
    with open("input_6_0.txt", "r") as file:
        data = file.read()
    lines = data.split('\n')

    direction_map = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
    }
    indicator_map = {
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0),
    }

    direction, position = None, None
    for i, line in enumerate(lines):
        for indicator in indicator_map:
            if indicator in line:
                direction = indicator_map[indicator]
                position = (i, line.index(indicator))
                break
        if direction is not None:
            break
    
    assert (direction is not None) and (position is not None)

    unique_positions = set([position])
    while True:
        next_position = (position[0] + direction[0], position[1] + direction[1])
        if next_position[0] < 0 or next_position[0] >= len(lines) or next_position[1] < 0 or next_position[1] >= len(lines[0]):
            break
        elif lines[next_position[0]][next_position[1]] == '#':
            direction = direction_map[direction]
        else:
            position = next_position
            unique_positions.add(position)
    
    print(len(unique_positions))