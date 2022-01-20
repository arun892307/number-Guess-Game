import random
n=random.randint(1,100)
count=0
print("welcome to number guess game Code by arun kumar:\n")
print("your goal is between 1 to 100:")
while(1):
    num=int(input("Guess a number:"))
    if num>n:
        print("It is grater than the real number:")
        count=count+1
        continue
    elif num<n:
        print("It is less than the real number")
        count=count+1
        continue
    elif num==n:
        break

print("congratulation you win the game :")
print("you attempt",count,"steps")