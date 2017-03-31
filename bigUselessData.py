from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import urllib2
#from random import randint

#use this counter to sometimes start from a new source
init=0;

def random_amount_of_waiting():
    time.sleep(random.randint(0,10)+1)

def start_new_session():
    list_of_sources = ["https://www.wikipedia.org/","https://www.yahoo.com/","https://www.bing.com","https://www.youtube.com","https://www.google.com","https://www.flickr.com/"]
    which_source = (random.randint(0, len(list_of_sources)))-1

    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

    response = urllib2.urlopen(word_site)
    txt = response.read()
    WORDS = txt.splitlines()

    which_search_term = (random.randint(0, len(WORDS)))-1

    #open Chrome

    #select which place to start
    driver.get(list_of_sources[which_source]);
    #tell it the name of the search box on the screen
    if "yahoo" in list_of_sources[which_source]:
        search_box = driver.find_element_by_name('p')
    elif "wikipedia" in list_of_sources[which_source]:
        search_box = driver.find_element_by_name('search')
    elif "bing" in list_of_sources[which_source]:
        search_box = driver.find_element_by_name('q')
    elif "youtube" in list_of_sources[which_source]:
        search_box = driver.find_element_by_name('search_query')
    elif "google" in list_of_sources[which_source]:
        search_box = driver.find_element_by_name('q')
    elif "flickr" in list_of_sources[which_source]:
        search_box = driver.find_element_by_name('text')

    #put a search term in the search box
    search_box.send_keys(WORDS[which_search_term])
    search_box.submit()
    random_amount_of_waiting() # Let the user actually see something!
    return driver

driver = webdriver.Chrome()

# create an infinite loop
while True:
    if init==0:
        driver=start_new_session()
    # store the current url in a variable
    current_page = driver.current_url
    try:
        # find element using css selector
        links = driver.find_elements_by_xpath("//a[@href]")

        # create a list and chose a random link
        l = links[randint(0, len(links) - 1)]
        print l
        random_amount_of_waiting() # Let the user actually see something!

        # click link
        l.click()
        # check link
        #new_page = driver.current_url #this maybe shouldn't be commented out

        #1 in 10 times, start from a new source again
        num1= random.randint(1, 10)
        if num1==7:
            init=0
        else:
            init=1

        #see if

        if len(driver.window_handles) > 1:
            driver.switch_to_window(driver.window_handles[1])

    except:
        continue

#shouldn't ever get here..but go ahead and quit the page nicely, if you do

driver.quit()
