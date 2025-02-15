import random


n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Guess a number: "))
    if (a > n):
        print("Lower Number Please")
    elif(a < n):
        print("Higer Number Please")
    elif(a == n):
        break
print(f"You Find the number in {guesses} guesses")