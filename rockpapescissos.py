import random
choices = ('r', 'p', 's')
bot_choice = random.choice(choices)
beats = {'r':'s',
         'p':'r',
         's':'p',}
while True:
    bot_choice = random.choice(choices)
    #print(bot_choice)
    user_choice = input('Enter a choice; rock(r), paper(p), scissors(s):\n ').lower()
    if user_choice not in choices:
        print('invalid choice, r p s only')
        continue
    #print(user_choice)
    if user_choice == (bot_choice):
        print('draw')
    elif beats[user_choice] == (bot_choice):
        print('win')
    else:
        print('lose')
    retry = input('do you want to try again? (y/n): ').lower()
    if retry != 'y':
        print('see you again')
        break