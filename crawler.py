# request module to send HTTP/1.1 requests
# beautifulsoup4 module for parsing HTML/XMLto extract data
# Counter from collections to get elements counts

import requests
from bs4 import BeautifulSoup
from collections import Counter

# Function defining the web-crawler which will fetch info
# from a given website and push the resulting contents to the
# second function clear_symbols()


def crawl(url):
    # empty the wordlist variable to store the fetched contents
    wordlist = []
    source_code = requests.get(url).text

    # Create the beautifulSoup object to ping the requested url for data
    soup = BeautifulSoup(source_code, 'html.parser')

    # Store resulting text in <div> tags
    for each_text in soup.findAll('div'):
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


# Function to create dictionary containing each unique word's count
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    # To Get the count for each word in the crawled page stored
    # in the dictionary in key/value pairs
    # Use Counter from collections which converts the elements to
    # keys and values will be the count of the elements

    c = Counter(word_count)

    # Print the word:count key/value pairs to console
    print(c)




# Driver code
url = "https://pesapal.freshteam.com/jobs"
# starts crawling and prints output
crawl(url)
