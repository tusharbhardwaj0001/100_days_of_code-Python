for number in range(1, 101): 
  if number % 3 == 0 or number % 5 == 0:  #this line produce error ,in this line and should be instead of or
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
  
