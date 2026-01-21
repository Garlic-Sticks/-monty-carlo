import random
import numpy as np
import matplotlib.pyplot as plt

simulations = abs(int(input('how many simulations? ')))
wins = 0
losses = 0
print(f'running {simulations} simulations')
doors = ['a','b','c']

prize = np.random.randint(0,3, size=simulations)
bot_guess = np.random.randint(0,3, size=simulations)

stay_wins = (prize == bot_guess)
switch_wins = (prize != bot_guess)

total_stay_wins = np.sum(stay_wins)
total_switch_wins = np.sum(switch_wins)

x_axis = np.arange(1, simulations+1)
cum_switch_wins = np.cumsum(switch_wins)
cum_percent_win = (cum_switch_wins/x_axis)*100

print(f'results for {simulations} simulations')
print(f'stay wins: {total_stay_wins}')
print(f'switch wins: {total_switch_wins}')
print(f'switching winning % : {(total_switch_wins / simulations) * 100:.4f}%')

plt.plot(x_axis, cum_percent_win , label='switch wins')
plt.show()