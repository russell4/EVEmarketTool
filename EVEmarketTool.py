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
	
	csvFile = args[2] # do I need to check to see if file first? probably
	
	
	return 0

def readMarketExport(csvfile):
	with open(csvfile_name, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=',') #comma is standard with EVE export
	
	
	return marketArray
	
def totalBuySellOrders(marketArr):
	
	totalBuy = 0
	totalSell = 0
	
	for line in marketArry:
		if line[0] is "price":
			# do nothing
		else:
			
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
