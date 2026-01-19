import random

doors = ['A','B','C']
prize = random.choice(doors) #choosing correct door from options
while True:
    user = input(f'enter your choice {doors} \n').upper()
    if user in doors:
        break
    else:
        print('enter a valid choice: A, B, or C')

second_round = set(doors) - {user} - {prize} #options for second round
monty_opens = random.choice(list(second_round))
last_door = set(doors) - {user} - {monty_opens}
print(f'opening door {monty_opens}, it is a dud!')
new_choice = last_door.pop()
switch = input(f'do you want to switch to door {new_choice}? (y/n) ')
if switch == 'y':
   user = new_choice
if user == prize:
    print('you won!')
else:
    print(f'you lost, you chose {user}')