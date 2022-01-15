"""
### Keeping Time, Scheduling Tasks, and Launching Programs
"""
"""
#
"""
"""
### Project: Super Stopwatch
#! python3
# stopwatch.py - A simple stopwatch program.
import time

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. 

Press Ctrl-C to quit.')

input()                    # press Enter to begin

print('Started.')

startTime = time.time()    # get the first lap's start time

lastTime = startTime

lapNum = 1

# Start tracking the lap times.
u try:
v    while True:
        input()
w         lapTime = round(time.time() - lastTime, 2)

x         totalTime = round(time.time() - startTime, 2)

y         print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1

        lastTime = time.time() # reset the last lap time
z except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.

    print('\nDone.')
"""
"""
#
"""
"""
#
"""
#############
"""
### Project: Multi-threaded XKCD Downloader
#! python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.
import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)
        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# Create and start the Thread objects.
downloadThreads = []             # a list of all the Thread objects
for i in range(0, 1400, 100):    # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()
# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')

"""
###############
"""
#
"""
"""
### Project: Simple Countdown Program

#! python3
# countdown.py - A simple countdown script.

import time, subprocess
timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)
"""
"""
#
"""
"""
#
"""
"""
### Project: Prettified Stopwatch
"""
"""
### Project: Scheduled Web Comic Downloader
"""