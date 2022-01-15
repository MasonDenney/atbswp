"""
### WEB SCRAPING
# Modules:
# webbrowser - standard module, opens browser to specific page
# Requests - Downloads files/pages from internet
# BeautifulSoup - Parses HTML
# Selenium - Launches and controls a web browser
"""
"""
### Project: mapit.py with webbrowser module
#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)

"""
#########
"""
### Downloading Files wth 'requests' module

## requests.get()
import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
type(res)                               #<class 'requests.models.Response'>
res.status_code == requests.codes.ok    #True
len(res.text)                           #178981
print(res.text[:250])                   #The Project Gutenberg ...

## Check for errors
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()      #Traceback
# If not a dealbreaker, wrap in try/except
import requests
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
"""
"""
### Saving Downloads to the Hard Drive
# requests.get() to download
# open() with wb for new file in write and binary mode
# Loop
# write() on each iteration
# close()

import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):          #100k bytes a good size for a chunk
    playFile.write(chunk)
#100000
#78981
playFile.close()
"""
#############################
"""
### HTML
## Resources
# http://htmldog.com/guides/html/beginner/
# http://www.codecademy.com/tracks/web/
# https://developer.mozilla.org/en-US/learn/html/
## Free Books
# http://inventwithpython.com
## Quick Refresher
## View Source HTML in browser
## Developer Tools
# http://weather.gov/
"""
"""
### Parsing HTML With BeautifulSoup

####################################
<!-- This is the example.html example file. -->
<html><head><title>The Website Title</title></head>
<body>
<p>Download my <strong>Python</strong> book from <a href="http://
inventwithpython.com">my website</a>.</p>
<p class="slogan">Learn Python the easy way!</p>
<p>By <span id="author">Al Sweigart</span></p>
</body></html>
####################################

# EXAMPLE - Internet
import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)      #<class 'bs4.BeautifulSoup'>

# EXAMPLE - Local File
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)   #<class 'bs4.BeautifulSoup'>

## Finding an Element with select() Method
# Call select() method and pass string of CSS selector
# http://nostarch.com/automatestuff/

########################################################################
Selector passed to the select() method          Will match  .  .  .
soup.select('div')              All elements named <div>
soup.select('#author')          The element with an id attribute of author
soup.select('.notice')          All elements that use a CSS class attribute named notice
soup.select('div span')             All elements named <span> that are within an element 
                                    named <div>
soup.select('div > span')           All elements named <span> that are directly within an 
                                    element named <div>, with no other element in between
soup.select('input[name]')          All elements named <input> that have a name attribute 
                                    with any value
soup.select('input[type="button"]') All elements named <input> that have an attribute 
                                    named type with value button
########################################################################
# soup.select('p #author') will match our id=author and within a p tag
# select returns a list of Tag objects, Tag can be passed to str()
"""
"""
####################################
<!-- This is the example.html example file. -->
<html><head><title>The Website Title</title></head>
<body>
<p>Download my <strong>Python</strong> book from <a href="http://
inventwithpython.com">my website</a>.</p>
<p class="slogan">Learn Python the easy way!</p>
<p>By <span id="author">Al Sweigart</span></p>
</body></html>
####################################

## EXAMPLE
import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
type(elems)             #<class 'list'>
len(elems)              #1
type(elems[0])          #<class 'bs4.element.Tag'>
elems[0].getText()      #'Al Sweigart'
str(elems[0])           #'<span id="author">Al Sweigart</span>'
elems[0].attrs          #{'id': 'author'}

pElems = exampleSoup.select('p')
str(pElems[0])          #'<p>Download my <strong>Python</strong> book from <a href="http://
                        #inventwithpython.com">my website</a>.</p>'
pElems[0].getText()     #'Download my Python book from my website.'
str(pElems[1])          #'<p class="slogan">Learn Python the easy way!</p>'
pElems[1].getText()     #'Learn Python the easy way!'
str(pElems[2])          #'<p>By <span id="author">Al Sweigart</span></p>'
pElems[2].getText()     #'By Al Sweigart'

## EXAMPLE
import bs4
soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
str(spanElem)           #'<span id="author">Al Sweigart</span>'
spanElem.get('id')      #'author'
spanElem.get('some_nonexistent_addr') == None   #True
spanElem.attrs          #{'id': 'author'}


# Learn More
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/

"""
#################################################
"""
### Project: I'm Feeling Lucky Google Search

#! python3
# lucky.py - Opens several Google search results.
import requests, sys, webbrowser, bs4

print('Googling...')    # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)
# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

"""
#######################################
"""
### Project: Downloading all XKCD Comics

#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
import requests, os, bs4

url = 'http://xkcd.com'               # starting url
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
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
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')
"""
############################################
"""
### Controlling the Browser with Selenium module
# Using Firefox for below examples

from selenium import webdriver
browser = webdriver.Firefox()
type(browser)   #<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
browser.get('http://inventwithpython.com')

## Finding Elements on the Page
############################################
method name                                 WebElement object/list returned
browser.find_element_by_class_name(name)
browser.find_elements_by_class_name(name)   Elements that use the CSS class name
browser.find_element_by_css_selector(selector) 
browser.find_elements_by_css_selector(selector)     Elements that match the CSS selector
browser.find_element_by_id(id)
browser.find_elements_by_id(id)             Elements with a matching id attribute value
browser.find_element_by_link_text(text)
browser.find_elements_by_link_text(text)    <a> elements that completely match the text provided
browser.find_element_by_partial_link_text(text)
browser.find_elements_by_partial_link_text(text)    <a> elements that contain the text provided
browser.find_element_by_name(name)
browser.find_elements_by_name(name)         Elements with a matching name attribute value
browser.find_element_by_tag_name(name) 
browser.find_elements_by_tag_name(name)     Elements with a matching tag name (case insensitive; an <a> element is matched by 'a' and 'A')
############################################

############################################
Attribute or method         Description
tag_name                The tag name, such as 'a' for an <a> element
get_attribute(name)     The value for the element’s name attribute text The text within the element, such as 'hello' in <span>hello</span>clear() For text field or text area elements, clears the text typed into it
is_displayed()          Returns True if the element is visible; otherwise returns False
is_enabled()            For input elements, returns True if the element is enabled; otherwise returns False
is_selected()           For checkbox or radio button elements, returns True if the element is selected; otherwise returns False location A dictionary with keys 'x' and 'y' for the position of the element in the page
############################################

## EXAMPLE
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')


## CLICKING THE PAGE
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
type(linkElem)  #<class 'selenium.webdriver.remote.webelement.WebElement'>
linkElem.click()    # follows the "Read It Online" link

## FILLING OUT AND SUBMITTING FORMS
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('not_my_real_email@gmail.com')
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('12345')
passwordElem.submit()

## SENDING SPECIAL KEYS
############################################
Attributes                                      meanings
Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT       The keyboard arrow keys
Keys.ENTER, Keys.RETURN                         The enter and return keys
Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP   The home, end, pagedown, and pageup keys
Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE       The esc, backspace, and delete keys
Keys.F1, Keys.F2, .., Keys.F12                  The F1 to F12 keys at the top of the keyboard
Keys.TAB                                        The tab key
############################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)     # scrolls to bottom
htmlElem.send_keys(Keys.HOME)    # scrolls to top

## CLICKING BROWSER BUTTONS
browser.back()      Clicks the Back button.
browser.forward()   Clicks the Forward button.
browser.refresh()   Clicks the Refresh/Reload button.
browser.quit()      Clicks the Close Window button.
"""
###################################
"""
### Project: Command Line Editor
"""
"""
### Project: Image Site Downloader
"""
"""
### Project: 2048
https://play2048.co/
"""
"""
### Project: Link Verification
"""