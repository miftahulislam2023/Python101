""" bill = 400
vat  = 2.5/100 # % -> 1/100
total = bill + bill * vat
print(total) """

def vatCalculate(bill):
    vat  = 2.5/100 # % -> 1/100
    total = bill + bill * vat
    print(total)

vatCalculate(400)
vatCalculate(1000)