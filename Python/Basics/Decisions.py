# Examples of decision making in Python

# 1. Simple if statement
x = 10
if x > 5:
    print("x is greater than 5")

# 2. if-else statement
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")

# 3. if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or F")

# 4. Nested if statements
age = 20
if age >= 18:
    if age < 21:
        print("You are an adult but not yet 21.")
    else:
        print("You are 21 or older.")
else:
    print("You are a minor.")

# 5. Ternary operator (conditional expression)
number = 7
result = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {result}")