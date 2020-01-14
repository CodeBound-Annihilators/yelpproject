# Yelp project

### Goal: To predict the health inspection scores of restaurants in San Antonio, TX using yelp data

*3,200 restaurants in San Antonio*
#### Prerequisites:

#### Getting started:
1. Acquire Data
    - The health inspector scores are publically available at https://www.sanantonio.gov/Health/News/RestaurantReports#229312766-2017, we downloaded the excel files and combined the health inspection reports from 2017 to 2019. To merge the files, we manually combined the Excel files from the website according to year and quarter. This decision was made to divide the data in this manner to make the web craping process more managable for our computers. 
    - To get more details available in the Excel files about the health inspection reports (inspector, number of violations, and addresses of the restaurants), we decided to scrape that information from the website. Using **selenium**, **phantomjs drivers**, we created a webscraper to go scrape the available web links located in teh Excel files to create a pandas dataframe to get our desired information, with the end goal being appending this information to dataframes created from the other health department website information and from the Yelp API.

        In order to use Selenium, the user needs to -pip install Selenium onto their computer. Additionally, the use of the PhantomJS Driver also requires a donwload from . 

        The choice of Selenium over Beautiful Soup boiled down to personal preference and did not come at the cost of efficiency. The decision to use the Phantom JS driver was made because it provided better speed using the request method. 
    - Using the available API from the Yelp website to get the information we needed to predict our target variable: Health inspector code.     Yelp would only allow use to acquire 1,000 per inquiry, but by doing seperate inquires by type of reastaurant. By pulling each type of    restaurant we are able to get the information needed (about 3,000 of the establishments in San Antonio)