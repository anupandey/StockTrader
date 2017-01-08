from helper import getSoupObj

# Zack rank

def getZackStockUrl(stock_quote):
	return "http://www.zacks.com/stock/quote/" + stock_quote

def isZackDown():
	zack_stock_url = getZackStockUrl("AMBA")
	soup = getSoupObj(zack_stock_url)

	if type(soup) is int:
		return 1
	return 0

def getZackRank(stock_quote):
	zack_stock_url = getZackStockUrl(stock_quote)
	zack_rank = 10;
	try:
		soup = getSoupObj(zack_stock_url)
		zack_rank_list = soup.find("div", {"class": "zr_rankbox"}).find("p").contents
		zack_rank = zack_rank_list[0].split(":")[1].strip().split("-")[0]
	except AttributeError:
		pass

	try:
		zack_rank = int(zack_rank)
	except ValueError:
		zack_rank = 10 # Case - NA
	return zack_rank

def getZackData(stock_quote, id_name):
	zack_stock_url = getZackStockUrl(stock_quote)
	soup = getSoupObj(zack_stock_url)

	stock_activity_soup = soup.find("section", {"id": id_name})
	for tr_soup in stock_activity_soup.findAll("tr"):
		for td in tr_soup.findAll('td'):
			print str(td.findAll(text=True)[0]) + " ",
		print

#stock_quote = raw_input("Stock Quote:")
#print getZackRank(stock_quote)
#getZackData(stock_quote, "stock_activity")
#getZackData(stock_quote, "stock_key_earnings")
