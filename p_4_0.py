
if __name__ == "__main__":
    with open("input_4_0.txt", "r") as file:
        data = file.read()
    
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (-1, 1),
        (1, -1),
        (-1, -1),
        (1, 1)
    ]
    lines = data.split("\n")
    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            for direction in directions:
                chars = ""
                for magnitude in range(4):
                    new_i, new_j = i + direction[0] * magnitude, j + direction[1] * magnitude
                    if new_i < 0 or new_i >= len(lines) or new_j < 0 or new_j >= len(lines[i]):
                        break
                    chars += lines[new_i][new_j]
                if chars == "XMAS":
                    total += 1
    print(total)
