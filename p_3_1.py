import re

if __name__ == "__main__":
    with open("input_3_1.txt", "r") as file:
        data = file.read()
    
    mul_regex_str = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_regex_str = r"do\(\)"
    dont_regex_str = r"don\'t\(\)"
    combined_regex_str = f"({mul_regex_str})|({do_regex_str})|({dont_regex_str})"
    matches = re.findall(combined_regex_str, data)
    total, enabled = 0, True
    for mul_match, num1, num2, do_match, dont_match in matches:
        if do_match != '':
            enabled = True
        elif dont_match != '':
            enabled = False
        else:
            if enabled:
                total += int(num1) * int(num2)
    print(total)
