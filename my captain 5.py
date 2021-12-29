import requests
from bs4 import BeautifulSoup as bs
urls=["https://www.amazon.com/Beautiful-Keychain-Shoulder-Backpack-Supplies/dp/B09KZFC4QJ/ref=sr_1_7?crid=18107QFIL1Y1V&keywords=unicorn+toys+for+girls&qid=1640784849&sprefix=unicorn+%2Caps%2C401&sr=8-7"]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
page=requests.get(urls[0],headers=headers)
soup= bs(page.content,"html.parser")
title=soup.find(id="title_feature_div").get_text()
price=soup.find_all('span',attrs={"class":"a-price-whole"})[0].get_text()
from twilio.rest import Client
client=Client("AC0f88e7893e347cba2518a13f132b9703","3eee0e9ce0f4b9c5ff86fcbf02cbc372")
client.message.create(to_="+919840495107",from_="(217) 919-5679",body="Price reduced"+urls[0])

