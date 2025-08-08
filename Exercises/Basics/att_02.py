number = int(input("Enter a number: "))
initial = int(input("Enter the initial number of the range: "))
final = int(input("Enter the final number of the range: "))

for i in range(initial, final + 1):
    print(f"{number} x {i} = {number * i}")

