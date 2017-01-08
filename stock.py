#!/usr/bin/python

class Stock:
   'Common base class for all stocks'
   stock_count = 0

   def __init__(self, name, symbol):
      self.name = name
      self.symbol = symbol
      self.zack_rank = 0
      self.thestreet_rank = 0

      Stock.stock_count += 1
   
   def displayCount(self):
     print "Total Stocks %d" % Stock.stock_count

   def displayStock(self):
      print "Name : ", self.name,  ", Symbol: ", self.symbol

   def setTheStreetRank(self, rank):
      self.thestreet_rank = rank