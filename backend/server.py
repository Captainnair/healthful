# FLASK
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS, cross_origin
# WEB SCRAPING
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import random
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired


class FieldsRequiredForm(FlaskForm):
    """Require all fields to have content. This works around the bug that WTForms radio
    fields don't honor the `DataRequired` or `InputRequired` validators.
    """

    class Meta:
        def render_field(self, field, render_kw):
            render_kw.setdefault('required', True)
            return super().render_field(field, render_kw)


class Restrictions(FieldsRequiredForm):
    q1 = RadioField('Do you have any dietary restrictions', choices=[("vegan", "vegan"), ("vegetarian", "vegetarian"),("None", "None")])
    submit = SubmitField('Check you Answers')



# FLASK SERVER
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# WEB SCRAPING GLOBAL VARIABLES
PATH = "./chromedriver"
veg_fruit = ['cucumber', 'carrot', 'capsicum', 'onion', 'potato', 'tomato', 'beetroot', 'cabbage', 'lettuce', 'spinach', 'cauliflower', 'turnip', 'corn', 'sweetcorn', 'sweet_potato', 'paprika', 'ginger', 'garlic', 'pea', 'banana', 'apple', 'pear', 'grapes', 'orange', 'kiwi', 'watermelon', 'pomegranate', 'pineapple', 'mango']


@app.route('/')
@app.route('/poll', methods=['POST','GET'])
def poll():
    global form
    form = Restrictions()
    if form.validate_on_submit():
        return redirect(url_for('results'))
    return render_template('poll.html', form=form)



@app.route('/results', methods=['POST','GET'])
def results():
    global answer
    answer =request.form['q1']
    return render_template('results.html', answer=answer)


@app.route('/form', methods=['POST'])
def form():
    message = request.get_json(force=True)
    flag = True
    while flag:
        if message['name'] in veg_fruit:
            bbc_url = 'https://www.bbc.co.uk/food/' + message['name']
            flag = False
        else:
            response = {
                'error': 'Please enter a food in our database'
            }
            return jsonify(response)

    driver = webdriver.Chrome(PATH)
    req = requests.get(bbc_url).text
    soup = BeautifulSoup(req, 'lxml')

    url_list = []
    food = soup.find_all('a', class_="promo")
    for urls in food:
        if '/food/recipes/' in urls['href']:
            url_list.append('https://www.bbc.co.uk' + urls['href'])

    final_url = url_list[random.randint(0, len(url_list))]
    driver.get(final_url)

    div = driver.find_element_by_class_name('recipe-ingredients-wrapper')
    ingredients = div.text
    div2 = driver.find_element_by_class_name('recipe-method-wrapper')
    method = div2.text

    response = {
        'urls': url_list,
        'ingredients': ingredients,
        'method': method
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run()
