import random
import time

def print_dramatic_text(text: str, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    # create character by collecting user input (name + class)
    # print character sheet
    # specify roll that must be beat and enemy initiative by collecting user input
    # any buffs / debuffs?
    # any critical success / failure?

    name = input('Name: ')

    print_dramatic_text('Welcome to Marbles!!') 
    print_dramatic_text('In this game, you will start with 10 marbles. A number will be randomly rolled on a dice and, before seeing it, you must guess if it is odd or even.')
    print_dramatic_text('If you correctly guess if the number is odd or even, the number rolled will be added to your marble amount')
    print_dramatic_text('However, if you guess incorrectly, the number rolled will be taken from your marble amount.')
    print_dramatic_text('You will win once you gain 20 marbles, but if you run out, you will lose the game.')


    marbles = 10
    while marbles < 20 and marbles > 0:
        r = random.randint(1, 9)
        answer = input('odd or even? ')
        if answer == 'even' and r % 2 == 0:
            print_dramatic_text('Correct! the number was ' + str(r))
            marbles += r
            print('You have ' + str(marbles) + ' marbles')
        elif answer == 'odd' and r % 2 == 1:
            print_dramatic_text('Correct! the number was ' + str(r))
            marbles += r
            print('You have ' + str(marbles) + ' marbles')
        else:
            print_dramatic_text('Sorry the number was ' + str(r) + ' ...')
            marbles -= r
            print('You have ' + str(marbles) + ' marbles')

    if marbles >= 20:
        print_dramatic_text('Congratulations! You have ' + str(marbles) + ' marbles! You win!')
    else:
        print_dramatic_text('Sorry -- you\'ve run out of marbles! You lose!')