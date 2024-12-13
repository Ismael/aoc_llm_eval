def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    rules = []
    updates = []
    parsing_rules = True
    for line in lines:
        if line.strip() == '':
            parsing_rules = False
            continue
        if parsing_rules:
            x, y = map(int, line.strip().split('|'))
            rules.append((x, y))
        else:
            updates.append(list(map(int, line.strip().split(','))))
    return rules, updates

def is_correctly_ordered(update, rules):
    for x, y in rules:
        if x in update and y in update and update.index(y) < update.index(x):
            return False
    return True

def middle_page(update):
    return update[len(update) // 2]

def main():
    rules, updates = read_input('input.txt')
    correctly_ordered_updates = [update for update in updates if is_correctly_ordered(update, rules)]
    middle_pages = [middle_page(update) for update in correctly_ordered_updates]
    print(sum(middle_pages))

if __name__ == '__main__':
    main()