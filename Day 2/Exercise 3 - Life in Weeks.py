"""
Problem : Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
        It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Example input:
56

Example Output:
You have 12410 days, 1768 weeks, and 408 months left.

Code:
"""
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
yearsLeft = 90 - int(age)
month = yearsLeft*12
weeks = yearsLeft*52
days = yearsLeft *365

print(f"You have {days} days, {weeks} weeks, and {month} months left.")



