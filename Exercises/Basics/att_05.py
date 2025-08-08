number = int(input("Enter a number between 1000 and 9999: "))

if 1000 <= number <= 9999:
    thousands = number // 1000
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    units = number % 10

    print(f"Thousands: {thousands}")
    print(f"Hundreds: {hundreds}")
    print(f"Tens: {tens}")
    print(f"Units: {units}")