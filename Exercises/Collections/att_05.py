n = int(input('Number of people to register: '))

names = [''] * n
ages = [0] * n
genders = [''] * n

for i in range(n):
    names[i] = input(f'Enter name {i + 1}: ')
    ages[i] = int(input(f'Enter age for {names[i]}: '))
    genders[i] = input(f'Enter your gender (M/F) for {names[i]}: ').upper()

average_age = sum(ages) / n

print(f'The average age of the group is {average_age:.2f} years.')

women_under_20 = sum(1 for i in range(n) if genders[i] == 'F' and ages[i] < 20)

print(f'The number of women under 20 years old: {women_under_20}')