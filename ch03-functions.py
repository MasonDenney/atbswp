'''
### Functions
# Functions are programs within programs
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')
hello()
'''
'''
def hello(name):
    print('Hello ' + name) 
hello('Alice')
'''
############################################
'''
### magic8ball.py
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
#print(getAnswer(random.randint(1, 9)))
'''
############################################
'''
### The None Value
# None is similar to null/nil/undefined

# Python adds 'return None' to end of any function without a return statement
> spam = print('Hello!')
Hello!
> None == spam
True
'''

'''
### Print Args
# print has 'end' and 'sep' arg
>print('cats', 'dogs', 'mice', sep=',')
cats,dogs,mice

#can disable automatic newline with empty string
>print('Hello', end='')
>print('World')
HelloWorld
'''

'''
### Local and Global Scope
def spam():
    eggs = 'spam local'
    print(eggs)    # prints 'spam local'
def bacon():
    eggs = 'bacon local'
    print(eggs)    # prints 'bacon local'
    spam()
    print(eggs)    # prints 'bacon local'
eggs = 'global'
bacon()
print(eggs)        # prints 'global'
#prints bacon,spam,bacon,global
'''

'''
### Global statement
# use within a function to use/modify the global variable
def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)
#prints spam
'''
############################################
'''
### Exception Handling with try/except
# try in function
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
# prints 21.0,3.5,Error,None,42.0
'''
'''
# try in main
def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
#prints 21.0,3.5,Error
'''

############################################
'''
# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
'''