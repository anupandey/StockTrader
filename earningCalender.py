import datetime
import os
import logging
import ystockquote

from helper import getSoupObj

from thestreet import getStreetRank
from zack import getZackRank, isZackDown

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
logfile = 'hello.log'
os.remove(logfile)
handler = logging.FileHandler(logfile)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def getStockSymbolsFromEarningCalender(earning_calender_soup):
	symbol_list = []
	for table_row_soup in earning_calender_soup.findAll("tr"):
		count = 0
		for td_soup in table_row_soup.findAll('td'):
			if count == 1:
				try:
					stock_symbol = str(td_soup.findAll(text=True)[0]).strip()
					if 0 < len(stock_symbol) < 7 and stock_symbol.isupper():
						symbol_list.append(stock_symbol)
				except IndexError as ie:
					continue
			count = count + 1

	return symbol_list

mydate = datetime.date(2015,7,20)  #year, month, day
datestamp = mydate.strftime("%Y%m%d")
earning_calender_soup = getSoupObj("http://biz.yahoo.com/research/earncal/"+datestamp+".html")
if earning_calender_soup:
	symbol_list = getStockSymbolsFromEarningCalender(earning_calender_soup)
	new_symbol_list = []
	for symbol in symbol_list:
		stock_price = (ystockquote.get_price(symbol))
		try:
			stock_price = float(stock_price)
			if stock_price > 20:
				thestreet_rank = getStreetRank(symbol)
				if 0 < thestreet_rank < 6:
					#print symbol
					logger.info('symbol ' + symbol + ' has stock price $' + str(stock_price) + 
							' and Thestreet rank ' + str(thestreet_rank))

					if not (isZackDown()):
						zack_rank = getZackRank(symbol)

						if zack_rank < 4:
							print symbol + str(zack_rank)


		except ValueError:
			pass
