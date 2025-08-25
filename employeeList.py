salaries = [50000, 52000, 48000, 60000, 75000, 82000, 91000, 120000, 130000, 150000, 170000, 200000]
months = ["January","February","March","April","May","June","July","August","September","October","November","December" ]
total = 0
totaltax = 0

print(f"{'Month':^10} {'Salary':>10} {'Tax':>10} {'After Tax':>15}")

for salary in salaries:
    total += salary

    if 0 < salary < 50000:
        tax = salary * 0.03
    elif salary < 100000:
        tax = salary * 0.05
    elif salary < 300000:
        tax = salary * 0.08
    else:
        tax = salary * 0.10

    totaltax += tax
    net_salary = salary - tax

    print(f"{months[salaries.index(salary)]:^10}{salary:10.2f} {tax:10.2f} {net_salary:15.2f}")

# Print summary
print("\n --- Summary ---")
print(f"Total Salary: {total:.2f}")
print(f"Total Tax: {totaltax:.2f}")
print(f"Net Total: {total - totaltax:.2f}")