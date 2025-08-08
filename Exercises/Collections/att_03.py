name = str(input("Enter your name: "))

median = float(input("Enter your median grade: "))

student = {
    'name': name,
    'median': median
}

if median >= 50:
    student['status'] = 'AP'
else:
    student['status'] = 'RP'

print(student)