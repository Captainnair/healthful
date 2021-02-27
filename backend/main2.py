from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import random
import time

# Initiate the path for the chrome driver and create the list.
PATH = "C:\Program Files (x86)\chromedriver.exe"
veg = ['cucumber', 'carrot', 'capsicum', 'onion', 'potato', 'tomato', 'beetroot', 'cabbage', 'lettuce', 'spinach', 'cauliflower', 'turnip', 'corn', 'sweetcorn', 'sweet_potato', 'paprika', 'ginger', 'garlic', 'pea', 'banana', 'apple', 'pear', 'grapes', 'orange', 'kiwi', 'watermelon', 'pomegranate', 'pineapple', 'mango']

choice = input('Choose a vegetable/fruit:').lower()

# allows to repeat asking the question for what fruit/vegetable
flag = True
while flag:
    if choice in veg:
        bbc_url = 'https://www.bbc.co.uk/food/' + choice
        flag = False
    else:
        choice = input('That vegetable/fruit is not recognize, please enter another one:').lower


driver = webdriver.Chrome(PATH)  # opens the browser for selenium
req = requests.get(bbc_url).text # opens the url for scraping
soup = BeautifulSoup(req, 'lxml') # creates the soup for the initial page with all recipes

url_list = []
food = soup.find_all('a', class_="promo")  # gets all the different recipes found on the ingredient's page
for urls in food:
    if '/food/recipes/' in urls['href']:
        url_list.append('https://www.bbc.co.uk' + urls['href'])

# randomizes the recipe that will be picked for that certain ingredient
final_url = url_list[random.randint(0, len(url_list)-1)]
url_list.remove(final_url)
final_url1 = url_list[random.randint(0, len(url_list)-1)]
url_list.remove(final_url1)
final_url2 = url_list[random.randint(0, len(url_list)-1)]
url_list.remove(final_url2)
driver.get(final_url)  # open up the recipe's url for parsing and getting html data


req = requests.get(final_url).text
soup2 = BeautifulSoup(req, 'lxml')
try:
    img = soup2.find("div", {"class": "recipe-media"}).find("img")
    image = img['src']
    print(image + '\n')
except:
    print('There is no image \n')

prep = soup2.find('div', class_="recipe-leading-info")
prep = prep.find_all('div', class_="gel-pica")
print(prep[0].text)
print(prep[1].text)
print(prep[2].text)

title = driver.find_element_by_class_name('gel-trafalgar')
print('Title:' + title.text +'\n')

div = driver.find_element_by_class_name('recipe-ingredients-wrapper') # gets the ingredients for the recipe
print(div.text)
div2 = driver.find_element_by_class_name('recipe-method-wrapper') # gets the method or steps to make the recipe
print('\n')
print(div2.text)
print('------------------------------------------------------------------------------------------\n')


driver.get(final_url1)
req = requests.get(final_url1).text
soup2 = BeautifulSoup(req, 'lxml')
try:
    img = soup2.find("div", {"class": "recipe-media"}).find("img")
    image = img['src']
    print(image + '\n')
except:
    print('There is no image \n')

prep = soup2.find('div', class_="recipe-leading-info")
prep = prep.find_all('div', class_="gel-pica")
print(prep[0].text)
print(prep[1].text)
print(prep[2].text)

title = driver.find_element_by_class_name('gel-trafalgar')
print('Title:' + title.text +'\n')

div = driver.find_element_by_class_name('recipe-ingredients-wrapper') # gets the ingredients for the recipe
print(div.text)
div2 = driver.find_element_by_class_name('recipe-method-wrapper') # gets the method or steps to make the recipe
print('\n')
print(div2.text)
print('------------------------------------------------------------------------------------------\n')

driver.get(final_url2)
req = requests.get(final_url2).text
soup2 = BeautifulSoup(req, 'lxml')
try:
    img = soup2.find("div", {"class": "recipe-media"}).find("img")
    image = img['src']
    print(image + '\n')
except:
    print('There is no image \n')

prep = soup2.find('div', class_="recipe-leading-info")
prep = prep.find_all('div', class_="gel-pica")
print(prep[0].text)
print(prep[1].text)
print(prep[2].text)

title = driver.find_element_by_class_name('gel-trafalgar')
print('Title:' + title.text +'\n')

div = driver.find_element_by_class_name('recipe-ingredients-wrapper') # gets the ingredients for the recipe
print(div.text)
div2 = driver.find_element_by_class_name('recipe-method-wrapper') # gets the method or steps to make the recipe
print('\n')
print(div2.text)

time.sleep(5)
driver.close()
