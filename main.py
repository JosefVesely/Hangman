import os
import time
import random
import msvcrt
import unidecode
from sound import playsound

from menu import menu
from color import color
from yes_no import yes_no
from stats import get_stats, pickle_stats

os.system('title Hangman')

wins, losses = 0, 0
used_words = []


def get_topic_and_word():
    # get random file from folder "words"
    # filename => topic
    # random line => word
    file_name = random.choice(os.listdir(os.getcwd()+'/assets/words'))

    while True:
        with open(f'{os.getcwd()}\\assets\\words\\{file_name}', encoding='utf-8') as f:
            words = f.readlines()
            topic = file_name[:-4]

            word = random.choice(words)
            word = unidecode.unidecode(word).upper().strip()

            if word in used_words:
                continue
            else:
                break

    return topic, word


def print_hangman():
    with open(f'assets/lives/{lives}.txt') as f:
        hangman = f.readlines()

    for line in hangman:
        line = line.replace('\n', '')
        print(color(line))


def get_guess():
    # return input if character is a letter of alphabet or "?"
    while True:
        try:
            guess = input('\tGuess a letter (? for hint): ')[0]
            guess = unidecode.unidecode(guess).upper()
        except IndexError:
            continue

        if guess == '?':
            if hints < 0:
                print(color('You ran out of hints!', 'red'))
                playsound('wrong')
                continue

        elif guess.isalpha():
            if guess in guessed_letters:
                print(color('You already guessed this letter!', 'red'))
                playsound('wrong')
                continue
        else:
            continue

        return guess


def get_guessed_word(word):
    guessed_word = ''

    for letter in word:
        if letter in guessed_letters or letter == ' ':
            guessed_word += letter
        else:
            guessed_word += '_'

    return guessed_word


def get_hints(word):
    # return number of hints according to length of the word
    length = len(word.replace(' ', ''))

    # 1 - 6  => 1
    # 7 - 14 => 2
    # 15 - ∞ => 3

    if length <= 6:
        hints = 1
    elif length <= 14:
        hints = 2
    else:
        hints = 3

    return hints


def add_word(word):
    if len(used_words) >= 16:
        del used_words[0]

    used_words.append(word)


# start menu
menu(get_stats())

print(f'\n\n{" "*30} PRESS ANY KEY TO PLAY')

msvcrt.getch()  # wait for keypress


# game loop
while True:
    topic, word = get_topic_and_word()
    lives = 10
    hints = get_hints(word)
    guessed_letters = []
    won = False


    while True:
        os.system('cls')
        print_hangman()

        guessed_word = get_guessed_word(word)

        # info =>
        print()
        print(color(f'Topic: {topic}', 'cyan'))


        print(color(f'Hints left: {hints}', 'cyan' if hints > 0 else 'red'))

        if wins != 0 or losses != 0:
            print(color(f'Wins: {wins}', 'green'))
            print(color(f'Losses: {losses}', 'red'))
        # <= info

        print()
        print(color(f'>  {" ".join(guessed_word)}  <', 'yellow'))
        print('\n')


        # check if player lost or won
        if guessed_word == word:
            wins += 1
            won = True
            add_word(word)

            print(color(f'You won!\n', 'green'))

            playsound('win')
            break

        if lives == 0:
            losses += 1
            add_word(word)

            print(
                color('You lost!', 'red'),
                color(f'\n\tThe word is {word}', 'yellow'),
                color('\n\tThis person died because of your incompetency...\n', 'red'))

            playsound('loss')
            break

        guess = get_guess()

        # wrong word
        if guess not in word and guess != '?':
            lives -= 1
            playsound('wrong')

        # hint
        elif guess == '?':
            if hints > 0:
                while True:
                    random_letter = random.choice(word)

                    if random_letter not in guessed_letters:
                        guessed_letters.append(random_letter)
                        playsound('right')
                        hints -= 1
                        break
            else:
                playsound('wrong')
        else:
            playsound('right')

        guessed_letters.append(guess)

    if won:
        pickle_stats(wins=1)
    else:
        pickle_stats(losses=1)

    answer = yes_no('\tDo you want to kill another person?')

    if answer:
        menu(get_stats())
        time.sleep(0.3)
        continue
    else:
        break
