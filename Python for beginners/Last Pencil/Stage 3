def printpencils(n):
    print("|" * n)

def printturn(Name):
    print(Name + "'s turn:")

n = int(input("How many pencils would you like to use:\n"))
Name = input("Who will be the first (John, Jack):\n")
if Name == "John" :
    i = 1
else :
    i = 0

while n > 0:
    printpencils(n)
    if i % 2 == 1:
        printturn("John")
        i = i + 1
    else :
        printturn("Jack")
        i = i + 1
    m = int(input())
    n = n-m
