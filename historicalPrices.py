import ystockquote
from plotgraph import barchart

dict = ystockquote.get_historical_prices('AMBA', '2015-07-5', '2015-07-18')

stockHighList = []
stockLowList = []
stockCloseList = []
stockOpenList = []
dateList = []
count = 1
for date, priceDict in dict.iteritems():
	dateList.append("Day" + str(count))
	stockHighList.append(float(priceDict['High']))
	stockLowList.append(float(priceDict['Low']))
	stockCloseList.append(float(priceDict['Close']))
	stockOpenList.append(float(priceDict['Open']))
	count = count + 1

print dateList
print stockLowList
print stockHighList

print(ystockquote.get_price('AMBA'))

