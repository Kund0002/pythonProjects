import requests as req
from bs4 import BeautifulSoup as bs
import time

url = "http://quotes.toscrape.com/page/"
max = 10

def scrape(url, max):
    """_summary_

    Args:
        url (string): the url of the page with the page number missing
        max (int): An int for the maximum amount of pages wanted to iterate through
    """
    base_url = url
    for page in range(1, max, 1):
        
        url = base_url + str(page) + "/"
        response = req.get(url)
        
        if response.status_code == 200:
            #Saving the html of the page from the get request
            html_content = response.text
            
            #Taking the sumn and doing sumn
            soup = bs(html_content, 'html.parser')
            
            #Saving the relevant information from the page scrape in relevant variables
            quotes = soup.find_all(class_="text")
            authors = soup.find_all(class_="author")
            
            #Iterating through the lists with the relevant information and printing it out
            for author, quote in zip(authors, quotes):
                print(quote.get_text())
                print("By: " + author.get_text())
                print("---------------------------------------\n")
                
        else:
            #Error handling (needs work)
            print("There has been an error")
            
        #Delay to not overload the server for the page that we are scraping from
        time.sleep(1)
        
if __name__ == "__main__":
    scrape(url, max)