"""
Problem : Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

Example Input:
weight = 80
height = 1.75

Example Output:
80 ÷ (1.75 x 1.75) = 26.122448979591837
26

Code:
"""
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = float(weight) // (float(height) ** 2)
print(int(BMI))
