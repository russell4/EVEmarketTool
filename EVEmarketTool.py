#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  EVEmarketTool.py
#  
#  Copyright 2019 Russell Brinson <>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import csv

def main(args):
	# args[0] tool name
	# args[1] function to call
	# args[2] file to use
	
	functCall = args[1]
	csvFile = args[2] # do I need to check to see if file first? probably
	
	marketArray = readMarketExport(csvFile)
	
	if functCall == "--total-buy-sell":
		totalBuySellOrders(marketArray)
	
	return 0

def readMarketExport(csvfile_name):
	
	marketArray = list()
	lineCount = 0
	
	with open(csvfile_name, mode='r') as csv_file:
		# csv_reader = csv.DictReader(csv_file, delimiter=',') #comma is standard with EVE export
		csv_reader = csv.reader(csv_file, delimiter=',') #comma is standard with EVE export
		
		for line in csv_reader:
			marketArray.append(line)
				
	return marketArray
	
def totalBuySellOrders(marketArr):
	
	totalBuy = 0
	totalSell = 0
	lineCount = 0
	
	for line in marketArr:
		if line[0] != "price":
			if line[7] == "False":
				totalBuy += 1
			elif line[7] == "True":
				totalSell += 1
			else:
				print("Error on Line " + str(lineCount) + ": " + str(line[7]))

		lineCount += 1

	print("Total Buy Orders: " + str(totalBuy))
	print("Total Sell Orders: " + str(totalSell))
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
