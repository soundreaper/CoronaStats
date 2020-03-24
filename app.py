import os
from flask import Flask, render_template, url_for, send_from_directory, send_file, request
import pandas as pd
from do_plot import do_plot
from base64 import b64encode

df_confirmed = pd.read_csv('time_series_covid19_confirmed_global.csv')
drop_coord_df = df_confirmed.drop(['Province/State', 'Lat', 'Long'], axis=1)
set_index_to_country = drop_coord_df.set_index('Country/Region')
new_df = set_index_to_country.transpose()

df_deaths = pd.read_csv('time_series_covid19_deaths_global.csv')
drop_coord_df_deaths = df_deaths.drop(['Province/State', 'Lat', 'Long'], axis=1)
set_index_to_country_deaths = drop_coord_df_deaths.set_index('Country/Region')
new_df_deaths = set_index_to_country_deaths.transpose()

def get_country_list():
    df_confirmed = pd.read_csv('time_series_covid19_confirmed_global.csv')
    country_list = df_confirmed['Country/Region'].tolist()
    country_list.insert(0," ")
    return country_list

def get_confirmed_sum():
    confirmed_sum = new_df.iloc[-1].sum()
    return confirmed_sum

def get_confirmed_num(country):
    confirmed_num = new_df.iloc[-1][country]
    return confirmed_num

def get_deaths_num(country):
    deaths_num = new_df_deaths.iloc[-1][country]
    return deaths_num

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/mypage.jpg', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    """Index page of the application"""
    confirmed_sum = get_confirmed_sum()
    return render_template('index.html', confirmed_sum=confirmed_sum)

@app.route('/confirmed', methods=['GET','POST'])
def confirmed():
    """Confirmed page of the application"""
    country_list = get_country_list()
    bytes_obj = None
    confirmed_num = 0
    if request.method == "POST":
        country = request.form.get("countries", None)
        confirmed_num = get_confirmed_num(country)
        bytes_obj = do_plot(country, "confirmed")
        image = b64encode(bytes_obj.getbuffer()).decode("utf-8")
        return render_template('confirmed.html', country_list=country_list, graph=image, confirmed_num=confirmed_num, country=country)
    return render_template('confirmed.html', country_list=country_list)

@app.route('/deaths', methods=['GET','POST'])
def deaths():
    """Deaths page of the application"""
    country_list = get_country_list()
    bytes_obj = None
    deaths_num = 0
    if request.method == "POST":
        country = request.form.get("countries", None)
        deaths_num = get_deaths_num(country)
        bytes_obj = do_plot(country, "deaths")
        image = b64encode(bytes_obj.getbuffer()).decode("utf-8")
        return render_template('deaths.html', country_list=country_list, graph=image, deaths_num=deaths_num, country=country)
    return render_template('deaths.html', country_list=country_list)

@app.route('/login')
def login():
    """Page for logging in"""
    return render_template('login.html')

@app.route('/register')
def register():
    """Page for registering"""
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)