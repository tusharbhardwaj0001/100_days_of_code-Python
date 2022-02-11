#Write your code below this line 👇
def paint_calc(height,width,cover):
  area = int(height) * int(width)
  no_of_cans = area/int(cover)
  n = area//int(cover)
  if no_of_cans > n:
    print (int(no_of_cans) + 1)
  else :
    print (int(no_of_cans))


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


