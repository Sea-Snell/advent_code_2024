

if __name__ == "__main__":
    with open("input_5_0.txt", "r") as file:
        data = file.read()
    
    rules, updates = data.split('\n\n')
    rules = rules.split('\n')
    rules = list(map(lambda x: tuple(map(int, x.split('|'))), rules))
    updates = updates.split('\n')
    updates = list(map(lambda x: tuple(map(int, x.split(','))), updates))
    assert len(rules) == len(set(rules))
    rules = set(rules)
    total = 0
    for update in updates:
        assert len(update) % 2 == 1
        valid = True
        for i in range(len(update)):
            for j in range(len(update)):
                if i == j:
                    continue
                if (update[i], update[j]) in rules:
                    if i > j:
                        valid = False
                        break
            if not valid:
                break
        if valid:
            total += update[len(update) // 2]
    print(total)