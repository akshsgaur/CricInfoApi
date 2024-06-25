from bs4 import BeautifulSoup
import requests
html_text = requests.get("https://sports.ndtv.com/cricket/live-scores").text
soup = BeautifulSoup(html_text, "html.parser")
sect = soup.findAll('div', class_='sp-scr_wrp')
section = sect[0]
description = section.find('span', class_='description').text
location = section.find('span', class_='location').text
current = section.find('div', class_='scr_dt-red').text
link = "https://sports.ndtv.com/" + \
       section.find('a', class_='scr_ful-sbr-txt').get('href')