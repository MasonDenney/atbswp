"""
### STRINGS

# Double-quote strings can have single-quote pnctuation without escaping
spam = "That is Alice's cat."
spam = 'Say hi to Bob\'s mother.'

# Print raw string with r prefix
print(r'That is Carol\'s cat.')
"""
#################################
"""
#### Multi-line Strings with triple single-quotes
# prints 5 lines including blank lines
# Don't need to escape the single-quote

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
"""
##############################

#### Multi-line comments use triple double-quotes
# FUNCTION DOCUMENTATION in """ or ''' under function

"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""

#def spam():
#    """This is a multiline comment to help     # hover documentation works
#    explain what the spam() function does."""
#    print('Hello!')
#def x():
#    # Test x                                   # hover documentation FAILS
#    print()
#def y():
#    '''Test y'''                               # hover documentation works
#    print()

#############################
"""
### Slicing and Indexing
spam = 'Hello world!'
spam[0:5]   #'Hello'

### in and not Operators
# case-sensitive
'Hello' in 'Hello World'        #True
'' in 'spam'                    #True
'cats' not in 'cats and dogs'   #False
"""
#############################
"""
### USEFUL METHODS

### upper() and lower()
spam = 'Hello world!'
spam = spam.upper()         #HELLO WORLD!
spam = spam.lower()         #hello world!

### isupper() and islower()
'HELLO'.isupper()       #True
'abc12345'.islower()    #True, alpha is lower
'12345'.islower()       #False, no alpha

### isX METHODS
# isalpha(), isalnum(), isdecimal(), isspace(), istitle()
# Helpful for validating user input

### stratswith() and endswith()
# useful alternatives to == sometimes
'Hello world!'.startswith('Hello world!')   #True
'Hello world!'.endswith('Hello world!')     #True

### join() and split() String Methods
', '.join(['cats', 'rats', 'bats'])     #'cats, rats, bats'
' '.join(['My', 'name', 'is', 'Simon']) #'My name is Simon'
# split does space by default
'My name is Simon'.split()              #['My', 'name', 'is', 'Simon']
'My name is Simon'.split('m')           #['My na', 'e is Si', 'on']
# Split('\n') will split multi-line string at newline
"""
"""
### JUSTIFYING TEXT rjust(), ljust(), and center()
> 'Hello'.rjust(10)
'     Hello'
> 'Hello'.rjust(20)
'               Hello'
> 'Hello World'.rjust(20)
'         Hello World'
> 'Hello'.ljust(10)
'Hello 
> 'Hello'.center(20)
'       Hello        '
> 'Hello'.center(20, '=')
'=======Hello========'

### PICNIC EXAMPLE
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
"""
#############################
"""
### Removing Whitespace
> spam = '    Hello World    '
> spam.strip()      #'Hello World'
> spam.lstrip()     #'Hello World    '
> spam.rstrip()     #'    Hello World'

# removes chars in any order
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')  #'BaconSpamEggs'
"""
#############################
"""
### PYPERCLIP MODULE
import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste()               #'Hello world!'
# paste works with whatever is in clipboard, don't need to copy
"""
#############################
"""
### Project: Password Locker
#! python3
# pw.py - An insecure password locker program.
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]    # first command line arg is the account name
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

"""
#############################
"""
### Project: Bullet Point Adder for Wikipedia
#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip
text = pyperclip.paste()
# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
"""
#############################
"""
### Practice Project: Table Printer
tableData = [['apples', 'oranges', 'cherries', 'banana'], 
             ['Alice', 'Bob', 'Carol', 'David'], 
             ['dogs', 'cats', 'moose', 'goose']]
"""
