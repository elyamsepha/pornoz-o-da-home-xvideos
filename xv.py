import requests
from lxml import html
from bs4 import BeautifulSoup
import re

header = {
	'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75"
}

URL = "https://www.xvideos.com/"

response = requests.get(URL, headers=header)
print("codigo de requesição: ", response.status_code)

content = response.content
site = BeautifulSoup(content, 'html.parser')
arq = open('xvideos.txt', 'w')
for titulo in site.find_all('p', attrs={'class': "title"}):
        for titu in titulo:
                arq.write("titulo: "+titu.get('title')+"\nlink: "+"https://www.xvideos.com"+titu.get('href')+"\n\n")
arq.close()
