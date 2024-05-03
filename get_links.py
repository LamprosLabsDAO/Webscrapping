import csv
from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys

args = sys.argv

input_file = "input_datas/"  + args[1]

if(len(args)<=1):
    print("no arguments provided")
response = requests.get("https://developers.tron.network/docs/getting-start")
# Assuming 'html_content' is the HTML content of the webpage
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all headings (h1, h2, h3, etc.)
articles = soup.find(class_="Sidebar1t2G1ZJq-vU1 rm-Sidebar hub-sidebar-content")
# print(articles)
links = articles.find_all('a')

all_hrefs=[]

for link in links :
         
    print(link.get('href'))
    
    str ="https://developers.tron.network" + link.get('href')
    all_hrefs.append(str)

all_hrefs=pd.DataFrame(all_hrefs)
all_hrefs.to_csv(input_file,index=False,header=False)
print(f"Data has been successfully.")
