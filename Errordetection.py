broj_otvorenih_zagrada = 0
broj_zatvorenih_zagrada = 0

with open("sum_func.py") as file:
    for line in file:
        for char in line:
            if char == '[':
                broj_otvorenih_zagrada += 1
            elif char == ']':
                broj_zatvorenih_zagrada += 1

if broj_otvorenih_zagrada != broj_zatvorenih_zagrada:
    print("Doslo je do greske proverite da li su sve zagrade pravilno napisane.")
    exit(1)