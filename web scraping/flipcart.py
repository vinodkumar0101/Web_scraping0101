from selenium import webdriver
#from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

products = []
prices = []
ratings = []
driver.get("https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=a734b8d9-d1fb-4c21-8c50-8c01228d4e18&as-backfill=on")
content = driver.page_source

for i in range(2,24):
    str1='//*[@id="container"]/div/div[3]/div[1]/div[2]/div['
    str2=']/div/div/div/a/div[2]/div[1]/div[1]'
    prc1='//*[@id="container"]/div/div[3]/div[1]/div[2]/div['
    prc2=']/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]'
    rat1 = '//*[@id="container"]/div/div[3]/div[1]/div[2]/div['
    rat2 = ']/div/div/div/a/div[2]/div[1]/div[2]'
    name = driver.find_element(By.XPATH,str1+str(i)+str2)
    price = driver.find_element(By.XPATH,prc1+str(i+1)+prc2)
    rating = driver.find_element(By.XPATH,rat1+str(i)+rat2)
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

for i in range(len(products)):
    print(products[i],prices[i])
'''
#soup = BeautifulSoup(content, features="html.parser")
print(soup)
for a in soup.findAll:
    name=a.find('div',attrs={'class':'_4rR01T'})
    price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    rating=a.find('div',attrs={'class':'_3LWZlK'})
    print(a,rating)
products.append(name.get_text()) if name else ''
prices.append(price.get_text()) if price else ''
ratings.append(rating.get_text()) if ratings else '' '''

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 

df.to_csv('products.csv', index=False, encoding='utf-8')