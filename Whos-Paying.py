# Split string method
import random 

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
long = len(names)


n = random.randint(0, long-1)
payer = random.choice(names)
print(f"{payer} is going to buy the meal today!")
