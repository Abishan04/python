subjects = [1, 2, 3, 4, 5]
j = 0

while j < len(subjects):
    answer = input(f"Do you want to change subject {subjects[j]} name? (y/n)\n").strip().lower()
    
    if answer == "y":
        name = input(f"Change subject {subjects[j]} name: ").strip()
        subjects[j] = name
    elif answer == "n":
        subjects[j] = subjects[j]
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue  
    
    j += 1

print(subjects)