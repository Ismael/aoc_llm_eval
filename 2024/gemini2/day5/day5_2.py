def is_valid_order(order, rules):
  """Checks if a page order is valid according to the given rules."""
  for i in range(len(order)):
    for j in range(i + 1, len(order)):
      if (order[j], order[i]) in rules:
        return False
  return True


def get_valid_order(pages, rules):
  """Finds a valid order of pages based on the given rules."""

  def get_next_pages(current_pages):
      next_pages = []
      for p in pages:
          all_precs_present = True
          for rule in rules:
                # if rule[1] ==p and rule[0] is not in current_pages:
            if rule[1] == p and rule[0] in pages and rule[0] not in current_pages:
                all_precs_present = False
                break

          if all_precs_present and p not in current_pages:
              next_pages.append(p)
      return next_pages
           
  
  result = []
  current_pages = []
  while(len(current_pages)< len(pages)):
    next_pages =get_next_pages(current_pages)
    if len(next_pages) ==0:
        return None
    result.append(next_pages[0])
    current_pages.append(next_pages[0])
    
    
  return result
          


def solve():
  """Solves part two of the puzzle."""
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
    if not is_valid_order(pages, rules):
      ordered_pages = get_valid_order(pages,rules)
      middle_index = len(ordered_pages) // 2
      total_middle_page_number += ordered_pages[middle_index]


  print(total_middle_page_number)

if __name__ == "__main__":
  solve()
