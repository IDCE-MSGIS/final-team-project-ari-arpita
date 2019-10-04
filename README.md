#### Names: Ariana Nicholson and Arpita Shalini
#### Assignment title: Final Project
#### Due date: October 6th, 2019
#### Time to complete (Read Me): 1 hour

## Final Project: Script 1
### Web-scraping Weather Forecast Information with Python

For script 1, you can explain the purpose of the script, how well it functioned (or if it didn’t), and whether or not you might use something like this in the future.

In this lab, you will work with a script that scrapes the 5-day weather forecast from the National Weather Service website. The script extracts information from multiple elements listed under the same class name using the BeautifulSoup library. 

- Copy the **NWS_WeatherForecast.py** file and paste it into the online Python compiler: https://repl.it/languages/python
Make sure you are using Python version 2.7. You can check the Python version in the compiler window on the right.

- Read the description and comments in the script to understand the purpose of the script

- Run the script. You will see some packages being installed in the compiler window when you run it for the first time.

- The script returns the 5-day forecast for Worcester, MA (Lat: 42.2634, Lon: -71.8022) with the latitude and longitude information provided. Using the latitude and longitude values, it generates the following URL through string concatenation: https://forecast.weather.gov/MapClick.php?lat=42.2634&lon=-71.8022

- Open this URL in a Firefox or Chrome browser. Locate the information that is being outputted in our script. Right click on this and select the Inspect Element option. This will launch the Inspector window that helps locate different elements on the page.

- Notice that all forecast containers in this section are located in the _forecast-tombstone_ class inside the _li_ tag. In order to scrape multiple elements listed under the same class name, we utilize the _findAll()_ function from BeautifulSoup. The tag and class names are required arguments for this function.

### Edit the NWS_ WeatherForecast.py script to add the following functionality:
1. Take latitude and longitude values as inputs in decimal degrees from user

2.	Convert the latitude and longitude values to strings to generate the URL for the selected location. Pass this URL as an argument in the _get()_ request.

3.	The returned forecast information did not preserve its spacing during the scraping process. Using the _replace()_ function, fix any spacing issues with the output

4.	Convert the final output to uppercase

Remember to update the Script1.py file to include comments and documentation in your script to tell me what it’s doing!

## Final Project: Script 2
### Runoff Calculator - Reboot of Lab 1
This script calculates the runoff from rainfall and snowfall in gallons on a user defined plot of land, with user defined precipitation levels. The calculator begins with a script introducing the goal of the calculator, and then a prompt to input the length of the plot in feet. Then, the calculator asks for an input of the width of the plot in feet. The script then converts these numbers to inches and multiplies them together to get the area in inches squared. 

In the next section of code, the script asks the user to input rain and snow in inches. Then, the script converts inches of snowfall into inches of water. Then, the script converts both of these numbers to cubic inches of water by multiplying them by the area in inches that it previously calculated. 

Finally, the script multiples both numbers by the decimal needed to convert cubic inches into gallons (0.004329). The script adds these numbers, and provides the user with an output of the numbers that they entered, and the total gallons of water runoff based on the numbers that the user entered. 

This script has several changes from the lab to help with functionality. First, it includes clear instructions given to the user throughout the process, so that the user understand when to enter which number. Second, this script incorporates user input, so that the user does not have to code in Python to change the inputs. Third, the script clear outputs both what the user inputted (so the user can check their work), as well as what the total gallons would be. Finally, we added snowfall, utilizing the average measurements for snowfall to water conversion. 

There were many challenges throughout this process. Originally, we thought we would define a function in order to make the script run. However, after some fiddling we realized that it functioned just fine without defining a function, and decided to keep it simple. The largest challenge was deciding how to include snowfall in the calculator. First, we tried to use an if/elif/else statement to ask the user if the wanted to input snowfall or rainfall. However, we could not figure out how to use user input within an if/elif/else statement. Additionally, we realized often there are times when it both rains and snows. With this in mind, we decided to have the script always ask the user each question, with an option of typing zero as an answer to either. This way, we can add up both, and calculate the total runoff. 

When looking into conversions for snowfall into water, we came across a 'rule of thumb - ten inches of snow melts down to one inch of water. We found this online at Maynard Life Outdoors (http://www.maynardlifeoutdoors.com/2013/02/snow-to-water-conversion.html) as well as other websites we consulted. This article goes on to say that not all snow is equally wet - snow may be powdery or icy or slushy. This all impacts how much water is created when the snow melts. We did not include this as a factor in our script, but would be a good opportunity for further exploration. Perhaps there is a website that characterizes snow based on latitude and longitude, and we could simply ask for these inputs and use web scraping to collect the input data for rain and snow fall. Perhaps there is an official scale of snow quality that we could explain to a user in our calculator, then ask the user to rate the quality of the snow. Based on this, we could use an if/elif/else statement to determine which conversion would be necessary for a certain input. there are many opportunities for expansion of this script.

