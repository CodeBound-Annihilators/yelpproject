# Yelp project

### Goal: To predict the health inspection scores of reastaurants in San Antonio, TX using yelp data

*3,200 restaurants in San Antonio*
#### Prerequisites:

#### Getting started:
1. Acquire Data
    - The health inspector scores are publically available at https://www.sanantonio.gov/Health/News/RestaurantReports#229312766-2017, we       downloaded the excel files and combined the health inspection reports from 2017 to 1019.
    - To get more details not avialble in the excel files about the health inspection reports (inspector, number of violations, and addresses   of the restaurants), we had scrape that information from the website. Using **selenium**, **phantomjs drivers**, we created a             webscraper to go through a pandas dataframe to get our desired information
    - Using the available API from the Yelp website to get the information we needed to predict our target variable: Health inspector code.     Yelp would only allow use to acquire 1,000 per inquiry, but by doing seperate inquires by type of reastaurant. By pulling each type of    restaurant we are able to get the information needed (about 3,000 of the establishments in San Antonio)
    - ##### The amount of health establishments vs the aquisistion of yelp is uneven due to the fact that health inspections apply to any       place that will sell foor including such estbaliushments that may just have a vending machine. We will be discarding these                establiushments for this model 
    - 