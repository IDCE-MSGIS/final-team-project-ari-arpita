# Place necessary comments and code here. 

# Name: Ariana Nicholson

# Assignment title: Lab 1

# Time to complete: 45 min

# Description: This script calculates the rainfall in gallons on a small plot of land in a one inch rainstorm.For our final project will be focusing on lab 3 about calculating the runoff from any given rainfall. We will be adding a few aspects. First, we will define it as a function. Then, we will create options for user input of the variables of plot length in feet, plot width in feet, and rainfall in inches. Then, we will have it do the proper conversions in the script from feet to inches, and cubic inches to gallons. Finally, we will give output in gallons. We are also considered adding snowfall as another input option, which we will explore when we create our program. 

#Introdution
print "Welcome to the runoff calculator! Follow the on-screen instructions to find the rainfall in gallons from any sized rectangular area."
print "     "

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

#Calculating square inches of rainfall and snowfall

snowfallin = input_snowfall
snowin = snowfallin * areain
watersnowin = snowin / 10

rainfallin = input_rainfall
waterin = rainfallin * areain

#Converting square inches to gallons
snowwatergal = (watersnowin * )
watergal = (waterin * 0.004329)

#Printing the final results
print "     "
print "You entered the length as:", input_length, "feet"

print "You entered the width as:", input_width, "feet"

print "You entered the rainfall as:", input_rainfall, "inches"

print "     "
print "Therefore:"
print waterin, "cubic inches of water fell."

print "This is eqaul to ", watergal, "gallons."
