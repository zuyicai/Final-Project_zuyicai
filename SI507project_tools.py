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
from sqlalchemy.orm import relationship
import time

##########scraping data from the website: states, topics, activities
FILENAME = "allinfo_parks.json" # saved in variable with convention of all-caps constant
program_cache = Cache(FILENAME) # create a cache -- stored in a file of this name

url = "https://www.nps.gov/findapark/advanced-search.htm?p=1&v=0" #url can act as identifier for caching in a scraping situation -- it IS frequently unique here, unlike in query requests

data = program_cache.get(url)
if not data:
    data = requests.get(url).text
    program_cache.set(url, data, expire_in_days=1)


soup = BeautifulSoup(data, "html.parser") # html.parser string argument tells BeautifulSoup that it should work in the nice html way
states = soup.find_all(id="form-park")
activities = soup.find_all(id="form-activity")
topics = soup.find_all(id="form-topic")

states_name=[]
for state in states:
    b=state.find_all('option')
    for i in range(len(b)):
        c=b[i]['value'],b[i].text
        states_name.append(c)


activities_name=[]
for activity in activities:
    b=activity.find_all('option')
    for i in range(len(b)):
        c=b[i]['value'],b[i].text
        activities_name.append(c)

topics_name=[]
for topic in topics:
    b=topic.find_all('option')
    for i in range(len(b)):
        c=b[i]['value'],b[i].text
        topics_name.append(c)


with open('states_info.csv','w') as f:
    writecsv = csv.writer(f)
    writecsv.writerow(['value','name'])
    for i in range(len(states_name)-1):
        writecsv.writerow([states_name[i+1][0],states_name[i+1][1]])

with open('activities_info.csv','w') as f:
    writecsv = csv.writer(f)
    writecsv.writerow(['value','name'])
    for i in range(len(activities_name)):
        writecsv.writerow([activities_name[i][0],activities_name[i][1]])

with open('topics_info.csv','w') as f:
    writecsv = csv.writer(f)
    writecsv.writerow(['value','name'])
    for i in range(len(topics_name)):
        writecsv.writerow([topics_name[i][0],topics_name[i][1]])


###########################
###########################


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
    # park = relationship("National_Park", backref="states")# many to many


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
    park = relationship("National_Park", backref="typeee")# one to many


    def __repr__(self):
        return "Type id: {}\nType name:{}".format(self.id,self.name)

class National_Park(db.Model):
    __tablename__="National_Park"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    type = db.Column(db.String())
    location = db.Column(db.String())
    description = db.Column(db.String())
    value = db.Column(db.String())
    type_id = db.Column(db.Integer, db.ForeignKey("Types.id"))#type-parks:one to many
    # state_id = db.Column(db.Integer, db.ForeignKey("States.id"))#park-states: many to many

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

######write types from parks.csv
def get_and_write_types(tname):
    t = Type.query.filter_by(name = tname).first()
    if t:
        return t
    else:
        t = Type(name = tname)
        session.add(t)
        session.commit()
        return t

types_info = pd.read_csv('parks.csv')
types_info.drop_duplicates(subset='Type',inplace=True)
types_info=types_info.reset_index()

for i in range(len(types_info)):
    get_and_write_types(types_info['Type'][i])


####write data from parks.csv
def get_and_write_parks(pname,ptype,plocation,pdescription,pvalue):
    p = National_Park.query.filter_by(name = pname.decode('utf-8'), type = ptype.decode('utf-8'), location = plocation.decode('utf-8'), description=pdescription.decode('utf-8'),value = pvalue.decode('utf-8')).first()
    if p:
        return p
    else:
        ty = get_and_write_types(ptype)
        p = National_Park(name = pname.decode('utf-8'), type = ptype.decode('utf-8'), location = plocation.decode('utf-8'), description=pdescription.decode('utf-8'),value = pvalue.decode('utf-8'),type_id = ty.id)
        session.add(p)
        session.commit()
        return p


parks_info = pd.read_csv('parks.csv')
parks_info.drop_duplicates(subset='Name',inplace=True)
parks_info=parks_info.reset_index()
for i in range(len(parks_info)):
    get_and_write_parks(parks_info['Name'][i],parks_info['Type'][i],parks_info['Location'][i],parks_info['Description'][i],parks_info['Value'][i])










############Flask Routes
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
        return redirect('/all_info')
    else:
        flash('Error: All the form fields are required. ')


    return render_template('index.html', form=form)


@app.route("/all_info")#http://127.0.0.1:5000/all_info
def all_info():
    parks = National_Park.query.all()
    topics = Topic.query.all()
    activitis = Activity.query.all()
    states = State.query.all()
    return render_template('all_info.html',parks=parks,topics = topics,activitis=activitis,states=states)


@app.route("/parks")#http://127.0.0.1:5000/parks
def parks():
    parks = National_Park.query.all()
    return render_template('parks.html', parks = parks)


@app.route("/plan")#http://127.0.0.1:5000/plan
def design():
    return render_template('plan.html')





@app.route('/query-example')#http://127.0.0.1:5000/query-example?state=AK&activity=3&topic=4
def query_example():
    chromedriver =  "/Users/caizuyi/Downloads/chromedriver"# please change the path to where you install chromedriver in
    os.environ["webdriver.chrome.driver"] = chromedriver
    state = request.args.get('state') #if key doesn't exist, returns None
    activity = request.args.get('activity') #request.args['activity']:if key doesn't exist, returns a 400, bad request error
    topic = request.args.get('topic')
    driver = webdriver.Chrome(chromedriver)

    identical_url= "https://www.nps.gov/findapark/advanced-search.htm?s=%s&a=%s&t=%s&p=1&v=0" % (state,activity,topic)
    driver.get(identical_url)
    time.sleep(10)

    data = driver.page_source
    # print(data)

    soup = BeautifulSoup(data, "html.parser") # html.parser string argument tells BeautifulSoup that it should work in the nice html way

    results_text = soup.find_all(id="ListingHeaderResults")
    if results_text[0].text == "Showing 0 - 0 of 0 results":
        return "There is no eligible park of your selection, please change your selection of values and try again :)"
        # print(results_text[0].text)##the results sentence
    else:
        results = soup.find_all(id="ListingResultsGrid")
        n = []
        t = []
        s = []
        for r in results:
            sname=r.find_all('h3')# name list
            for i in sname:
                n.append(i.text)
            stype=r.find_all('span')
            for i in stype:
                t.append(i.text)
            sstate=r.find_all('p')
            for i in sstate:
                s.append(i.text)
        # with open('user_selection.csv','w') as f:
        #     writecsv = csv.writer(f)
        #     writecsv.writerow(['name','type','state'])
        #     for i in range(len(n)):
        #         writecsv.writerow([n[i].decode('utf-8'),t[i].decode('utf-8'),s[i].decode('utf-8')])

        return render_template('query_example.html',result = results_text[0].text, name = n,a=activity,t=topic,s=state)






if __name__ == '__main__':
    app.run()
