def solve_equation(target, numbers):
  """
    Checks if a given target can be reached using the provided numbers and +, * operators.
    
    Args:
      target: The target value for the equation.
      numbers: A list of numbers to be used in the equation.
    
    Returns:
      True if the target can be reached, False otherwise.
  """
  def calculate(nums, ops):
      result = nums[0]
      for i in range(len(ops)):
          if ops[i] == '+':
              result += nums[i+1]
          elif ops[i] == '*':
              result *= nums[i+1]
      return result
  
  num_ops = len(numbers) - 1
  
  for i in range(2**num_ops):
      ops = []
      temp = i
      for _ in range(num_ops):
           if temp % 2 == 0:
               ops.append('+')
           else:
               ops.append('*')
           temp //= 2
      
      if calculate(numbers, ops) == target:
           return True
  
  return False
  

def main():
  """
    Reads equations from the input file, determines which can be solved,
    and calculates their total calibration result.
  """
  total_calibration_result = 0
  
  with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(":")
        target = int(parts[0])
        numbers = [int(num) for num in parts[1].split()]
        
        if solve_equation(target, numbers):
             total_calibration_result += target

  print("Total calibration result:", total_calibration_result)

if __name__ == "__main__":
    main()
