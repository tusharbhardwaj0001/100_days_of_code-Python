import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(names)
n = len(names)
print(n)
i = random.randint(0,n-1)
print(i)
print(names[i] +" is going to buy the meal today!")
