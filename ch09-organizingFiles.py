"""
### ORGANIZING FILES

### The shutil module
# Can copy, move, rename and delete

## Example
import shutil, os
os.chdir('C:\\')
shutil.copy('C:\\spam.txt', 'C:\\delicious')    #no new name
# 'C:\\delicious\\spam.txt'
shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt') #new name
# 'C:\\delicious\\eggs2.txt'
shutil.copytree('C:\\bacon', 'C:\\bacon_backup')    # copies -R

## Moving and Renaming
shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt') #move
shutil.move('C:\\bacon.txt', 'C:\\eggs')                #rename

## Deleting
os.unlink(path)         # Removes file at path
os.rmdir(path)          # Removes empty folder
shutil.rmtree(path)     # Removes folder ad all contents
"""
"""
## Safe deletes and send2trash()
import send2trash
baconFile = open('bacon.txt', 'a')              # creates the file
baconFile.write('Bacon is not a vegetable.')    #25
baconFile.close()
send2trash.send2trash('bacon.txt')
"""
########################
"""
### Walking a dir tree
# os.walk() returns 3 things: name, list of folders, list of files

## EXAMPLE
import os
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
    print('')        
"""
########################
"""
### The zipfile module

## Reading zips
import zipfile, os
os.chdir('C:\\')            # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()       #['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size          #13908
spamInfo.compress_size      #3828
'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
# 'Compressed file is 3.63x smaller!'
exampleZip.close()

## Extracting all from zips
import zipfile, os
os.chdir('C:\\')    # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()

## Extract single file
exampleZip.extract('spam.txt')      #must match something in namelist()
#'C:\\spam.txt'
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
#'C:\\some\\new\\folders\\spam.txt'
exampleZip.close()

## Creating and adding to zips
# write will override, a will append
import zipfile
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
"""
#############################
'''
### Project: Rename files with usa date to euro date
#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format  
# to European DD-MM-YYYY.

import shutil, os, re
# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip files without a date.
    if mo == None:
        continue
    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)
    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename)   # uncomment after testing
'''
#############################
"""
### Project: Backing up a Folder into a zip file

#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os
def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)   # make sure folder is absolute
    
    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase / os.path.basename(folder) + '_' 
            if filename.startswith(newBase) and filename.endswith('.zip')
                continue            # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip('C:\\delicious')

"""
