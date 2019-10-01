For script 1, you can explain the purpose of the script, how well it functioned (or if it didn’t), and whether or not you might use something like this in the future.
For script 2, clearly explain what the goal of the script is; what inputs are required; what outputs are expected. Ideally, you’d have a real-life scenario in hand (e.g. “by allowing user input for the script to _______, we ensure that it can be easily run without a user needing to program in Python.”). That is only an example but should give you an idea for what I’m looking for. Additionally, you should describe the process of writing the script: was it easy, hard, what challenges or errors did you face and how did you resolve the issue? If you use any resources to help write your code (e.g. Stackoverflow.com; the text book; etc.) then please describe these in the body of the text. E.g. “After repeated syntax errors, I checked Stackoverflow.com to find that…”  If you can link to a specific thread or page that would be great.

 600 – 800 word write up 

## Final Project: Script 1
### Web-scraping Weather Forecast Information with Python
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
This script calculates the runoff from rainfall and snowfall in gallons on a user defined plot of land, with user defined percipitation levels. The calculator begins with a script introducing the goal of the calculator, and then a prompt to input the length of the plot in feet. Then, the calculator asks for an input of the width of the plot in feet. The script then converts these numbers to inches and multiples them together to get the area in inches squared. 

In the next section of code, the script asks the user to input rain and snow in inches. Then, the script converts inches of snowfall into inches of water. Then, the script converts both of these numbers to cubic inches of water by multiplying them by the area in inches that it previously calculated. 

Finally, the script multiples both numbers by the decimal needed to convert cubic inches into gallons (0.004329). The script adds these numbers, and provides the user with an output of the numbers that they entered, and the total gallons of water runoff based on the numbers that the user entered. 
