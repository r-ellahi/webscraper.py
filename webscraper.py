import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
        
    #The urlopen () function sends a request to a website and 
    # returns a Response object in which its HTML code is stored, 
    # along with additional data. The response of the function. 
    # read () returns the HTML of the Response object.
    #All the HTML for the website is in the html variable.

        
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("\n" + url)


news =   "https://news.sky.com/"              
Scraper(news).scrape()