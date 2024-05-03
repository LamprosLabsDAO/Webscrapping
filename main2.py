import csv
from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys

def is_valid_url(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

args = sys.argv

if(len(args)<=1):
    print("no arguments provided")
    exit()


input_file = "input_datas/"  + args[1]
output_file = "output_datas/"  + args[2]

url_list=pd.read_csv(input_file,header=None)
print(len(url_list))

heading_texts = {}
for index, row in url_list.iterrows():
    url = row[0] 
    
    if is_valid_url(url):
        response = requests.get(url)
    else : 
        continue
    # Assuming 'html_content' is the HTML content of the webpage
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all headings (h1, h2, h3, etc.)
    article = soup.find(class_="rm-Article")
    headings = article.find_all(['h1', 'h2', 'h3'])

    # Initialize an empty dictionary to store heading names and their corresponding text

    # print("entering inner for loop")
    # Iterate over the headings
    for i in range(len(headings) - 1):  # Exclude the last heading as there's no heading after it
        # Find all elements between two consecutive headings
        elements_between_headings = headings[i].find_all_next(['h1','h2','h3','p', 'ul', 'ol'])  # Find all siblings after the current heading
        links_between_headings = headings[i].find_all_next(['h1','h2','h3','a'])  # Find all siblings after the current heading
        code_between_headings = headings[i].find_all_next(['h1','h2','h3','code'])  # Find all siblings after the current heading
        next_heading_index = headings.index(headings[i + 1])  # Index of the next heading

        # Initialize an empty list to store text under the current heading
        text_under_heading = []
        link_under_heading = []
        code_under_heading = []
        
        # Iterate over the elements between two headings
        # print("entering most inner for loop")
        for links in links_between_headings:
            # If the element is a heading, break the loop
            if links in headings[next_heading_index:]:
                break
            # Append the text of the element to the list
            link_under_heading.append(links.get('href'))
            
        for element in elements_between_headings:
            # If the element is a heading, break the loop
            if element in headings[next_heading_index:]:
                break
            # Append the text of the element to the list
            text_under_heading.append(element.get_text(strip=True))
            
        for code in code_between_headings:
            # If the element is a heading, break the loop
            if code in headings[next_heading_index:]:
                break
            # Append the text of the element to the list
            code_under_heading.append(code.get_text(strip=True))
        
        # Join the text under the current heading into a single string
        text_under_heading = ' '.join(text_under_heading)
        text_under_heading = text_under_heading.replace("\n", "")
        # link_under_heading = ','.join(link_under_heading)
        # code_under_heading = ' '.join(code_under_heading)
        
        heading_texts[headings[i].get_text(strip=True)] = {
                'url' : url,
                'text': text_under_heading,
                'code': code_under_heading,
                'link': link_under_heading
            }
    # Write the dictionary to a CSV file

    print(url)
    
with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # Write the header row
    
    writer.writerow(['url','Heading', 'Text', 'Link', 'Code'])
    # Write each heading and its corresponding text, link, and code as a row in the CSV file
    for heading, content in heading_texts.items():
        writer.writerow([content['url'],heading, content['text'], content['link'], content['code']])

print("csv created")
   

