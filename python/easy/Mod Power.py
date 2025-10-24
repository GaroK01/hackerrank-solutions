if __name__ == '__main__':
  a = int(input())
  b = int(input())
  m = int(input())

  # Alternative is a**b
  first_oper = pow(a,b)
  # The third parameter is for the modulo operation
  # This can be translated to a**b%m
  second_oper = pow(a,b,m)
  
  print(first_oper)
  print(second_oper)
