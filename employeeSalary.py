months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
salaries = [50000, 52000, 48000, 60000, 75000, 82000, 91000, 120000, 130000, 150000, 170000, 200000]
taxes = [0,0,0,0,0,0,0,0,0,0,0,0]
total = 0
totaltax = 0

print(f"{'':>10}{'Salary':>10} {'Tax':>10} {'Net Salary':>15}")

i = 0
while i < len(salaries):
    salary = salaries[i]
    
    if 0 < salary < 50000:
        tax = salary * 0.03
    elif salary < 100000:
        tax = salary * 0.05
    elif salary < 300000:
        tax = salary * 0.08
    else:
        tax = salary * 0.10
    taxes[i] = tax
    net_salary = salary - taxes[i]
    total += salary
    totaltax += taxes[i]

    print(f"{months[i]:<10} {salary:>10.2f} {taxes[i]:>10.2f} {net_salary:>15.2f}")
    i += 1
print("-"*48)
print(f"{"Total":<10}{total:>10.2f} {totaltax:>10.2f} {(total - totaltax):>15.2f}")
print("-"*48)