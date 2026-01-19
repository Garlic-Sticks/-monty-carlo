import random
from operator import truediv

doors = ['A','B','C']
#correct = [] #bucket to store winner
#choice = []
prize = random.choice(doors) #choosing correct door from options
#correct.append(prize)
print(prize)
#user = input(f'enter your choice {doors} \n').upper()
while True:
    user = input(f'enter your choice {doors} \n').upper()
    if user in doors:
        break
    else:
        print('enter a valid choice: A, B, or C')

#choice.append(user) #adding user choice door to bucket
second_round = set(doors) - {user} - {prize} #options for second round
system_opens = random.choice(list(second_round))
last_door = set(second_round) - set(system_opens)
print(f'opening door {system_opens}, it is a dud!')
switch = input(f'do you want to switch to door {last_door}? (y/n) ')
if switch == 'y':


if user == prize:
    print('you won!')
else:
    print(f'you lost, you chose {user}')