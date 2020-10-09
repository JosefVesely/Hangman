
import os
import random
from color import color
from sound import playsound

def menu(stats):
     os.system('cls')

     colors = ['yellow', 'magenta', 'cyan', 'white']

     with open('assets/logo.txt', encoding='utf-8') as f:
          print('\n')
          print(color(f.read(), random.choice(colors), margin=False))

     games_played = stats['wins'] + stats['losses']

     if games_played != 0:
          win_ratio = stats['wins'] / games_played * 100
          win_ratio = int(win_ratio * 10) / 10
     else:
          win_ratio = '?'


     print(
     color(f'Games played: {games_played}', 'cyan'), 
     color(f'Wins: {stats["wins"]}', 'green'), 
     color(f'Losses: {stats["losses"]}', 'red'),
     color(f'Win ratio: {win_ratio}%', 'yellow')
     )

     playsound('theme')
