def is_valid_order(order, rules):
  """Checks if a page order is valid according to the given rules."""
  for i in range(len(order)):
    for j in range(i + 1, len(order)):
      if (order[j], order[i]) in rules:
        return False
  return True


def solve():
  """Solves the puzzle."""
  with open("input.txt", "r") as f:
    data = f.read().split("\n\n")
    rule_lines = data[0].splitlines()
    update_lines = data[1].splitlines()

  rules = set()
  for line in rule_lines:
    parts = line.split("|")
    rules.add((int(parts[0]), int(parts[1])))

  total_middle_page_number = 0
  for line in update_lines:
    pages = [int(x) for x in line.split(",")]
    if is_valid_order(pages, rules):
      middle_index = len(pages) // 2
      total_middle_page_number += pages[middle_index]
  print(total_middle_page_number)


if __name__ == "__main__":
  solve()

