from collections import Counter

if __name__ == "__main__":
    with open("input_1_1.txt", "r") as f:
        input_data = f.read().strip()

    lines = list(map(lambda x: tuple(map(int, x.split("   "))), input_data.split("\n")))
    l1, l2 = list(zip(*lines))

    l2_counts = Counter(l2)
    total = 0
    for item in l1:
        total += item * l2_counts[item]
    print(total)
