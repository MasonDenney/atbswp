'''
### Basic Operations and Types
# Math Operators
Operator    Name                    Example     Result
**          Exponent                2 ** 3      8
%           Mod/Remainder           22 % 8      6
//          IntDivision/Floor       22 // 8     2

# Types
strings have single quotes

### Strings
# String Concatenation
>'Alice' + 'Bob'
'AliceBob'
> 'Alice' + 42
TypeError

# String Replication when string and int
> 'Alice' * 5
'AliceAliceAliceAliceAlice'
 'Alice' * 'Bob'
TypeError
> 'Alice' * 5.0
TypeError

### Variables
# Allowed: alphanumeric, underscores (even begin with underscore)
# Not Allowed: spaces, hyphens, special chars, cant begin with a number

# Variables are case-sensitive, convention is start with lowercase camelcase

# PEP8 suggests underscores but camelcase is common 
'''

'''
### First Program
# This program says hello and asks for my name.
print('Hello world!')
print()                                             #Prints blank line
print('What is your name?')
myName = input()                                    #input saves as string
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))                                  #len() works on strings
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')   #force into to str
'''

'''
### Evaluating to diff type
> str(-3.14)
'-3.14'
> int('-99')
-99
> int(1.99)     #Rounds float down
1
> float(10)
10.0

>int('99.99')
Error
>int('twelve')
Error
'''

'''
### Text and Number Equivalence
> 42 == '42'
False
> 42 == 42.0
True
> 42.0 == 0042.000
True
'''


