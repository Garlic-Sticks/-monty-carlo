import numpy as np
import matplotlib.pyplot as plt

rolls_array = np.random.randint(1,7,size=(5,10))
player_totals = np.sum(rolls_array, axis=1)
print(f'scores: {player_totals}')
#print(np.max(player_totals))
players = np.array(['a', 'b', 'c', 'd', 'e'])
plt.bar(players, player_totals, color='green')
max_score = max(player_totals)
print(f'max_score: {max_score}')
winning_index= np.where(player_totals == max_score)[0]
plt.title('dice game')
plt.xlabel('players')
plt.ylabel('total points')
print(f' winner is: {winning_index +1}')
plt.bar(players[winning_index], player_totals[winning_index], color='blue')
plt.show()
