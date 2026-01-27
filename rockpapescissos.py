import random

user_choice = input("Enter your choice: ")
choices = {'r':1,
           'p':2,
           's':0}
bot_choice = random.choice(list(choices))
print(f'bot choice {bot_choice}')
bot_store = choices.get(bot_choice)
user_store = choices.get(user_choice)
# print(f'bot store {bot_store}, {type(bot_store)}')
# print(f'user store {user_store}, {type(user_store)}')
# print(f'user choice {user_choice}')
decider = (user_store - bot_store) % 3
if decider == 1:
    print(f'you won, bot chose {bot_choice} and you chose {user_choice}')
elif decider == 2:
    print(f'you lost, bot chose {bot_choice} and you chose {user_choice}')
else:
    print('draw')


