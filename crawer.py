#coding=utf-8
import requests
from bs4 import BeautifulSoup
key_words = ['Protein degradation','degradation;proteasome','diabetes','T1D','T2D','glucagon','glucose','hyperglycemia','glycemic','ubiquitin','glycometabolism','metabolism','gluconeogenesis', 'glucolysis']

def get_teams_list(year):
	url = 'https://igem.org/Team_List?year='+year
	print(url)
	result = []
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html,'lxml')
	table_team = soup.find(id='table_team')
	all_url = table_team.find_all('a')
	for url in all_url:
		team_url = url['href']
		team_name = url.text
		if 'team_id' in team_url:
			#print(team_url)
			abstract = check_content(team_url)
			if abstract is not None:
				result.append([team_name, team_url ,abstract])
				print('[+] ',team_name)
	print('[*] ', year, len(result))
	return result
def check_content(url):
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html,'lxml')
	table_abstract = soup.find(id='table_abstract')
	abstract = table_abstract.text
	for key_word in key_words:
		if key_word in abstract:
			return abstract
	return None

import csv
results = []
for year in range(2008,2019):
	results += get_teams_list(str(year))
with open('history.csv', 'w', newline='') as csvfile:
	writer  = csv.writer(csvfile)
	for row in results:
		try:
			writer.writerow(row)
		except:
			print(row)
