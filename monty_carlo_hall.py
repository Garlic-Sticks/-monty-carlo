#always switching
import random

simulations = abs(int(input('how many simulations? ')))
wins = 0
losses = 0
test_condition = int(input("type '1' for switching, '2' for staying "))
print(f'running {simulations} simulations')

doors = ['A','B','C']

for i in range(simulations):
    prize = random.choice(doors)
    bot_initial = random.choice(doors)

    second_round = set(doors) - {bot_initial} - {prize} #options for second round

    monty_opens = random.choice(list(second_round))
    last_door = set(doors) - {bot_initial} - {monty_opens}

    #switching condition
    switch_choice = last_door.pop()
    if test_condition == 1: #switch
        final_choice = switch_choice
    else: #stay
        final_choice = bot_initial

    if final_choice == prize:
        wins += 1
    else:
        losses += 1
strat_name = 'switching' if test_condition == 1 else 'staying'
print(f'strategy name: {strat_name}')
print(f'wins {strat_name}: {wins}')
print(f'losses {strat_name}: {losses}')
print(f'winning %: {wins / simulations * 100:.4f}%')