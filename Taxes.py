wage = 1500
allowances = 2

def FIT(wage, allowances):
    deductions = allowances * 153.8
    taxableWage = wage - deductions
    base = 1040
    taxableAtRate = taxableWage - base
    rate = 0.15
    rateTax = taxableAtRate * rate
    add = 70.9
    FIT = rateTax + add
    return FIT

def SS(wage):
    SS = wage * 0.062
    return SS

def Medicare(wage):
    Medicare = wage * 0.0145
    return Medicare

def netPay(wage, FIT, SS, Medicare):
    netPay = wage - (FIT + SS + Medicare)
    return netPay

FIT = FIT(wage, allowances)
SS = SS(wage)
Medicare = Medicare(wage)
netPay = netPay(wage, FIT, SS, Medicare)

print "FIT is " + str(FIT)
print "Social Security is " + str(SS)
print "Medicare is " + str(Medicare)
print "Net Pay is " + str(netPay)