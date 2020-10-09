
from termcolor import colored

def color(sentence, color='white', margin=True):
     if margin:
          return colored(f'\t{sentence}', color, attrs=['bold'])
     else:
          return colored(sentence, color, attrs=['bold'])
