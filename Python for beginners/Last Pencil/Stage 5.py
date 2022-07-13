import random

def printpencils(n):
    print("|" * n)

def printturn(Name):
    print(Name + "'s turn!")
    
def order(Name):
    if Name == "John" :
        i = 1
    elif Name == "Jack" :
        i = 0
    else :
        while (Name != "John") or (Name != "Jack") :
            print("Choose between 'John' and 'Jack'")
            Name = input()
            if Name == "John" :
                i = 1
                break
            elif Name == "Jack" :
                i = 0
                break
    return i
    
def checkpencils(n):
    while n.isnumeric() != True :
        print("The number of pencils should be numeric")
        n = input()
    while int(n) <= 0 :
        print("The number of pencils should be positive")
        n = input()
        while n.isnumeric() != True :
            print("The number of pencils should be numeric")
            n = input()
    return n
    
def Game(n,i):
    while int(n) > 0:
        printpencils(int(n))
        if i % 2 == 1:
            printturn("John")
            i = i + 1
            m = input()
            m = checkinput(n,m)
        else :
            printturn("Jack")
            i = i + 1
            m = bot_choice(int(n))
            print(m)
        n = int(n)-int(m)
    return i
    
def checkinput(n,m):
    while m.isnumeric() != True :
        print("Possible values: '1', '2' or '3'")
        m = input()
    while int(m) <= 0 or int(m) > 3 :
        print("Possible values: '1', '2' or '3'")
        m = input()
        while m.isnumeric() != True :
            print("Possible values: '1', '2' or '3'")
            m = input()
    while int(m) > int(n):
        print("Too many pencils were taken")
        m = input()
    return m
    
def Win(i):
    if i % 2 == 1:
        print("John Won!")
    else :
        print("Jack Won!")

# Stage 5
def bot_choice(n):
    if n in range(2,n+1,4):
        m = 1
    elif n in range(3,n+1,4):
        m = 2
    elif n in range(4,n+1,4):
        m = 3
    elif n == 1:
        m = 1
    else:
        m = random.randint(1,3)
    return m
   
    
n = input("How many pencils would you like to use:\n")
n = checkpencils(n)
Name = input("Who will be the first (John, Jack):\n")
i = order(Name)
Win(Game(n,i))
