units = input("Enter Your Used Water level(litre) :")
unit = float(units)
amount = 0.0

if unit > 0:
    if unit>=0 and unit <= 1000:
        amount=500
    elif unit>1000 and unit <= 3000:
        amount = 500 + (unit - 1000)*3
    elif unit>3000 and unit <= 10000:
        amount = 500 + 2000*3 + (unit - 3000)*5
    else:
        amount = 500 + 2000*3 + 7000*10 + (unit - 10000)*10
    print(f"Your Water Bill is  = {amount}")
else:
    print("Invalid Unit Number")