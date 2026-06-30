# Program to print the letter K using logic

n = 7

for i in range(n):
    for j in range(n):
        if j == 0 or i + j == 3 or i - j == 3:
            print("*", end="")
        else:
            print(" ", end="")
    print()