# Name: Ariana Nicholson and Arpita Shalini

# Assignment title: Script 2 final

# Time to complete: 1 hour 30 minutes

# Description: This script calculates the runoff from rainfall and snowfall in gallons on a user defined plot of land, with user defined percipitation levels.

#Introdution
print "Welcome to the runoff calculator! Follow the on-screen instructions to find the perciptation runoff in gallons from any rectangular area.\n"


#Geting user input for plot length and width in feet 
input_length = input ("What is the length of the plot in feet?")
input_width = input ("What is the width of the plot in feet?")

# Calculating the area of the plot of land in inches

lengthin = input_length * 12
widthin = input_width * 12
areain = (lengthin * widthin)

#Getting user input on rain and snow

input_snowfall = input ("How many inches of snow fell?")
input_rainfall = input ("How many inches of rain fell?")

#Calculating square inches of rainfall and snowfall. To calculate snow, we divide the number of inches by 10. Source: http://www.maynardlifeoutdoors.com/2013/02/snow-to-water-conversion.html

snowfallin = input_snowfall
snowin = snowfallin * areain
watersnowin = snowin / 10

rainfallin = input_rainfall
waterin = rainfallin * areain

#Converting square inches to gallons
snowwatergal = (watersnowin * 0.004329)
watergal = (waterin * 0.004329)

#adding up total of snow and rain

totalgal = watergal + snowwatergal

#Printing the final results

print "\nYou entered the plot length as:", input_length, "feet"

print "You entered the plot width as:", input_width, "feet"

print "You entered the rainfall as:", input_rainfall, "inches"

print "You entered the snowfall as:", input_snowfall, "inches"


print "\nTherefore: \nThere was", totalgal, "gallons of water runoff on this plot of land."