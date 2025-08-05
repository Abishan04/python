units = input("Enter Your Used Water level(litre) :")
unit = float(units)
amount = 0.0

if unit >= 0:
    if unit <= 1000:
        amount=500
        print(amount)
    elif unit <= 3000:
        amount = (unit - 1000)*3
        print(amount)
else:
    print("Invalid Unit Number")