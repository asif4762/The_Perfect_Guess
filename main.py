import random


n = random.randint(1, 100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess a number: "))
    if (a > n):
        print("Lower Number Please")
    elif(a < n):
        print("Higer Number Please")
    guesses += 1
print(f"You Find the number in {guesses} guesses")