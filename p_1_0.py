
if __name__ == "__main__":
    with open("input_1_0.txt", "r") as f:
        input_data = f.read().strip()

    lines = list(map(lambda x: tuple(map(int, x.split("   "))), input_data.split("\n")))
    l1, l2 = list(zip(*lines))
    l1, l2 = sorted(l1), sorted(l2)
    distances = list(map(lambda x: abs(x[0] - x[1]), zip(l1, l2)))
    print(sum(distances))
