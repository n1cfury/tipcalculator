#!/usr/bin/env python


#This is a simple calculator to figure the tip amount per your meal. 
'''
meal = 32.50
tax = .075  
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

#The command below designates how many digits passed the decimal I want displayed. Here, I want to tenths place only (rounded up)
print("%.1f" % total)  '''
def banner():
	print "###### Tip Calculator #########"
	print "Enter the amount when prompted"
	print ""
	
def main():
	banner()
	meal = float(raw_input("How much was your meal? "))			#Asks for cost of meal
	tax = meal * 0.075
	tip = 0.15
	mealtotal = meal + tax
	finaltotal = total + (tip * mealtotal)							#Calculated final total
	print ("Your meal was %s with an added %s for tax.") % (meal, tax)
	print ("Including the tip the meal is %s") % round(finaltotal, 2)

if __name__ == "__main__":
  main()