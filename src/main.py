from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
 
# Get all the links from the webpage 
html_page = urlopen("http://www.fortuneindia.com/fortune-500/company-list/reliance-industries?year=2017")
soup = BeautifulSoup(html_page, "html5lib")
all_links = []
number_of_links = 0
 
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    all_links.append(link.get('href'))

number_of_links = len(all_links)

 
# print(all_links)
# print(len(links))

# Filter the links
# relevant_links = []
# main_url = "www.fortuneindia.com/fortune-500/company-list/"



