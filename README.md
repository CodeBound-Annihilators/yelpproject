# Yelp project

### Goal: To predict the health inspection scores of restaurants in San Antonio, TX using yelp data

### PIP INSTALLS THAT YOU MIGHT NEED TO MAKE:

geopandas,
descartes,
shapely,
folium,
Levenshtein.


#### Quick Run Through (Uses our aggregated datasets instesad of creating them from scratch):
##### For a Quick Run Through, Run these jupyter notebooks in the order below.

 - 1_create_health_and_inspector_dataframe.ipynb
 - 2_create_yelp_dataframe.ipynb	
 - 3_levenshtein_merge_yelp_and_health_data.ipynb
 - 4_Master_Model.ipynb
 - 5_exploration.ipynb


### Creating datasets from scratch (scraping inspector name from links in CSV and getting Yelp data from Fusion API)
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

      - ##### The amount of health establishments vs the aquisistion of yelp is uneven due to the fact that health inspections apply to any place that will sell food including such establishments that may just have a vending machine. We will be discarding these establiushments for this model.

      The results from the webscraping were appended to the manually procured health inspection data into a file titled: health_inspector_combined.csv


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
 
 The results were stored in a file named 'yelp.csv'

#### Working with the API Data From JSON ####

Imports: JSON, numpy, pandas

From the JSON library we imported the JSON from the Yelp API. We created an empty data frame with defined columns to provide an easier path for the JSON data to be created. Having the defined columns prior to attempting to extract the information would make for easier data compiling. We extracted the file using a loop to extract the data. 

In order to extract the different categories that the restaurants belonged to, it was necessary to create an empty dictionary and list. Using a series of embedded for loops, we extracted each category name, placed them into a list, and put it in a new column in the data frame. From that column, we created a loop that extracted each category and placed it within a list.




2. Prep

### Preparing the dataframes to join on one another

### Installs ###

pip install Levenshtein

A decision was made to join the data using by comaring the Levenshtein distance of certain words in the name and address of each location. More about Levenshtein distance can be found here:
   
    Levenshtein distance (https://www.python-course.eu/levenshtein_distance.php)

Steps involved in prepping and cleaning the data:
1) Extracting Yelp API fusion data from the JSON file into a working data frame
2) Cleaning particular rows using a combination of string methods and regex.
3) Breaking down the heatlh department addresses and Yelp API addresses into seperate components. 
    i.e. 1600/Pennsylvania/Ave  We chose to eliminate city/state because it only added noise to the model.
4) Standardizing all columns that contained string objects (all lower case, stripping necessary white space, etc)
5) Stemming and Lemmatizing restaurant names and addresses. This included eliminating articles such as A/An/The, popular filler words like of/on/in as well as eliminating their Spanish counterparts given the influence of Spanish/Mexican culture in San Antonio. For addresses, it was imperative to examine the data and find common misspellings (hyw instead of hwy) and correct them as well as eliminating suffixes like ct, blvd, st, bvd and ave/av

These cleaning steps allowed us to successfully merge the information by using the Levenshtein distance. Short explanation of it: It's like a Rubix cube computation for changing from one word to another. ALso called an edit distance, the ideal distance in a merge like this would be zero. However, this wasn't the case for us, so we had to cycle between cleaning and rerunning the data through the Levenshtein function. Additionally, we ran multiple columns through the function. Specifically, we used the restaurant name and address columns from each dataframe to increase the chances of getting matches. This distance for the name column ended up as anything less than 7 and the address distance was everything less than a distance of 4. 

### ANOTHER WESBITE THAT EXPLAINS HOW THE LEVENSHTEIN FUNCTION WORKS ###
https://medium.com/@ethannam/understanding-the-levenshtein-distance-equation-for-beginners-c4285a5604f0

Post merge you will see that the number of rows in your merged dataframe will have grown significantly. This is a normal output of using the Levenshtein function. The next step is to drop the non matching columns and duplicates in the dataframe to have a fully merged dataframe. 

### MODELING ###

### BINNING SCORES TO RUN ANALYSIS

To use a classification model, we knew that we'd have to bin our scores. What we initially could not decided upon was the appropriate number of bins to use. Our first thought was to bin each individual number from 100 - 90, and a final bin of 89 and below. However, results of that produce a model that would not beat the baseline. We noted the importance of the scoring of 100 and from there created three additional bins by way of trail and error to create consistency in the value counts. We ended up with the following bins and counts:

100 : 447

96-99 : 697

92-95 : 608

<92 : 657

BASELINE MODEL: We created a baseline model by taking the bin with the highest number of entries and divided that number by the total number of data points : 755/2409 == .3134. We used this percentage as our baseline.


MODEL ONE: Using Yelp Data

We used a decision tree model first with a RANDOM STATE of 42. The hyper parameters passed included a max depth of 5, min_samples_leaf=1, min_samples_split=2. 

This produced a model with an accuracy of .36. An improvement over the baseline model but having discovered that the relationship between the inspector and the scores they give was significant, we decided to create a feature that took into account the likelihood of an inspector assigning a score in a bin and used those features in the same classification model. This resulted in a accuracy score on the test data of .41.

### Limitations of the Model

We were unable to find a coherent method to classify the food categories of each restaurant. Using relative geographic data from the health department files did not improve the model to a greater extent than the inspector score probabilities did. 

