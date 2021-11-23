import pandas as pd
import requests
from bs4 import BeautifulSoup
import html5lib

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"

data = requests.get(url).text

soup = BeautifulSoup(data, 'html5lib')

amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])                 #creating the database


# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row

for row in soup.find("tbody").find_all("tr"):                                                           #tbody is the whole table whereas tr is all the rows
    col = row.find_all("td")                                                                            #td is each cell
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text                                                                                #naming the columns accordingly

    amazon_data = amazon_data.append(
     {"Date": date, "Open": Open, "High": high, "Low": low, "Close": close, "Adj Close": adj_close,
      "Volume": volume}, ignore_index=True)                                                             #adding the data to the table

print(amazon_data.head())

amazon_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in soup.find('tbody').find_all('tr'):
    col = row.find_all('td')
    date = col[0].text
    Revenue = col[1].text

    tesla_data = amazon_data.append(
        {"Date": date, "Revenue": Revenue}, ignore_index=True)

print(amazon_data)
