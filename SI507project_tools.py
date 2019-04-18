from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, session, redirect, url_for, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, BooleanField
import pandas as pd
import csv,json
from advanced_expiry_caching import Cache # use tool from the other file for caching
import requests,os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security let us play with national parks'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./parks_collection.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy


class State(db.Model):
    __tablename__="States"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    value = db.Column(db.String(64))
    # park_id = db.Column(db.Integer, db.ForeignKey("National_Park.id")) #ok to be null for now


    def __repr__(self):
        return "State id: {}\nState name: {}\nState value: {}".format(self.id,self.name,self.value)

class Topic(db.Model):
    __tablename__="Topics"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    value = db.Column(db.Integer)

    def __repr__(self):
        return "Topic id: {}\nTopic name: {}\nTopic value: {}".format(self.id,self.name,self.value)

class Activity(db.Model):
    __tablename__="Activities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    value = db.Column(db.Integer)

    def __repr__(self):
        return "Activity id: {}\nActivity name: {}\nActivity value: {}".format(self.id,self.name,self.value)

class Type(db.Model):
    __tablename__="Types"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    # park_id = db.Column(db.Integer, db.ForeignKey("National_Park.id"))


    def __repr__(self):
        return "Type id: {}\nType name:{}".format(self.id,self.name)

class National_Park(db.Model):
    __tablename__="National_Park"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    description = db.Column(db.String(64))
    # states = db.relationship("States",backref="National_Park")#park-state: one to many
    # type = db.relationship("Type", backref=db.backref("National_Park", uselist=False))# park-type: one to one



    def __repr__(self):
        return "{}:\nLocation: {}\n{}".format(self.name,self.location,self.description)


db.create_all()

#######write topics
def get_or_create_topic(topicname,topicvalue):
    t = Topic.query.filter_by(name = topicname, value = topicvalue).first()
    if t:
        return t
    else:
        t = Topic(name = topicname, value = topicvalue)
        session.add(t)
        session.commit()
        return t

topics_info = pd.read_csv('topics_info.csv')
for i in range(len(topics_info)):
    get_or_create_topic(topics_info['name'][i],topics_info['value'][i])



#######write activities
def get_or_create_activities(activitiesname,activitiesvalue):
    t = Activity.query.filter_by(name = activitiesname, value=activitiesvalue).first()
    if t:
        return t
    else:
        t = Activity(name = activitiesname, value=activitiesvalue)
        session.add(t)
        session.commit()
        return t

activities_info = pd.read_csv('activities_info.csv')
for i in range(len(activities_info)):
    get_or_create_activities(activities_info['name'][i],activities_info['value'][i])



#####write states
def get_or_create_states(statesname,statesvalue):
    t = State.query.filter_by(name = statesname, value=statesvalue).first()
    if t:
        return t
    else:
        t = State(name = statesname, value=statesvalue)
        session.add(t)
        session.commit()
        return t

states_info = pd.read_csv('states_info.csv')
for i in range(len(states_info)):
    get_or_create_states(states_info['name'][i],states_info['value'][i])




#
# class Historical_Park(National_Park):
#     def fname(arg):
#         pass
#
#
# class National_Monument(National_Park):
#     def fname(arg):
#         pass
#
#
# class National_Military_Park(National_Park):
#     def fname(arg):
#         pass
#
#
# class National_Preserve(National_Park):
#     def fname(arg):
#         pass
#
#
# class National_Heritage_Area(National_Park):
#     def fname(arg):
#         pass


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
    # remember_me = BooleanField('Remember Me')
    # submit = SubmitField('Sign In')

@app.route("/", methods=['GET', 'POST'])#http://127.0.0.1:5000/
def home_page():
    form = ReusableForm(request.form)
    print form.errors

    if request.method == 'POST':
        name=request.form['name']
        password=request.form['password']
        email=request.form['email']
        print name, " ", email, " ", password

    if form.validate():
        flash('Thanks for registration ' + name)
        return redirect('/index')
    else:
        flash('Error: All the form fields are required. ')

    # if form.validate_on_password():
        # return redirect('/index')

    return render_template('hello.html', form=form)


@app.route("/parks")#http://127.0.0.1:5000/index
def parks():
    return render_template('index.html')

#
#
# @app.route("/parks")#http://127.0.0.1:5000/parks
# def parks():
#     return render_template('parks.html')





chromedriver =  "/Users/caizuyi/Downloads/SI\ 507/final_project/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver


@app.route('/query-example')#http://127.0.0.1:5000/query-example?state=AK&activity=3&topic=4
def query_example():
    state = request.args.get('state') #if key doesn't exist, returns None
    activity = request.args['activity'] #if key doesn't exist, returns a 400, bad request error
    topic = request.args.get('topic')
    driver = webdriver.Chrome(chromedriver)

    identical_url= "https://www.nps.gov/findapark/advanced-search.htm?s=%s&a=%s&t=%s&p=1&v=0" % (state,activity,topic)
    driver.get(identical_url)
    time.sleep(10)

    data = driver.page_source
    # print(data)

    soup = BeautifulSoup(data, "html.parser") # html.parser string argument tells BeautifulSoup that it should work in the nice html way

    results_text = soup.find_all(id="ListingHeaderResults")
    # print(results_text[0].text)##the results sentence

    results = soup.find_all(id="ListingResultsGrid")
    for r in results:
        img=r.find_all('a')
        name=r.find_all('h3')
        type=r.find_all('span')
        state=r.find_all('p')
        # print(img[0])#how to deal with image info?---image
        # print(name[0].text)#---park.name
        # print(type[0].text)#---park.type
        # print(state[0].text)#---park.state
        name=name[0].text
        type=type[0].text


    return '''The {},{},{}'''.format(state,activity,topic)










if __name__ == '__main__':
    app.run()
