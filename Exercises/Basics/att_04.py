distance = float(input("Enter the distance in kilometers: "))

if distance > 200:
    print(F"Price: R$ {distance * 0.50:.2f}")
if distance <= 200:
    print(F"Price: R$ {distance * 0.45:.2f}")