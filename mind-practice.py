import time
import random as rnd

print()
print('Hi, this is memory and attentiveness test. To the screen for you, I will show you a secret number. You have to guess it.')
print()
time.sleep(3)
print('We start!')
time.sleep(3)
print()
isTrue = True
cnt = 0


while isTrue:
    secret = str(rnd.randint(1, 100))

    print(secret)
    time.sleep(0.2)
    print('\033[F\033[K')
    print()

    answer = input("If you want to exit the game, just type 'exit'. Enter your answer: ")
    print()
    if answer == secret:
        cnt += 1
        print('You are right!')
        print()

        time.sleep(0.6)
    elif answer == 'exit':
        print('Bye!')
        print()

        isTrue = False
    else:
        print("You are wrong! Let's try one more time!")
        print()

        time.sleep(0.6)
print('You have guessed the secret number {} times.'.format(cnt))