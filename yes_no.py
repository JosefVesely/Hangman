
def yes_no(question):
    while True:
        answer = input(f'{question} (y/n) ')

        if answer.strip().lower()[:1] == 'y':
            return True
        elif answer.strip().lower()[:1] == 'n':
            return False
