
salaries = [10000, 23495, 244403]
total = 0
totaltax = 0

for salary in salaries:
    total += salary

    if salary < 50000:
        tax = salary * 0.03
    elif salary < 100000:
        tax = salary * 0.05
    elif salary < 300000:
        tax = salary * 0.08
    else:
        tax = salary * 0.10

    totaltax += tax
    net_salary = salary - tax

    print(f"Salary: {salary:.2f}, Tax: {tax:.2f}, After Tax: {net_salary:.2f}")

print("\n--- Summary ---")
print(f"Total Salary: {total:.2f}")
print(f"Total Tax: {totaltax:.2f}")
print(f"Net Total: {total - totaltax:.2f}")



