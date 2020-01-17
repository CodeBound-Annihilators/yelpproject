# Yelp project

### Goal: To predict the health inspection scores of restaurants in San Antonio, TX using yelp data

*3,200 restaurants in San Antonio*
#### Prerequisites:

#### Getting started:
1. Acquire Data

#### Webscraping and Health Inspection Reports #####

 File: inspector_acquire.py

Imports: pandas
requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bsoup
re
json

    - The health inspector scores are publically available at https://www.sanantonio.gov/Health/News/RestaurantReports#229312766-2017, we downloaded the excel files and combined the health inspection reports from 2017 to 2019. To merge the files, we manually combined the Excel files from the website according to year and quarter. This decision was made to divide the data in this manner to make the web craping process more managable for our computers. 
    - To get more details available in the Excel files about the health inspection reports (inspector, number of violations, and addresses of the restaurants), we decided to scrape that information from the website. Using **selenium**, **phantomjs drivers**, we created a webscraper to go scrape the available web links located in teh Excel files to create a pandas dataframe to get our desired information, with the end goal being appending this information to dataframes created from the other health department website information and from the Yelp API.

        In order to use Selenium, the user needs to **-pip install Selenium** onto their computer. Additionally, the use of the PhantomJS Driver also requires a donwload from. 
        
        ***Download PhantomJS at:*** https://phantomjs.org/download.html

        The choice of Selenium over Beautiful Soup boiled down to personal preference and did not come at the cost of efficiency. The decision to use the Phantom JS driver was made because it provided better speed using the request method. **make sure to allow phantomjs in your secuirty preferences**
    - Using the available API from the Yelp website to get the information we needed to predict our target variable: Health inspector code. Yelp would only allow use to acquire 1,000 per inquiry, but by doing seperate inquires by type of reastaurant. By pulling each type of restaurant we are able to get the information needed (about 3,000 of the establishments in San Antonio)

      - ##### The amount of health establishments vs the aquisistion of yelp is uneven due to the fact that health inspections apply to any place that will sell food including such estbaliushments that may just have a vending machine. We will be discarding these establiushments for this model.

#### The Joys of using the Yelp Fusion API ####

On advice of the instructional staff, we opted to use the Yelp Fusion API to collect the restaurant data for San Antonio. The website for the Yelp API is: 

https://www.yelp.com/fusion

Getting started:
	The first order of business to utilize the API is to “create an APP” after clicking on the “Get Started” link on the homepage. The website wants you to fill out some basic information so it has an idea of what you’re using you’re their API for. Filling out this form generates your Client ID and API key for you to use when making requests to the API. Take these two pieces of information and create an env.py (what whatever-you-want-to-call-it.py) file to import into your script. Add this file to your gitignore file to protect your identity. While there should not be any sensitive information in your client ID or in you API, it is a best practice to guard this information for when these keys do contain personal/sensitive information. 

Basic Searches In Yelp Fusion

https://www.yelp.com/developers/documentation/v3/business

The Yelp API has a basic search based on what they call “Endpoints”. Those of you with more experience dealing with API’s and the internet in general are probably familiar with this terminology, but I (Paddy) wasn’t, so it took me a minute or so to figure out what I was working with. My initial assumption was that by searching for restaurants under the category endpoint would provide the necessary results from the API. However, there were some limitations in place by Yelp that made it necessary to find workarounds to acquire a dataset of enough robustness to be feasible for the project. Yelp Fusion limits their total search results to 1,000, irrespective the number of offsets and limits place in your search request. Additionally, there was no way of running the same request and knowing whether you’d receive the same data again or a different set of data. To work around this limitation, we decided to do a more advanced search by specifically naming 200 different categories that we suspected would both have high numbers of restaurants counts as well as be present in the health inspection reports. To accomplish this, we created a list for all the categories and passed a loop through it.

BE PREPARED FOR THIS LOOP TO RUN FOR A LITTLE BIT

CAVEAT: We are unfamiliar with how the request process works under the hood, so we cannot guarantee that the results you will obtain will be the results we obtained. We suspect that the results will be the same, if not very similar.


Working with the API Data From JSON

Imports: JSON, numpy, pandas

From the JSON library we imported the JSON from the Yelp API. We created an empty data frame with defined columns to provide an easier path for the JSON data to be created. Having the defined columns prior to attempting to extract the information would make for easier data compiling. We extracted the file using a loop to extract the data. 

In order to extract the different categories that the restaurants belonged to, it was necessary to create an empty dictionary and list. Using a series of embedded for loops, we extracted each category name, placed them into a list, and put it in a new column in the data frame. From that column, we created a loop that extracted




2. Prep
    ### Joining the Data
    Using the address as primary key to join between the dataframes
    - 
    -
    Levenshtein distance (https://www.python-course.eu/levenshtein_distance.php)