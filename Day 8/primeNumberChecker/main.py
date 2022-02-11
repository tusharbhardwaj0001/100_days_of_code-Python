#Write your code below this line 👇
def prime_checker(number):
  flag = True
  n = int(int(number)/2)
  for i in range(2,n):
    if number%i == 0:
      print("It's not a prime number.")
      flag = False
      break
  if flag:
    print ("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



