"""
### DEBUGGING
"""
"""
## Raising Exceptions
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))
"""
"""
## Get Traceback as String
def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')
spam()

# Instead of crashing, can log to file and keep running
import traceback
try:
         raise Exception('This is the error message.')
except:
         errorFile = open('errorInfo.txt', 'w')
         errorFile.write(traceback.format_exc())
         errorFile.close()
         print('The traceback info was written to errorInfo.txt.')
#116 #num of chars in errorinfo.txt
#The traceback info was written to errorInfo.txt.

"""
##################
"""
## Assertions
# Sanity check 
podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can't do that.''
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
 #Traceback (most recent call last):
 #  File "<pyshell#10>", line 1, in <module>
 #    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
 #AssertionError: The pod bay doors need to be "open".


## Using an assertion for traffic light
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}
def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
        assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
switchLights(market_2nd)


## Disabling Assertions
# Can be disabled by passing the -O option when running Python
# Good once done testing
"""
##################
"""
## Logging
## Logging module
# Creates a LogRecord object, can customize with basicConfig()
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s  -  %(message)s')

# EXAMPLE FACTORIAL
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s  -  %(message)s')
logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
#    for i in range(n + 1):     #Multiplying by zero
    for i in range(1,n + 1):    
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total
print(factorial(5))
logging.debug('End of program')


## Don't debug with print()
# Pain to remove when done testing

## Logging levels
# Lowest level will show all --> Highest will only show crash
# Only for diagnosing --> Only things that will stop program
# DEBUG, INFO, WARNING, ERROR, CRITICAL
# logging.debug() ... logging.critical()
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
logging.debug('Some debugging details.')
# 2015-05-18 19:04:26,901 - DEBUG - Some debugging details.

## Disabling logging
logging.disable(logging.CRITICAL)   #Disables all logging at all levels

## Logging to a file
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

"""
###################
"""
## IDLE's debugger

"""
###################
"""
### Project: Debugging Coin Toss

"""