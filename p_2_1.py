

def process_report(report):
    sign = report[-1] - report[0]
    sign /= max(abs(sign), 1)
    did_skip, curr = False, report[0]
    for item in report[1:]:
        delta = item - curr
        if not (delta * sign > 0 and abs(delta) >= 1 and abs(delta) <= 3):
            if did_skip:
                return False
            else:
                did_skip = True
        else:
            curr = item
    return True

if __name__ == "__main__":
    with open("input_2_1.txt", "r") as f:
        reports = [list(map(int, line.split(" "))) for line in f]
    
    count = 0
    for report in reports:
        count += process_report(report) or process_report(report[::-1])
    print(count)
