def calcInterest(amount, time):
    if time > 60:
        rate = 15.5
    elif time == 60:
        rate = 15
    elif time >= 12:
        rate = 13
    elif time >= 6:
        rate = 12.5
    elif time >= 3:
        rate = 12
    else:
        rate = 0
    interest = (amount * rate * (time / 12)) / 100
    return interest
    
amount = float(input("Enter amount: "))
time = int(input("Enter duration in months: "))
result = calInterest(amount, time)
print(f"Interest for Rs.{amount:.2f} over {time} months is Rs.{result:.2f}")