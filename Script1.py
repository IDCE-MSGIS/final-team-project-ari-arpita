# Name : Ari Nicholson and Arpita Shalini
# Assignment Title : Final project Script 1 -  Web scraping Forecast
# Time taken : 2 Hours.
# Description :  Asking the user to input latitude and longitude and scraping the data from the National Weather website to print the weather conditions of the place enetered with proper spacing and in uppercase. 
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
lat =str(input("Please enter the latitude : "))
lon =str(input("Please enter the Longitude : "))

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

# Print list to remove unicode characters and use of replace function
for day in forecast:
  day = day.replace('CloudyLow','Cloudy Low')                                    #Add spaces within the unicode output
  day = day.replace('High',' High')                                              #Add spaces within the unicode output
  day = day.replace('ThisAfternoon', 'This Afternoon')                           #Add spaces within the unicode output
  day = day.replace('ChanceShowers', 'Chance Showers')                           #Add spaces within the unicode output
  day = day.replace('then', ' then ')                                            #Add spaces within the unicode output
  day = day.replace('ShowersLow', 'Showers Low')                                 #Add spaces within the unicode output
  day = day.replace('Low', ' Low')                                               #Add spaces within the unicode output
  day = day.replace('and', ' and')                                               #Add spaces within the unicode output
  day = day.replace('IsolatedT-storms','Isolated T-storms')                      #Add spaces within the unicode output
  day = day.replace('ShowersLikely', 'Showers Likely')                           #Add spaces within the unicode output
  day = day.replace('Night',' Night')                                            #Add spaces within the name of the day and the timing 
  day = day.replace('BecomingSunny','Becoming Sunny')                            #Add spaces within the unicode output
  day = day.replace('SlightChance','Slight Chance')                              #Add spaces within the name of the day and the timing

  print day.upper()                                                              #Printing the output in Upper Case
