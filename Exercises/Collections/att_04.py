names = [''] * 3
wheits = [0.0] * 3

for i in range(3):
    names[i] = str(input(f'Enter name {i + 1}: '))
    wheits[i] = float(input(f'Enter weight for {names[i]}: '))

weight_sort = sorted(wheits)

max_weight = weight_sort[-1]

min_weight = weight_sort[0]

print(f'The heaviest person is {names[wheits.index(max_weight)]} with a weight of {max_weight} kg.')

print(f'The lightest person is {names[wheits.index(min_weight)]} with a weight of {min_weight} kg.')