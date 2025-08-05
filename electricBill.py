units = input("Enter Your Units :")
unit = float(units)
amount = 0.0

if unit > 0:
    if unit <= 90:
        amount = unit*7
    elif unit <= 150:
        amount = 90*7 + (unit - 90)*10
    elif unit <= 300:
        amount = 90*7 + 60*10 + (unit - 150)*15
    else:
        basic = 90*7 + 60*10 + 150*15
        amount = basic + (unit - 300)*15
        amount *= 1.03
    print(f"Your Bill Amount is = {amount}")
else:
    print("Invalid Unit Number")