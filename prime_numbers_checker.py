#Write your code below this line 👇
def prime_checker(number):
    count = 0
    for divisor in range(1, number+1):
        if number%divisor == 0:
            count+= 1
    if not count == 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")
    





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
