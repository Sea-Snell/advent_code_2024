
if __name__ == "__main__":
    with open("input_2_0.txt", "r") as f:
        reports = [list(map(int, line.split(" "))) for line in f]
    
    count = 0
    for report in reports:
        sign = report[-1] - report[0]
        sign /= max(abs(sign), 1)
        valid = True
        for a, b in zip(report[:-1], report[1:]):
            if not ((b - a) * sign > 0 and abs(b - a) >= 1 and abs(b - a) <= 3):
                valid = False
        count += valid
    print(count)


