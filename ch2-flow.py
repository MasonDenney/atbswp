'''
### Boolean
True or False

### Comparison Operator results in Boolean
# ==,!=,<,>,<=,>=

> 42 == '42'
False

### Operators
# and, or, not,

### Elements of Flow Control
# Only the first matching if/elif is executed and all other good/bad are skipped
# break breaks out of loop it is in
# continue goes back to beginning of loop it is in

### Truthy and Falsey Values
# False = 0 and 0.0 and '' (empty string)
'''

'''
### while break 
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')
'''

'''
### while continue break
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue            #restarts loop at 'Who are you?'
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break               #will exit loop
print('Access granted.') 
'''

'''
### For loops and range()
for i in range(5):
    print('Zero to Four Means Five Times (' + str(i) + ')')
'''
'''
# Equivalent in while loop
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1
'''
'''
### range with 2 args
# prints 12,13,14,15
for i in range(12, 16):
    print(i)
'''
'''
# range with 3 args
# prints 0,2,4,6,8
for i in range(0, 10, 2):
    print(i)
'''
############################################
'''
### IMPORTING MODULES
# prints 5 random ints 1-10
import random
for i in range(5):
    print(random.randint(1, 10))
'''
'''
#(from random import *) CANNOT USE A PREFIX
from random import *
for i in range(5):
    print(randint(1, 10))
'''
############################################
'''
# Can exit but need to import
import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
'''
