import requests
from bs4 import BeautifulSoup

URL = 'https://www.wcoanimesub.tv/anime/black-clover-tv-english-subbed'
#headers can be found by typing 'What is my user agent' into your browser and copying the result
headers = {"User-Agent": 'enter your headers here!'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

epasodes = soup.find(id = "sidebar_right3").get_text()
#print(epasodes)

epasodes_list = list(epasodes.split())
#print(epasodes_list)