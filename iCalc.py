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


meal = float(raw_input("How much was your meal? "))			#Asks for cost of meal
tax = meal * 0.075
tip = 0.15
total = meal + tax
gratuiity = total + (tip * total)							#Calculated final total


print ("Your meal was %s with an added %s for tax.") % (meal, tax)
print ("Including the tip the meal is %s") % round(gratuiity, 2)
