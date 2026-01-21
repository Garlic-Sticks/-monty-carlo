#
import numpy as np
import matplotlib.pyplot as plt

def dice_game(players, rolls):
    rolls_array = np.random.randint(1,7,size=(players,rolls))
    player_totals = np.sum(rolls_array, axis=1)
    return player_totals

a = int(input('Enter a number of players: '))
b = int(input('Enter rolls per player: '))
game1 = dice_game(a,b)
print(f'scores: {game1}')

max_score = max(game1)
print(f'max_score: {max_score}')
winning_index= np.where(game1 == max_score)[0]
x_axis = np.arange(a) + 1
plt.bar(x_axis,game1,color='blue')
plt.bar(x_axis[winning_index],game1[winning_index],color='red')

print(f' winner is: {winning_index + 1}')
plt.show()
