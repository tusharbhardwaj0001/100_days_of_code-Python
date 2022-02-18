year = input("Which year do you want to check?")  #this line produce error 
#year = int(input("Which year do you want to check?"))  #this is correct line

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
