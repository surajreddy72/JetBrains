def printpencils(n):
    print("|" * n)

def printturn(Name):
    print(Name + "'s turn!")


n = input("How many pencils would you like to use:\n")

while n.isnumeric() != True :
        print("The number of pencils should be numeric")
        n = input()
while int(n) <= 0 :
        print("The number of pencils should be positive")
        n = input()
        while n.isnumeric() != True :
            print("The number of pencils should be numeric")
            n = input()

Name = input("Who will be the first (John, Jack):\n")
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
   

while int(n) > 0:
    printpencils(int(n))
    if i % 2 == 1:
        printturn("John")
        i = i + 1
    else :
        printturn("Jack")
        i = i + 1
    m = input()
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
    n = int(n)-int(m)

if i % 2 == 1:
        print("John Won!")
else :
    print("Jack Won!")
