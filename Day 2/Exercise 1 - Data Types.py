"""
Problem : Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

Example input :
39

Example Output :
3 + 9 = 12
12

Code:
"""
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
digit_number = int(two_digit_number)
sum = digit_number%10 + digit_number//10
print(sum)
