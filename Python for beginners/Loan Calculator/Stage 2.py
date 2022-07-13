import math

def mon_payment(principal,mon_payment):
    months = math.ceil(principal/mon_payment)
    if months == 1:
        print("It will take 1 month to repay the loan")
    else :
        print("It will take "+ str(months) +" months to repay the loan")

def num_of_months(principal,num_of_months):
    payment = math.ceil(principal/num_of_months)
    last_payment = principal - (num_of_months-1)* payment
    if last_payment != payment:
        print("Your monthly payment = " + str(payment) + "and the last payment = " + str(last_payment))
    else :
        print("Your monthly payment = " + str(payment))

n = int(input("Enter the loan principal : \n"))
print("what do you want to calculate?")
type = input('Type "m" for number of monthly payments,\ntype "p" for the monthly payment:\n')
if type == "m":
    m = int(input("Enter the monthly payment:\n"))
    mon_payment(n,m)
elif type == "p":
    p = int(input("Enter the number of months:\n"))
    num_of_months(n,p)
