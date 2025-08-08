teams = ['Barcelona', 'Madrid', 'Valencia', 'Sevilla', 'Bilbao']

print(f'A) The firsts four teams are: {teams[:4]}')

print(f'B) The last two teams are: {teams[-2:]}')

print(f'C) Alphabetically sorted teams: {sorted(teams)}')

print(f'D) What position is Barcelona in the list? {teams.index("Barcelona") + 1}')