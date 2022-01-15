'''
### Dictionaries
# Unordered list and can have non-int index
# Indexes called keys, as in key-value pair

### Examples
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size']   #fat
'''
'''
### BIRTHDAYS
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
'''
'''
### METHODS keys() values() and items()
spam = {'color': 'red', 'age': 42}
for v in spam.values():
        print(v)        #red then 42
for k in spam.keys():
        print(k)        #color then age

# Items returns tuples
> for i in spam.items():
        print(i)
('color', 'red')
('age', 42)

### MULTIPLE ASSIGNMENT TRICK
> for k, v in spam.items():
        print('Key: ' + k + ' Value: ' + str(v))
Key: age Value: 42
Key: color Value: red
'''
'''
### EXISTS
spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys()       #True
'color' in spam             #False
print('Zophie' in spam)     #False only checks keys
'''
'''
### get() METHOD
# Two args, a key and a fallback
> picnicItems = {'apples': 5, 'cups': 2}
> 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing 2 cups.'
> 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
'I am bringing 0 eggs.'
'''
###############################################################
'''
### setdefault only works if no keyval yet, otherwise ignored
# mydict.setdefault('key','value')

### PRETTY PRINTING CHARACTER COUNT
# import module then pprint a dictionary's values

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)

#{' ': 13,
#...
#'y': 1}

# PFORMAT INTO STRING
pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))  #Into String
'''

######################################################
### USING DATA STRUCTURES TO MODEL REAL THINGS
# algebraic chess notation 
# from bottom left, so x=a-h rightwards and y=1-8 up

'''
### Tic-Tac-Toe
# can be 'X','O', or ' '
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
# Doesn't Check if over and can overwrite
'''

'''
### NESTED DICTIONARIES AND LISTS
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought
print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))
'''
######################################################

