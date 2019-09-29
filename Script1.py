# Place necessary comments and code here. 
'''
# Assignment title: Final Project- Web-scraping Weather Forecast
# Date: 09/23/2019
# Description: The script web-scrapes the weather.gov website to extract the 5-Day weather forecast for a given location
# Inputs: Latitude & Longitude in Decimal Degrees
# Outputs: 5-Day Weather Forecast
'''

# import required libraries
import requests
from bs4 import BeautifulSoup

# List to store response
forecast = []

## Provide the latitude and longitude for the location you would like to check the forecast for
## Lat/lon in decimal degrees provided for Worcester, MA
lat =str(input("Please enter the latitude value : "))
lon=str(input("Please enter the Longitude value: "))

#print ("The latitude value entered by the user is : " ),lat
#print ("The longitude vale entered by the user is : " ),lon


# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon
# Check if the URL exists
# print url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})

# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list
for i in weather_forecast:
    i = i.text
    forecast.append(i)

# Print list to remove unicode characters
for day in forecast:
  day = day.replace('CloudyLow','Cloudy Low')
  day = day.replace('High',' High')
  day = day.replace('ChanceShowers', 'Chance Showers')
  day = day.replace('thenPartly', 'then Partly')
  day = day.replace('ShowersLow', 'Showers Low')
  day = day.replace('RainLow', 'Rain Low')
  day = day.replace('LikelyLow', 'Likely Low')
  day = day.replace('thenMostly','then Mostly')
  day = day.replace('MondayNight','Monday Night')
  day = day.replace('TuesdayNight','Tuesday Night')
  day = day.replace('WednesdayNight','Wednesday Night')
  day = day.replace('ThursdayNight','Thursday Night')
  day = day.replace('FridayNight','Friday Night')
  day = day.replace('SaturdayNight','Saturday Night')
  day = day.replace('SundayNight','Sunday Night')
  day = day.replace('ClearLow','Clear Low')
  day = day.replace('IsolatedT-storms','Isolated T-storms')
  day = day.replace('T-stormsLow','T-storms Low')
  day = day.capitalize()
  print day.upper()
