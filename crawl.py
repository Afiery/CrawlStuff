import requests
from bs4 import BeautifulSoup

url='https://www.imdb.com/chart/top/?ref_=nv_mv_250'

r = requests.get(url)
request = r.content

soup = BeautifulSoup(request, 'html.parser')

title = soup.findAll('td',attrs={'class':'titleColumn'})

count = 0
for x in range(0,len(title)):
    count = +1
    print("{0}.  {1}".format(count, title[x].text.strip()))