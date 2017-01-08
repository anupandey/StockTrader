from helper import getSoupObj

# Nasdaq
stock_quote = raw_input("Stock Quote:")
nasdaq_url = "http://www.nasdaq.com/symbol/"
nasdaq_stock_url = nasdaq_url+stock_quote.lower()+"/ownership-summary"
soup = getSoupObj(nasdaq_stock_url)

institutional_ownership = soup.find("td", {"class": "callout-large"}).contents
print "Institutional Ownership : " +str(institutional_ownership[0])
