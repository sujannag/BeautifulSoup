from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import csv
import os, os.path
 
# Store all the links from the webpage
dict_all_links = {}
all_links = []
number_of_links = 0

# Store all the relevant links from the webpage
relevant_links = []
dict_relevant_links = {}
number_of_relevant_links = 0

# Get all the links from the webpage 
html_page = urlopen("http://www.fortuneindia.com/fortune-500/company-list/reliance-industries?year=2017")
soup = BeautifulSoup(html_page, "html5lib")
 
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    all_links.append(link.get('href'))
    # print(link.get('href'))
    # print(link.getText())
    dict_all_links[link.getText().strip()] = link.get('href')
    

number_of_links = len(dict_all_links)

# if any link contains the main_url, puch it to the relevant links list.
main_url = "www.fortuneindia.com/fortune-500/company-list/"

for key, value in dict_all_links.items():
	if main_url in value:
		dict_relevant_links[key] = value

# Find the tables from the links.
for key, value in dict_relevant_links.items():
	# print(value)
	html_page = urlopen(value)
	soup = BeautifulSoup(html_page, "html5lib")
	for row in soup('table')[0].findAll('tr'):
		tds = row('td')
		print (tds)






