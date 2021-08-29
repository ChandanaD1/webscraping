# web scraping

from bs4 import BeautifulSoup # virtual environment
import time
import csv
import requests # allows to request acces to info from website

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
get_link = requests.get(START_URL)
time.sleep(10)

headers = ["name", "distance", "mass", "radius"]
planet_data = []

def scrape(): #planet_data contains planet NUMBER data (ex: weight of planet)
    for i in range(0, 100): 
        soup = BeautifulSoup(get_link.text, "html.parser") #creating virtual environment 
        temp_list = []
        for tr_tag in soup.find_all("tr"): #soup finds all "tr" as tr_tags
            td_tags = tr_tag.find_all("td") #tr_tag finds all "td" as td_tags 
            for td_tags in td_tags: #tr is table row, td is table data
                try:
                    temp_list.append(td_tag.find_all("div",attrs={"class":"value"})[0].contents[0]) #appends all td_tags with "value" class (only first address)
                except: #exception for try
                    temp_list.append("")
        planet_data.append(temp_list)
    with open("scrapper_2.csv", "w") as f: #writing info into scraper_2.csv
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

scrape()


