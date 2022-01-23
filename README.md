# Diction & Dictionary Scrapping Problem

Write an application which, when given a web page will download the text on it and output a sorted list of the unique words on the page, with counts of the occurrences.


## Solution
To solve this problem, I developed a web crawler application in Python, which will take the URL of 
a given page from the console and print back the required output.

To begin we need 3 modules: 
 1. **requests**: This will be used to send HTTP/1.1  requests to our select url.
 2. **beautifulsoup4**: To pull data out of the HTML/XML page and parse it.
 3. **Counter** from **collections** for the counting operations

```python
import requests
from bs4 import BeautifulSoup
from collections import Counter
```
Next, we will write a ***crawl*** method defining the web-crawler, which will fetch the information from the webpage. This method has a ***wordlist*** list to store the fetched contents.

To ping the requested url we create a ***beautifulSoup*** object  with an html parser to return html content then strip all the text content which is embedded in the div tags.

We then convert the text content into lowercase sentences and convert the sentences into a list with the ***split()*** function. The resulting text is then appended onto our wordlist list.
```python
def crawl(url):
    # empty the wordlist variable to store the fetched contents
    wordlist = []
    source_code = requests.get(url).text



    # Create the beautifulSoup object to ping the requested url for data
    soup = BeautifulSoup(source_code, 'html.parser')

    # Fetch all the resulting text in <div> tags 
    for each_text in soup.findAll('div'):
        content = each_text.text

        # use split() to break the sentence into
        # words and convert them into lowercase
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clear_symbols(wordlist)
```
Next, We define a second method ***clear_symbols()*** which will strip our text of all unnnecessary symbols we have defined in the variable ***symbols*** and store the result in the ***clean_list***  which we will pass onto our next method to make a dictionary with all the unique words and their count. 

```python
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
```
 Our third method ***create_dictionary()*** will iterate through the clean_list list and call the Counter module which will store all the unique words and their count as ***key:value*** pairs in a dictioanary. 

The keys are assigned to the words while the value is assigned to the individual word count before finally printing the result to the console.
```python
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
```

   
## Example
To try out this application you can clone it from this 
[url](https://github.com/Joseph-Mutua/problem_set_3) into your project folder.

```bash
git clone <url>
```
To run the code simply navigate to the project folder on a text editor of your choice and replace the ***url*** parameter at the bottom with the url of your choice.

For this example I used the [pesapal homepage](https://www.pesapal.com/).
```python
# Driver code
url="https://www.pesapal.com/"
```
Next, jump back into your terminal, navigate to the application folder and run the program. That's it! 
```
~/problem_set_3$ python3 crawler.py
'nfc': 4, 'modes': 4, 'fitbit': 4, 'google': 4, 'integrate': 4, 'systems': 4, 'oracle': 4, 'micros': 4, 'compulynx': 4, 'microsoft': 4, 'amx': 4, 'connect': 4, 'during': 4, 'pickup': 4, 'upon': 4, 'delivery': 4,...

```
