import re

if __name__ == "__main__":
    with open("input_3_0.txt", "r") as file:
        data = file.read()
    
    regex_str = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(regex_str, data)
    total = 0
    for match in matches:
        total += int(match[0]) * int(match[1])
    print(total)
