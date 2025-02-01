
if __name__ == "__main__":
    with open("input_5_1.txt", "r") as file:
        data = file.read()
    
    rules, updates = data.split('\n\n')
    rules = rules.split('\n')
    rules = list(map(lambda x: tuple(map(int, x.split('|'))), rules))
    updates = updates.split('\n')
    updates = list(map(lambda x: tuple(map(int, x.split(','))), updates))
    assert len(rules) == len(set(rules))
    rules = set(rules)
    invalid_update_data = []
    for update in updates:
        assert len(update) % 2 == 1
        valid = True
        relevent_rules = []
        for i in range(len(update)):
            for j in range(len(update)):
                if i == j:
                    continue
                if (update[i], update[j]) in rules:
                    if i > j:
                        valid = False
                    relevent_rules.append((update[i], update[j]))
        if not valid:
            invalid_update_data.append((update, relevent_rules))
    
    total = 0
    for update, relevent_rules in invalid_update_data:
        in_degree = {item: 0 for item in update}
        for rule in relevent_rules:
            in_degree[rule[1]] += 1
        queue = [item for item in update if in_degree[item] == 0]
        result = []
        while queue:
            item = queue.pop(0)
            result.append(item)
            for rule in relevent_rules:
                if rule[0] == item:
                    in_degree[rule[1]] -= 1
                    if in_degree[rule[1]] == 0:
                        queue.append(rule[1])
        total += result[len(result) // 2]
    print(total)
