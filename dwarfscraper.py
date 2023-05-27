from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy
import requests

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

brown_dwarf_data = []

def scrape_dwarfs(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, features="html.parser")
        table = soup.find_all("table", attrs={'class': "wikitable"})[2]
        rows = table.find_all("tr")
        for row in rows:
            temp = []
            cols = row.find_all("td")
            for col in cols:
                try:
                    data = col.text.strip()
                    temp.append(data)
                except:
                    temp.append('')
            brown_dwarf_data.append(temp)
    except:
        time.sleep(1)
        scrape_dwarfs(url)

scrape_dwarfs(url)

headers = ['Brown Dwarf', 'Constellation', "Right Ascension", "Declination", "Apparent Magnitude", "Distance", "Spectral Type", "Mass", "Radius", "Date Discovered"]
dwarfdf = pd.DataFrame(brown_dwarf_data,columns=headers)
dwarfdf.to_csv('dwarf_data.csv', index=True, index_label="id")