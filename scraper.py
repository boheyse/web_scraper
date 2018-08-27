#Simple Script to calculate the gas savings of a Tesla using average gas prices
#in big cities around the country
import bs4 as bs
import requests
import pandas as pd
import numpy as np
import timeit

start = timeit.default_timer()

#allows access to the url
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

url= 'http://www.gregthatcher.com/Bank/RoutingNumbers/State/AK'

#grabs all html code from url
html_code = requests.get(url, headers=headers)

#stores the code in a beautifulSoup object to allow for parsing
soup = bs.BeautifulSoup(html_code.text, 'html.parser')

#looks for specific html code to find average prices, varies depending on code you want to parse
results = soup.find_all('td')
print(results)
i = 0
r = []
while i in range(len(results)):
    if i % 9 == 0:
        x = str(results[i])
        if len(x) > 25:
            x = str(results[i+1])
            x = x[30:-5]
        else:
            x = x[4:-5]
        r.append(x)
    i+=1

print(r)
df = pd.DataFrame(data={"col1": r})
df.iloc[4:-4]
df.to_csv("./file.csv", sep=',',index=False)

stop = timeit.default_timer()

print(stop - start)
