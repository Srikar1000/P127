from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By 
import pandas as pd
import time

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars'

scraped_data = []
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)


def scrape():
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    bright_star_table = soup.find("table", attrs={'class','wikitable'})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')
        temp_data = []
        for col_data in table_cols:
            data = col_data.text.strip()
            temp_data.append(data)
    scraped_data.append(temp_data)



scrape()
print(scraped_data)

star_data = []

for i in range(0,len(scraped_data)):
    Star_names = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][0]
    required_data = [Star_names,Distance,Mass]
    star_data.append(required_data)


headers = ['Name','Distance','Mass']

star_df = pd.DataFrame(star_data, columns=headers)

star_df.to_csv('scraped_data.csv',index= True, index_label='id')

