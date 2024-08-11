from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://br.investing.com/currencies/exchange-rates-table'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

find_text = soup.find('td', class_='pid-2103-last').text.strip()

print(find_text)

table = soup.find('table')

world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]

df = pd.DataFrame(columns=world_table_titles)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    lenght = len(df)
    df.loc[lenght] = individual_row_data

print(df)

df.to_csv(r'E:\8. Programming\beautifulsoup_web_scraping\output.csv', index=True)