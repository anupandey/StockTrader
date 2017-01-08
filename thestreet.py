# Thestreet rank

from helper import getSoupObj

# THese are buy .. rest all are hold/sell
thestreet_rank_map= {
		'A+' : 1,
		'A'  : 2,
		'A-' : 3,
		'B+' : 4,
		'B'  : 5,
		'B-' : 6
}

def getStreetRank (stock_quote):
	thestreet_url = "http://www.thestreet.com/quote/"
	thestreet_stock_url = thestreet_url + stock_quote + ".html"
	soup = getSoupObj(thestreet_stock_url)

	try:
		thestreet_rank_list = soup.find("span", {"id": "currentRating"}).contents
		thestreet_rank = thestreet_rank_list[0].split(" ")[0]

		if thestreet_rank in thestreet_rank_map:
			return thestreet_rank_map[thestreet_rank]
	except AttributeError:
		pass

	return 10

#stock_quote = raw_input("Stock Quote:")
#print getStreetRank(stock_quote)