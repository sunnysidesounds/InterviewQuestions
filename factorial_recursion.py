
# Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop

#function findFactorialIterative(number) {
#  //code here
#  return answer;
#}

def find_factorial_recursive(number):
  if number == 0 or number == 1:
    return 1
  else:
    return number * find_factorial_recursive(number - 1)

  
def find_factorial_iterative(number):
  total = 1
  for i in range(1, number+1):    
    total = total * i

  return total





