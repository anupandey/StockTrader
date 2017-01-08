from BeautifulSoup import BeautifulSoup
import urllib2
import requests

import datetime

def getSoupObj(page_url):
	result = requests.get(page_url)
	
	if result.status_code == 200:
		page_soup = BeautifulSoup(result.content)
		return page_soup
		
	return


def getEPSData(url, eps_dict):
	cnnmoney_financials_soup = getSoupObj(url)

	if cnnmoney_financials_soup:
		key_metric_headers = cnnmoney_financials_soup.find("tr", {"id": "periodHeaders"}).findAll('th')
		eps_content_arr =  cnnmoney_financials_soup.find("div", {"id": "financial_statement"}).find("tbody").findAll("tr")[-2].contents[1:5]

		for x, y in zip(key_metric_headers, eps_content_arr):
			header_value = x.text.split(" ")[-1]
			if (len(header_value) == 5):
				header_value_year =  ''.join(list(header_value)[1:])
				header_value_qtr = "Q" + header_value[0:1]
				header_value = header_value_qtr + " " + header_value_year
			eps_dict[header_value] = y.text

	return eps_dict


def getOwnershipDetails(url, eps_dict):
	cnnmoney_ownership_soup = getSoupObj(url)

	if cnnmoney_ownership_soup:
		for ownership_row_soup in cnnmoney_ownership_soup.find("div", {"id": "wsod_shareholderTable"}).findAll("tr"):
			eps_dict[ownership_row_soup.contents[0].text] = ownership_row_soup.contents[1].text

	return eps_dict


def cnnmoneyFinancials(stock_quote):
	eps_dict = {}

	#cnnmoney_financials_url = "http://money.cnn.com/quote/financials/financials.html?symb=" + stock_quote
	#eps_dict = getEPSData(cnnmoney_financials_url, eps_dict)
	
	#cnnmoney_financials_url = "http://money.cnn.com/quote/financials/financials.html?symb=" + stock_quote + "&dataSet=IS&period=Q"
	#eps_dict = getEPSData(cnnmoney_financials_url, eps_dict)

	# Institutional
	cnnmoney_ownership_url = "http://money.cnn.com/quote/shareholders/shareholders.html?symb=" + stock_quote + "&subView=institutional"
	eps_dict = getOwnershipDetails(cnnmoney_ownership_url, eps_dict)
	
	for k in eps_dict:
		print k + " : " + eps_dict[k]

	# EPS forecast
	#cnnmoney_url = "http://money.cnn.com/quote/quote.html?symb" + stock_quote
	#cnnmoney_soup = getSoupObj(cnnmoney_url)

	#if cnnmoney_soup:
	#	print cnnmoney_soup.find("div", {"id", "wsod_snapshotView"}YCHARTS )


stock_quote = raw_input("Stock Quote:")
cnnmoneyFinancials(stock_quote)
