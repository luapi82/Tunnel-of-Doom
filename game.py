from random import randint
gameOn = True
score = 0

print('***** Tunnel of Doom *****\n')

def startGame():
    global gameOn
    global score
    while gameOn:
        wrongTunnel = randint(1,3)
        choice = int(input('\nChoose a tunnel Left[1], Middle[2], Right[3] [1,2,3]: '))
        if (choice == 1 or choice == 2 or choice == 3):
            if choice == wrongTunnel:
                ohNo = '\nOh no, wrong tunnel.'
                whichOne = randint(1,7)
                if whichOne == 1: print(ohNo, 'A dragon ate you...')
                elif whichOne == 2: print(ohNo, 'You fell into lava...')
                elif whichOne == 3: print(ohNo, 'A boulder fell and crushed you...')
                elif whichOne == 4: print(ohNo, 'You tripped on your shoe laces and hit your head...')
                elif whichOne == 5: print(ohNo, 'You ate a really poisonous mushroom and succombed to your death...')
                elif whichOne == 6: print(ohNo, 'You got lost and died of starvation...')
                elif whichOne == 7: print(ohNo, 'You fell off the boat...')
                print('\nGame over! You scored *****', score, '*****')    
                usrChoice = str(input('Would you like to play again? [Y,N]: '))
                if (usrChoice == 'y' or choice == 'Y' or choice == 'YES' or choice == 'yes' or choice == 'Yes'):
                    score = 0
                    startGame()
                else:
                    print('Goodbye...')
                    gameOn = False
            else:
                score += 1
                print('\nCorrect Tunnel! Next room... Score: ',score,)
if gameOn: startGame()
