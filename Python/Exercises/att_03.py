sex = str(input("Enter your sex: "))

while sex not in ['M', 'F']:
    sex = str(input("Invalid input. Please enter 'M' or 'F': "))

if sex == 'M':
    print("Homem")
if sex == 'F':
    print("Mulher")