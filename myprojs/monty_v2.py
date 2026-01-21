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

print(f'results for {simulations} simulations')
print(f'stay wins: {total_stay_wins}')
print(f'switch wins: {total_switch_wins}')
print(f'switching winning % : {(total_switch_wins / simulations) * 100:.4f}%')
