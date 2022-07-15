import argparse
import math


def cal_diff_pay(list):
    principal = list[1]
    period = list[2]
    interest = list[3]
    payment = list[4]
    nom_i = interest/1200
    a1 = principal/period
    y = []
    mon_pay = []
    for i in range(1, int(period)+1):
        k = (principal * (i-1)) / period
        y.append(math.ceil(k))
    for i in y:
        D = a1 + nom_i * (principal - i)
        mon_pay.append(math.ceil(D))
    for i in mon_pay:
        counter = 1
        print("Month " + str(counter) + ": payment is " + str(i))
        counter += counter
    print("Overpayment = " + str(sum(mon_pay) - principal))


def cal_princ(list):
    principal = list[1]
    period = list[2]
    interest = list[3]
    payment = list[4]
    nom_i = interest/1200
    a1 = math.pow(1+nom_i, period)
    a2 = (nom_i * a1) / (a1 - 1)
    principal = payment / a2
    print("Your loan principal = " + str(int(principal)) + "!")
    print("Overpayment = " + str(math.ceil((payment * period) - principal)))


def cal_time(list):
    principal = list[1]
    period = list[2]
    interest = list[3]
    payment = list[4]
    nom_i = interest/1200
    val = payment / (payment - nom_i * principal)
    period = math.ceil(math.log(val, nom_i+1))
    years = period // 12
    months = period % 12
    if months > 0:
        print("It will take " + str(years) + " years and " +
              str(months) + " months to repay this loan!")
    else:
        print("It will take " + str(years) + " years to repay this loan!")
    print("Overpayment = " + str(math.ceil((payment * period) - principal)))


def cal_ann_pay(list):
    principal = list[1]
    period = list[2]
    interest = list[3]
    payment = list[4]
    nom_i = interest/1200
    a1 = math.pow(1+nom_i, period)
    a2 = (nom_i * a1) / (a1 - 1)
    payment = math.ceil(principal * a2)
    print("Your annuity payment = " + str(payment) + "!")
    print("Overpayment = " + str(payment * period - principal))


def check1(list):
    counter1 = 0
    for i in list:
        if i == None:
            counter1 = counter1 + 1
    return counter1


def check2(list):
    counter2 = 0
    for i in range(1, len(list)):
        j = list[i]
        if j != None and j < 0:
            counter2 += 1
    return counter2


parser = argparse.ArgumentParser()

parser.add_argument("-t",
                    "--type", choices=["diff", "annuity"], help="The type of Payments", required=True)

parser.add_argument("-p", "--principal",
                    help="The principle amount", type=float)

parser.add_argument("--periods", help="The time period", type=float)

parser.add_argument("-i", "--interest", help="The intrest Rate", type=float)

parser.add_argument("-d", "--payment",
                    help="The amount need to be paid every month", type=float)

args = parser.parse_args()
req_values = [args.type, args.principal,
              args.periods, args.interest, args.payment]


if check1(req_values) > 1:
    print("Incorrect Paramenters")
elif check2(req_values) > 0:
    print("Incorrect Paramenters")
else:
    if req_values[0] == "diff":
        cal_diff_pay(req_values)
    else:
        if req_values[1] == None:
            cal_princ(req_values)
        elif req_values[2] == None:
            cal_time(req_values)
        elif req_values[4] == None:
            cal_ann_pay(req_values)
