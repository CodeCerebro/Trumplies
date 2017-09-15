import requests
from bs4 import BeautifulSoup
import pandas as pd

source = requests.get("https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html")
soup = BeautifulSoup(source.text, "html.parser")

#all recordings begin with "span" and attribute "class =" so we use fall_all method to find it
results = soup.find_all("span", attrs={'class':'short-desc'})

#extracting the data
records = []
for result in results:
    date = result.find('strong').text[0:-1] + ', 2017'  #extracting the text from "strong" tag object
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date, lie, explanation, url))

#coverting a list of tuple
df = pd.DataFrame(records, columns = ['date', 'lie', 'explanation', 'url'])
df['date'] = pd.to_datetime(df['date'])

#exporting the data to a CSV file
df.to_csv('trump_lies.csv', index=False, encoding='utf-8')