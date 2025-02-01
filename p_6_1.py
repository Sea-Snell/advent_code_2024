
def get_next_state(lines, state):
    direction, position = state
    next_position = (position[0] + direction[0], position[1] + direction[1])
    if next_position[0] < 0 or next_position[0] >= len(lines) or next_position[1] < 0 or next_position[1] >= len(lines[0]):
        return None
    elif lines[next_position[0]][next_position[1]] == '#':
        direction = direction_map[direction]
    else:
        position = next_position
    return (direction, position)

def simulate_loop(lines, state, visited_states):
    has_loop = False
    while True:
        state = get_next_state(lines, state)
        if state is None:
            break
        if state in visited_states:
            has_loop = True
            break
        visited_states.add(state)
    return has_loop

if __name__ == "__main__":
    with open("input_6_1.txt", "r") as file:
        data = file.read()
    lines = list(map(list, data.split('\n')))

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

    state = None
    for i, line in enumerate(lines):
        for indicator in indicator_map:
            if indicator in line:
                direction = indicator_map[indicator]
                position = (i, line.index(indicator))
                state = (direction, position)
                break
        if state is not None:
            break
    
    assert state is not None
    init_state = state

    unique_positions = set([state[1]])
    total = 0
    while True:
        state = get_next_state(lines, state)
        if state is None:
            break
        if state[1] not in unique_positions:
            counterfactual_lines = list(map(list, lines))
            counterfactual_lines[state[1][0]][state[1][1]] = '#'
            if simulate_loop(counterfactual_lines, init_state, set([])):
                total += 1
        unique_positions.add(state[1])
    print(total)
