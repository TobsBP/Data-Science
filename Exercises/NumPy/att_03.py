import numpy as np

mtz = np.zeros((2, 2))

randon_indeces = np.random.randint(0, 2, 2)

mtz[randon_indeces[0], randon_indeces[1]] = 1

cont = 0

while (True):
    pos_x = int(input("Enter a position x (0-1): "))
    pos_y = int(input("Enter a position y (0-1): "))

    if mtz[pos_x, pos_y] == 1:
        print("Game over! :( Try again.!")
        break
    else:
        cont += 1
        print("Safe! Current score:", cont)

        if cont == 3:
            print("Congratulations! You beat the game!")
            break