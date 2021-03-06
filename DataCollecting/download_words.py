import functions
import pandas as pd 
import sys
from tqdm import tqdm
from selenium import webdriver
import string
import re
import time
from bs4 import BeautifulSoup
import os
import requests

"""
#ONLY USE THIS FUNCTION IF YOU HAVE THE CHROMEDRIVER
def get_urls_from_topic_page():
	base_url = 'https://speeches.byu.edu/topics/?L='
	letters = string.ascii_uppercase
	
	driver = webdriver.Chrome('/Users/benjafek/Desktop/MakePopularityCSV/cs478/chromedriver')
	
	talks_we_want = []

	try:
		for letter in letters[:1]:
			driver.get(base_url+letter)
			soup = BeautifulSoup(driver.page_source, 'html.parser')
			all_text = str(soup)
			talks_on_page = re.findall(r'\/talks\/[a-z\_\-]+?\/', all_text)
			talks_we_want.extend(set(talks_on_page))

			time.sleep(2)

	finally:
		driver.quit()

	return list(set(talks_we_want))
"""


def download_talks(list_of_urls):
	l = []
	for url in list_of_urls:
		print('Downloading URL {}'.format(url))
		
		fname = '{}.html'.format(url.split('/')[2])
		if not os.path.isfile(fname):
			link = 'https://speeches.byu.edu' + url
			text = requests.get(link).text
			html = BeautifulSoup(text, 'html.parser')
			
			try:
				speech = str(html.meta['content']) #should be unnecessary with python3 TODO.
			except KeyError:
				return 'BAD'

			with open('Speeches/{}'.format(fname), 'w') as outfile:
				outfile.write(text)
			with open('JustWordsSpeeches/{}'.format(fname), 'w') as outfile:
				outfile.write(speech)

		else:
			print ('already exists...')
			pass

	return l 

if __name__ == '__main__':
	#whole_list = get_urls_from_topic_page()
	new_list = ['/talks/cassy-budd_on-failing-and-finishing/']
	download_talks(new_list)