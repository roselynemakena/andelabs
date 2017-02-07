def fizz_buzz(value):
  if value%3 == 0:
    if value%5 ==0:
      return 'FizzBuzz'
    else:
      return 'Fizz'
    
  if value % 5 == 0:
     if value%3 ==0:
      return 'FizzBuzz'
     else:
      return 'Buzz'
    
  if value % 15 != 0:
    return value

    
    
  