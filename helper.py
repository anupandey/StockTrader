from BeautifulSoup import BeautifulSoup
import requests

def getSoupObj(page_url):
	result = requests.get(page_url)
	
	if result.status_code == 200:
		page_soup = BeautifulSoup(result.content)
		return page_soup
		
	return result.status_code