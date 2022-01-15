"""
### REGULAR EXPRESSIONS

# Test using website: http://regexpal.com/
"""
"""
### NO REGEX

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
         print('Phone number found: ' + chunk)
print('Done')
"""
"""
# REGEX
# \d is digit 0-9
# {3} at end means match 3 times
# \d\d\d-\d\d\d-\d\d\d\d is equivalent to \d{3}-\d{3}-\d{4}

# Use Raw String to save time
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   #raw
#phoneNumRegex = re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d') #not raw
"""
"""
# EXAMPLE
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   #Make regex obj
mo = phoneNumRegex.search('My number is 415-555-4242.') #Store matches
print('Phone number found: ' + mo.group())              #Print matches
"""
#######################################
"""
### MORE PATTERN MATCHING

# Group with parenthesis
import re

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)             #'(415)'
mo.group(2)             #'555-4242'
print(mo.groups())      #('(415)','555-4242')
"""
#######################################
"""
### PIPE |
# pipe used to match one of many
# first occurence returned

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()      #'Batmobile'
mo.group(1)     #'mobile'

### OPTIONAL ?
Should match whether or not preceeding found

batRegex = re.compile(r'Bat(wo)?man')               #Make Regex Pattern
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()     #'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()     #'Batwoman'

### STAR for 0 or more
# Can be absent
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()     #'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()     #'Batwoman'
mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()     #'Batwowowowoman'

### PLus for 1 or more
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()     #'Batwoman'
mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()     #'Batwowowowoman'
mo3 = batRegex.search('The Adventures of Batman')
mo3 == None     #True

### CURLY BRACES FOR SPECIFIC REPEATS
# specific number of groups
# {3,5} = three four or five
# {3,} = 3+   and   {,5} = 0 to 5

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()     #'HaHaHa'
mo2 = haRegex.search('Ha')
mo2 == None     #True
"""
########################################################
"""
### Greedy and Nongreedy Matching
# Regex is greedy by default and prefer longest string
# Non greedy if ? after like nongreedyHaRegex = re.compile(r'(Ha){3,5}?')

### The findall() Method
# search() will return first, findall() returns all
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
#['415-555-9999', '212-555-0000']
# \d\d\d-\d\d\d-\d\d\d\d        returns ['415-555-9999', '212-555-0000']
# (\d\d\d)-(\d\d\d)-(\d\d\d\d)  returns [('415', '555', '1122'), ('212', '555', '0000')]
"""
"""
### Character Classes
\d      Any numeric digit from 0 to 9.
\D      Any character that is not a numeric digit from 0 to 9.
\w      Any letter, numeric digit, or the underscore character. 
        (Think of this as matching “word” characters.)
\W      Any character that is not a letter, numeric digit, or the 
        underscore character.
\s      Any space, tab, or newline character. (Think of this as 
        matching “space” characters.)
\S      Any character that is not a space, tab, or newline.

# EXAMPLE
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 
swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
"""
#############################################
"""
### Making own character class
# define within square brackets
# Carot within means not
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.') #['o', 'o', 'o',
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.') #['R', 'b', 'c'

### Caret and Dollarsign
# ^ if match must occur in beginning
# $ if match occur at end
re.compile(r'^Hello')   #Hello at start
beginsWithHello.search('Hello world!')      #<_sre.SRE_Match object; span=(0, 5), match='Hello'>
re.compile(r'\d$')      #End with number
endsWithNumber.search('Your number is 42')  #<_sre.SRE_Match object; span=(16, 17), match='2'>
"""
############################################
"""
### THE WILDCARD
# matches anything and everything
# . means anything but newline and * means zero+ of preceeding
# So .* means anything

# EXAMPLE
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)     #'Al'
mo.group(2)     #'Sweigart'

# NON-GREEDY
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()      #'<To serve man>'
# GREEDY
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()      #'<To serve man> for dinner.>'
"""
#############################################
"""
#### Matching Newlines with re.DOTALL
newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent. 
\nUphold the law.').group()
# 'Serve the public trust.\nProtect the innocent.\nUphold the law.

### CASE-INSENSITIVE MATCHING
# re.IGNORECASE or re.I
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
#'RoboCop'
robocop.search('ROBOCOP protects the innocent.').group()
#'ROBOCOP'
robocop.search('Al, why does your programming book talk about robocop so much?').group()
#'robocop'
"""
#############################################
"""
### REVIEW
•  The ? matches zero or one of the preceding group.
•  The * matches zero or more of the preceding group.
•  The + matches one or more of the preceding group.
•  The {n} matches exactly n of the preceding group.
•  The {n,} matches n or more of the preceding group.
•  The {,m} matches 0 to m of the preceding group.
•  The {n,m} matches at least n and at most m of the preceding group.
•  {n,m}? or *? or +? performs a nongreedy match of the preceding group.
•  ^spam means the string must begin with spam.
•  spam$ means the string must end with spam.
•  The . matches any character, except newline characters.
•  \d, \w, and \s match a digit, word, or space character, respectively.
•  \D, \W, and \S match anything except a digit, word, or space character.
•  [abc] matches any character between the brackets (such as a, b, or c).
•  [^abc] matches any character that isn’t between the brackets.
"""
###############################################
"""
### Substituting Strings with sub() Method
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# 'CENSORED gave the secret documents to CENSORED.'
agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
# A**** told C**** that E**** knew B**** was a double agent.'

### VERBOSE
# verbose argument ignores whitespace and comments within '''
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
"""
"""
### COMBINING
# compile() only takes 2 args, but can pipe together
# someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
"""
#################################################
"""
### Project: Phone and Email Extractor
#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

"""
#######################################
"""
### Project: Strong Password Detection
"""
"""
### Project: Regex version of strip()
"""
