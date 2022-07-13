def printpencils(n):
    print("|" * n)

def printfirst(Name):
    print(Name + " is going first")

n = int(input("How many pencils would you like to use:\n"))
Name = input("Who will be the first (John, Jack):\n")

printpencils(n)
printfirst(Name)    
