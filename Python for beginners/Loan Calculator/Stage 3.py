import math
from re import A

def mon_payment(principal, mon_payment):
    months = math.ceil(principal/mon_payment)
    if months == 1:
        print("It will take 1 month to repay the loan")
    else:
        print("It will take " + str(months) + " months to repay the loan")


def num_of_months(principal, num_of_months):
    payment = math.ceil(principal/num_of_months)
    last_payment = principal - (num_of_months-1) * payment
    if last_payment != payment:
        print("Your monthly payment = " + str(payment) +
              "and the last payment = " + str(last_payment))
    else:
        print("Your monthly payment = " + str(payment))

def ifn():
    p = float(input("Enter the loan principal:"))
    m = float(input("Enter the monthly payment:"))
    i = float(input("Enter the loan intrest:"))
    nom_i = i / 1200
    val = m / (m-nom_i*p)
    num_of_payments = math.ceil(math.log(val, nom_i+1))
    years = num_of_payments // 12
    months = num_of_payments % 12
    print("It will take " + str(years) + " years and " + str(months) + " months to repay this loan!")

def ifa():
    p = float(input("Enter the loan principal:"))
    n = float(input("Enter the number of periods:"))
    i = float(input("Enter the loan intrest:"))
    nom_i = i / 1200
    a1 = math.pow(1+nom_i, n)
    a2 = (nom_i * a1) / (a1 - 1)
    A = p * a2
    print("Your monthly payment = " + str(math.ceil(A)) + "!")

def ifp():
    A = float(input("Enter the annuity payment:"))
    n = float(input("Enter the number of periods:"))
    i = float(input("Enter the loan intrest:"))
    nom_i = i / 1200
    a1 = math.pow(1+nom_i, n)
    a2 = (nom_i * a1) / (a1 - 1)
    p = A / a2
    print("Your loan principal = " + str(math.ceil(p)))
   


print("what do you want to calculate?")
type = input('Type "n" for number of monthly payments,\ntype "a" for annuity monthly payment amount,\ntype "p" for the loan principal:\n')
if type == "n":
    ifn()
elif type == "a":
    ifa()
elif type == "p":
    ifp()
