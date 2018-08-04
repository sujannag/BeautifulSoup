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
html_page = urlopen("https://www.fortuneindia.com/fortune-500/company-list/indian-oil-corporation?year=2017")
soup = BeautifulSoup(html_page, "html5lib")
# print(soup) 
for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
    all_links.append(link.get('href'))
    # print(link.get('href'))
    # print(link.getText())
    dict_all_links[link.getText().strip()] = link.get('href')
    
# print(dict_all_links)
number_of_links = len(dict_all_links)
# print(number_of_links)


# if any link contains the main_url, puch it to the relevant links list.
main_url = "www.fortuneindia.com/fortune-500/company-list/"

for key, value in dict_all_links.items():
	if main_url in value:
		# print(key, value)
		dict_relevant_links[key] = value

# Update a CSV file
FORTUNE_CSV = 'fortune.csv'

if os.path.exists(FORTUNE_CSV):
	print('File Exists, delete the old file')
	os.remove(FORTUNE_CSV)

csv_fortune = open(FORTUNE_CSV, 'a')

# Update the header for the CSV
# Company Name, Revenue, % Change, Net Operating Income, % Change, Profit, % Change, Assets, % Change, Net Worth, % Change,
# Equity Dividend,  % Change, Employee Cost,  % Change
csv_fortune_writer = csv.writer(csv_fortune, delimiter = ',', lineterminator = '\r\n', quotechar = '"')
csv_fortune_writer.writerow(['Rank', 'Company Name', 'Revenue', '% Change', 'Net Operating Income', '% Change', 'Profit', '% Change', 'Assets', '% Change',
							'Net Worth', '% Change', 'Equity Dividend', '% Change', 'Employee Cost', '% Change'])

# Find the tables from the links.
rank = 0; company_name = ''
revenue = 0; revenue_change = 0
net_operating_income = 0; net_operating_income_change = 0
profit = 0; profit_change = 0
assets = 0; assets_change = 0
net_worth = 0; net_worth_change = 0
equity_dividend = 0; equity_dividend_change = 0
employee_cost = 0; employee_cost_change = 0

for key, value in dict_relevant_links.items():
	# print(key)
	rank = rank + 1
	company_name = key
	temp_list = []

	html_page = urlopen(value)
	soup = BeautifulSoup(html_page, "html5lib")

	for row in soup('table')[0].findAll('tr'):
		tds = row('td')

		# ignore the first row, contains the "Parameters, Rs. Crore and % Change"
		# print(row())

		temp_list.append(tds[1].text)
		temp_list.append(tds[2].text)

	
	temp_list[0] = rank
	temp_list[1] = company_name
	print(temp_list)
	csv_fortune_writer.writerow([temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7],
								temp_list[8], temp_list[9], temp_list[10], temp_list[11], temp_list[12], temp_list[13], temp_list[14], temp_list[15]])
	# exit(0)
	# csv_fortune_writer.writerow([rank, company_name, revenue, revenue_change, net_operating_income, net_operating_income_change,
	# 	profit, profit_change, assets, assets_change, net_worth, net_worth_change, equity_dividend, equity_dividend_change, 
	# 	employee_cost, employee_cost_change])







