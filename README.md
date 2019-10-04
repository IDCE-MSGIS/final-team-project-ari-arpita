#### Names: Ariana Nicholson and Arpita Shalini
#### Assignment title: Final Project
#### Due date: October 6th, 2019
#### Time to complete (Read Me): 1 hour

## Final Project: Script 1
### Web-scraping Weather Forecast Information with Python

This python script enables us to do web-scraping from the National Weather Website. We have asked the user to input the longitude and latitude. Taking the values and web-scraping data, we obtained output with spacing issues. Using the Replace function we have replaced the original output and manipulated it by adding spaces between two words. The last requirement of this project was to print the whole output in Upper Case. Using the .upper( ) we have printed the whole output in uppercase. 

During out initial coding, we printed every day (“Monday”) and night and added the replace function to it so we could get the desired output. Then we managed to just replace ‘night’ with space before and after it. This is how we managed to shorten our code, so that it is easy to read and understand.  

Web scraping has multiple applications. We both are excited to use it collect data for GIS in future.

## Final Project: Script 2
### Runoff Calculator - Reboot of Lab 1
This script calculates the runoff from rainfall and snowfall in gallons on a user defined plot of land, with user defined precipitation levels. The calculator begins with a script introducing the goal of the calculator, and then a prompt to input the length of the plot in feet. Then, the calculator asks for an input of the width of the plot in feet. The script then converts these numbers to inches and multiplies them together to get the area in inches squared. 

In the next section of code, the script asks the user to input rain and snow in inches. Then, the script converts inches of snowfall into inches of water. Then, the script converts both of these numbers to cubic inches of water by multiplying them by the area in inches that it previously calculated. 

Finally, the script multiples both numbers by the decimal needed to convert cubic inches into gallons (0.004329). The script adds these numbers, and provides the user with an output of the numbers that they entered, and the total gallons of water runoff based on the numbers that the user entered. 

This script has several changes from the lab to help with functionality. First, it includes clear instructions given to the user throughout the process, so that the user understand when to enter which number. Second, this script incorporates user input, so that the user does not have to code in Python to change the inputs. Third, the script clear outputs both what the user inputted (so the user can check their work), as well as what the total gallons would be. Finally, we added snowfall, utilizing the average measurements for snowfall to water conversion. 

There were many challenges throughout this process. Originally, we thought we would define a function in order to make the script run. However, after some fiddling we realized that it functioned just fine without defining a function, and decided to keep it simple. The largest challenge was deciding how to include snowfall in the calculator. First, we tried to use an if/elif/else statement to ask the user if the wanted to input snowfall or rainfall. However, we could not figure out how to use user input within an if/elif/else statement. Additionally, we realized often there are times when it both rains and snows. With this in mind, we decided to have the script always ask the user each question, with an option of typing zero as an answer to either. This way, we can add up both, and calculate the total runoff. 

When looking into conversions for snowfall into water, we came across a 'rule of thumb - ten inches of snow melts down to one inch of water. We found this online at Maynard Life Outdoors (http://www.maynardlifeoutdoors.com/2013/02/snow-to-water-conversion.html) as well as other websites we consulted. This article goes on to say that not all snow is equally wet - snow may be powdery or icy or slushy. This all impacts how much water is created when the snow melts. We did not include this as a factor in our script, but would be a good opportunity for further exploration. Perhaps there is a website that characterizes snow based on latitude and longitude, and we could simply ask for these inputs and use web scraping to collect the input data for rain and snow fall. Perhaps there is an official scale of snow quality that we could explain to a user in our calculator, then ask the user to rate the quality of the snow. Based on this, we could use an if/elif/else statement to determine which conversion would be necessary for a certain input. there are many opportunities for expansion of this script.

