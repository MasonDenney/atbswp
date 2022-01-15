"""
### FILES
"""
"""
### Slashing on different OS
# Windows is backslash \ and linux/Mac is forward slash /

# Adds Slashes
import os
print(os.path.join('usr', 'bin', 'spam'))
# Windows = 'usr\\bin\\spam'
# Linux = 'usr/bin/spam'

# Multiple Files
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))
#C:\Users\asweigart\accounts.txt
#C:\Users\asweigart\details.csv
#C:\Users\asweigart\invite.docx
"""
"""
### Current Working Dir
import os
os.getcwd()     #'C:\\Python34'
os.chdir('C:\\Windows\\System32')   #Change dir to existing
os.getcwd()     #'C:\\Windows\\System32'

## Make dir
import os
os.makedirs('C:\\delicious\\walnut\\waffles')

### The os.path() Module
# http://docs.python.org/3/library/os.path.html
# os.path.abspath(path)         #
# os.path.isabs(path)           #
# os.path.relpath(path, start)  #if no start assumes current dir

path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path)      #'calc.exe'
os.path.dirname(path)       #'C:\\Windows\\System32'
os.path.split(calcFilePath) #('C:\\Windows\\System32', 'calc.exe')

# sep on linux
'/usr/bin'.split(os.path.sep)   #['', 'usr', 'bin']
"""
############################################
"""
### File Sizes and Folder Contents
os.path.getsize('C:\\Windows\\System32\\calc.exe')
#776192
os.listdir('C:\\Windows\\System32')
#['0409', '12520437.cpx', ...

# EXAMPLE
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)
"

### Path Validity
# os.path.exists(path)
# os.path.isfile(path)
# os.path.isdir(path)
"""
###########################################
"""
### OPEN FILES WITH open()
# open() returns a File object, read mode by default
# helloFile = open('C:\\Users\\m\\hello.txt')
# helloFile = open('/Users/m/hello.txt')

### Reading
# .read()
helloContent = helloFile.read()     #Returns one string
# .readlines()
sonnetFile = open('sonnet29.txt')
sonnetFile.readlines()              # Returns list of strings
#[When, in disgrace with fortune and men's eyes,\n', ' I all ... fate,']

### Writing
# write or append mode will create the file if needed
# write mode will wipe/override current contents
# append mode will add to end
# returns number of chars
# write() doesn't automatically add a newline like print() does

### EXAMPLE
baconFile = open('bacon.txt', 'w')   
baconFile.write('Hello world!\n')               #returns 13
baconFile.close()
baconFile = open('bacon.txt', 'a') 
baconFile.write('Bacon is not a vegetable.')    #returns 25
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
# Hello world!
# Bacon is not a vegetable.
"""
#######################################
"""
### Saving variables with shelve module
# Saves variables in program to binary shelf file on hard drive
# On Windows creates x.bak, x.dat, x.dir
# On Linux create x.db

# EXAMPLE STORE
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

# EXAMPLE LOAD
shelfFile = shelve.open('mydata')
type(shelfFile)     #<class 'shelve.DbfilenameShelf'>
shelfFile['cats']   #['Zophie', 'Pooka', 'Simon']
shelfFile.close()
"""
"""
### Saving Vars w pprint.pformat()
# pretty print module will save string w good syntax
# Can write string to .py file
# Only good for basic data types like ints,float,strings,lists,dirs

# EXAMPLE STORE
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')  #83
fileObj.close()

# EXAMPLE LOAD
import myCats
myCats.cats
# [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
myCats.cats[0]
# {'name': 'Zophie', 'desc': 'chubby'}
myCats.cats[0]['name']
# 'Zophie'
"""
#######################################
"""
### Project: Generating Random Quiz Files

#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in

# random order, along with the answer key.
import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New 
Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West 
Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    
    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    
    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,  
            states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        
        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[ 
            answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
"""
#################################################
"""
### Project: Multiclipboard

#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
"""

#################################################
"""
### Project: 
"""