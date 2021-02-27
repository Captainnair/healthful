from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import random

PATH = "./chromedriver"
veg_fruit = ['cucumber', 'carrot', 'capsicum', 'onion', 'potato', 'tomato', 'beetroot', 'cabbage', 'lettuce', 'spinach', 'cauliflower', 'turnip', 'corn', 'sweetcorn', 'sweet_potato', 'paprika', 'ginger', 'garlic', 'pea', 'banana', 'apple', 'pear', 'grapes', 'orange', 'kiwi', 'watermelon', 'pomegranate', 'pineapple', 'mango']

choice = input('Choose a vegetable/fruit:').lower()
# added code
from tkinter import *
root = Tk()
allergy = input('Please select any dietary restrictions:')
a = IntVar()
b = IntVar()
c = IntVar()
def clicked():
    label1 = Label(root, text=a.get())
    label2 = Label(root, text=b.get())
    label1.pack()
    label2.pack()
    label3 = Label(root, text=c.get())
    label3.pack()
Radiobutton(root, text="Vegetarian", variable=a, value=1, command=lambda: clicked(a.get())).pack()
Radiobutton(root, text="Vegan", variable=b, value=2, command=lambda: clicked(b.get())).pack()
Radiobutton(root, text="None", variable=c, value=3,  command=lambda: clicked(c.get())).pack()
label1 = Label(root, text=a.get())
label2 = Label(root, text=b.get())
label3 = Label(root, text=c.get())
label1.pack()
label2.pack()
label3.pack()
if(c.get()):
    flag = True
    while flag:
        if choice in veg_fruit:
            bbc_url = 'https://www.bbc.co.uk/food/' + choice
            flag = False
        else:
            choice = input('That vegetable/fruit is not recognize, please enter another one:').lower



    driver = webdriver.Chrome(PATH)
    req = requests.get(bbc_url).text
    soup = BeautifulSoup(req, 'lxml')

    div = driver.find_element_by_class_name('recipe-ingredients-wrapper')
    print(div.text)

    div2 = driver.find_element_by_class_name('recipe-method-wrapper')
    print('\n')
    print(div2.text)
elif(b.get()):
    flag = True
    while flag:
        if choice in veg_fruit:
            bbc_url = 'https://www.bbc.co.uk/food/search?q=vegan+'+choice
            flag = False
        else:
            choice = input('That vegetable/fruit is not recognize, please enter another one:').lower



    driver = webdriver.Chrome(PATH)
    req = requests.get(bbc_url).text
    soup = BeautifulSoup(req, 'lxml')

    div = driver.find_element_by_class_name('recipe-ingredients-wrapper')
    print(div.text)

    div2 = driver.find_element_by_class_name('recipe-method-wrapper')
    print('\n')
    print(div2.text)
elif(a.get()):
    flag = True
    while flag:
        if choice in veg_fruit:
            bbc_url = 'https://www.bbc.co.uk/food/search?q=Vegetarian+'+choice
            flag = False
        else:
            choice = input('That vegetable/fruit is not recognize, please enter another one:').lower



    driver = webdriver.Chrome(PATH)
    req = requests.get(bbc_url).text
    soup = BeautifulSoup(req, 'lxml')

    div = driver.find_element_by_class_name('recipe-ingredients-wrapper')
    print(div.text)

    div2 = driver.find_element_by_class_name('recipe-method-wrapper')
    print('\n')
    print(div2.text)
