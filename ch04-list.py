### LISTS
# Lists are values in an ordered sequence
#mylist = ['hello', 3.1415, True, None, 42]
'''
# Index of a list is an int
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[3])
print(['cat', 'bat', 'rat', 'elephant'][3])
# Negatve index starts at end
print(spam[-1])

# 2D List
twodee=[['a','b'],[0,1]]
print(twodee[0][0])
print(twodee[1][1])
'''
#######################################
'''
### Slice is a new list from a list
spam = ['cat', 'bat', 'rat', 'elephant']
> spam[1:3]
['bat', 'rat']
> spam[0:-1]
['cat', 'bat', 'rat']
> spam[:2]
['cat', 'bat']
> spam[1:]
['bat', 'rat', 'elephant']
> spam[:]
['cat', 'bat', 'rat', 'elephant']

# Can get length of list
>len(spam)
4

# Can change vals
> spam[1] = 'aardvark'
> spam[2] = spam[1]

# List Concat and Repllication
> [1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']
> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

# Remove value using del
spam = ['cat', 'bat', 'rat', 'elephant']
> del spam[2]
> spam
['cat', 'bat', 'elephant']
'''
#######################################
'''
# List of Cats
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + 
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)
'''

'''
### For Loops
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

### Using 'in' and 'not'
>spam = ['hello', 'hi', 'howdy', 'heyas']
>'howdy' in 'spam'
True
>'howdy' not in 'spam'
False

# EXAMPLE
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

### Multiple Assignment
# Exact num of vars as list
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
'''

'''
### Augmented Assignment Operators
> bacon = ['Zophie']
> bacon *= 3
> bacon
['Zophie', 'Zophie', 'Zophie']
'''
#######################################

'''
### METHODS FOR LISTS
# Like a function but for a value
# index()
spam = ['hello', 'hi', 'howdy', 'hello']
spam.index('hello')         #0 because returns first
spam.index('howdy howdy howdy') #ValueError

spam.append('x')            #adds 'x' to end
spam.insert(0,'y')          #inserts 'y' at front

# Sort
spam.sort()                 #sort only nums or strings not both
spam.sort(reverse=True) 
spam.sort(key=str.lower)    #sort lowercase first then upper for each letter 
'''
######################################3
'''
# MAGIC 8 BALL
import random
messages = ['It is certain',        #Lists can be multi-line and indented
    'It is decidedly so',           
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])
'''

#######################################
'''
### STRINGS ARE LISTS
# Can use index,slice,in,for loops
name = 'Zophie'
name[0]     #Z
name[0:4]   #Zoph

for i in name:
    print(i)        #Prints each char on own line
'''

'''
### TUPLE DATA TYPE
# TUPLES CAN'T BE MODIFIED
eggs = ('hello', 42, 0.5)
eggs[0]     #'hello'
len(eggs)   #3

# can change type
tuple(['cat','dog'])    #into ('cat','dog')
list('hi')              #into ['h','i']
'''
#######################################
'''
### REFERENCES
# Variables can store a LITERAL string,integer,tuple
> spam = 42
> cheese = spam
> spam = 100
> spam
100
> cheese
42

# Variables can store the REFERENCE of a list/dictionary
> spam = [0, 1, 2, 3, 4, 5]
> cheese = spam
> cheese[1] = 'Hello!'
> spam
[0, 'Hello!', 2, 3, 4, 5]
> cheese
[0, 'Hello!', 2, 3, 4, 5]

# Passing referrences
# Below will add 'Hello' because its given reference to a list
def eggs(someParameter):
    someParameter.append('Hello')
spam = [1, 2, 3]
eggs(spam)
print(spam)

### COPY MODULE
# Can import a module then use copy.copy()
# Can use copy.deepcopy() function for lists containing lists
> import copy
> spam = ['A', 'B', 'C', 'D']
> cheese = copy.copy(spam)
> cheese[1] = 42
> spam
['A', 'B', 'C', 'D']
> cheese
['A', 42, 'C', 'D']
'''
############################################
'''
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
'''