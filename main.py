print("hello dice roller")
name = input("enter your name: ")
dice = int(input("enter how many dice rolles you want: "))
print(f"hello {name}, you are using {dice} amount of dice rolles")
num = int(input("enter a number: "))
import random
    
random_number = random.randint(1, 6)
print("random number:", random_number)
for i in range(6):
    print("iteration",i)

if num > 3:
    print("the number is bigger than 3")
elif num < 3:
    print("the number is smaller than 3")
else:
    print("number is 3")
