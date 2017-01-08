import datetime
from helper import getSoupObj


QTR_MAP = {
		'jan.' 	: '1',
		'feb.' 	: '1',
		'march' : '1',
		'april' : '2',
		'may'	: '2',
		'june'	: '2',
		'july'	: '3',
		'aug.'	: '3',
		'sept.'	: '3',
		'oct.'	: '4',
		'nov.'	: '4',
		'dec.'	: '4',
		'1' 	: '1',
		'2' 	: '1',
		'3' 	: '1',
		'4' 	: '2',
		'5' 	: '2',
		'6' 	: '2',
		'7' 	: '3',
		'8' 	: '3',
		'9' 	: '3',
		'10'	: '4',
		'11'	: '4',
		'12'	: '4'
}


def findCurrentQtrYr(eps_dict):
	month = datetime.date.today().month
	year = datetime.date.today().year
	qtr = int(QTR_MAP[str(month)])

	updated_eps_dict = {}

	for i in xrange(0, 9):
		if qtr == 0:
			qtr = 4
			year = year - 1

		qtr_yr = returnQtrYr(qtr, year)
		qtr = qtr - 1

		try:
			updated_eps_dict[qtr_yr] = eps_dict[qtr_yr]
		except KeyError:
			continue;
		
	for k in updated_eps_dict:
		print k + " : " + updated_eps_dict[k]

	return updated_eps_dict


def returnQtrYr(qtr, yr):
	return "Q" + str(qtr) + " " + str(yr)


def qtrChange(eps_dict):
	month = datetime.date.today().month
	year = datetime.date.today().year
	qtr = int(QTR_MAP[str(month)])

	eps_qtr_change_list = []

	for i in xrange(0, 5):
		if qtr == 0:
			qtr = 4
			year = year - 1

		qtr_yr = returnQtrYr(qtr, year)
		old_qtr_yr = returnQtrYr(qtr, year-1)
		qtr = qtr - 1

		try:
			current_qtr_eps = float(eps_dict[qtr_yr])
			old_qtr_eps = float(eps_dict[old_qtr_yr])
			eps_percent_change = ((current_qtr_eps - old_qtr_eps) * 100)/ old_qtr_eps
			eps_qtr_change_list.append(int(eps_percent_change))
		except KeyError:
			continue;

	print eps_qtr_change_list

	return eps_qtr_change_list

def acceleratingEPS(eps_qtr_change_list):
	count = 0
	for i in xrange(0,3):
		if eps_qtr_change_list[i] > eps_qtr_change_list[i+1]:
			count = count + 1
		else:
			break
	
	return count

def ychartsEPS(stock_quote):
	ycharts_url = "https://ycharts.com/companies/" + stock_quote.upper() + "/eps"
	ycharts_financials_soup = getSoupObj(ycharts_url)

	eps_dict = {}

	if ycharts_financials_soup:
		eps_td_arr =  ycharts_financials_soup.find("div", {"id": "dataTableBox"}).findAll("td")
		for i in xrange(len(eps_td_arr)):
			text_str = eps_td_arr[i].text

			if (i%2 == 0):
				qtr_yr = text_str.split(",")
				qtr = qtr_yr[0].split(" ")[0]
				yr = qtr_yr[-1].strip()

				key = returnQtrYr(QTR_MAP[qtr.lower()], yr)

			else:
				value = text_str
				eps_dict[key] = value

	updated_eps_dict = findCurrentQtrYr(eps_dict)
	eps_qtr_change_list = qtrChange(updated_eps_dict)
	count = acceleratingEPS(eps_qtr_change_list)
	print count


stock_quote = raw_input("Stock Quote:")
ychartsEPS(stock_quote)