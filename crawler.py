# request module to send HTTP/1.1 requests
# beautifulsoup4 module for parsing HTML/XMLto extract data
# operator module for operator functions
# collections module to implement high-performance container datatypes

import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

# Function defining the web-crawler which will fetch info 
# from a given website and push the resulting contents to the
# second function clear_symbols()

def crawl(url)
    # empty the wordlist variable to store the fetched contents
    wordlist = []
    source_code = requests.get(url).text
    
    # Create the beautifulSoup object to ping the requested url for data
    soup = BeautifulSoup(source_code, 'html.parser')
    
    # Store resulting text in <div> tags with class <entry-content>
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text
 
        # use split() to break the sentence into
        # words and convert them into lowercase
        words = content.lower().split()
 
        for each_word in words:
            wordlist.append(each_word)
        clear_symbols(wordlist)
        
        
# Function to remove all unwanted symbols from the wordlist

def clear_symbols(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
        
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')
            
        if len(word) > 0:
            clean_list.append(word)
            
    create_dictionary(clean_list)
    
    
# Function to create dictionary containing each words count

        


