from bs4 import BeautifulSoup # need beautifulsoup for scraping
import requests, json, csv # need these to access data on the internet and deal with structured data in my cache
from advanced_expiry_caching import Cache # use tool from the other file for caching

FILENAME = "allinfo_parks.json" # saved in variable with convention of all-caps constant

program_cache = Cache(FILENAME) # create a cache -- stored in a file of this name

url = "https://www.nps.gov/findapark/advanced-search.htm?p=1&v=0" #url can act as identifier for caching in a scraping situation -- it IS frequently unique here, unlike in query requests

data = program_cache.get(url)
if not data:
    data = requests.get(url).text
    program_cache.set(url, data, expire_in_days=1)


soup = BeautifulSoup(data, "html.parser") # html.parser string argument tells BeautifulSoup that it should work in the nice html way
states = soup.find_all(id="form-park")
# print(states)
activities = soup.find_all(id="form-activity")
# print(activities)
topics = soup.find_all(id="form-topic")
# print(topics)

states_name=[]
for state in states:
    b=state.find_all('option')
    for i in range(len(b)):
#        print(b[i]['value'])
#        print(b[i].text)
        c=b[i]['value'],b[i].text
        states_name.append(c)
# print(states_name)
# [(,),(,)...] like this. value + name

activities_name=[]
for activity in activities:
    b=activity.find_all('option')
    for i in range(len(b)):
        c=b[i]['value'],b[i].text
        activities_name.append(c)
# print(activities_name)

topics_name=[]
for topic in topics:
    b=topic.find_all('option')
    for i in range(len(b)):
        c=b[i]['value'],b[i].text
        topics_name.append(c)
# print(topics_name)




# whether write csv? depends on the process.
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



# print(states_name[1][0])
# class IdenticalForm(Form):
#     state = TextField('State:', validators=[validators.required()])
#     activity = TextField('Activity:', validators=[validators.required()])
#     topic = TextField('Topic:', validators=[validators.required()])
#     # remember_me = BooleanField('Remember Me')
#     # submit = SubmitField('Sign In')
#
# @app.route("/identical", methods=['GET', 'POST'])#http://127.0.0.1:5000/identical
# def identical():
#     form = IdenticalForm(request.form)
#     print form.errors
#
#     if request.method == 'POST':
#         state=request.form['state']
#         activity=request.form['activit']
#         topic=request.form['topic']
#         print state, " ", activity, " ", topic
#
#     url = "https://www.nps.gov/findapark/advanced-search.htm?s=%s&a=%s&t=%s&p=1&v=0" % (state,activity,topic)
#     FILENAME = "%s_%s_%s_data.json" % (state,activity,topic)# saved in variable with convention of all-caps constant
#     program_cache = Cache(FILENAME) # create a cache -- stored in a file of this name
#     data = program_cache.get(url)
#
#     if not data:
#         data = requests.get(url).text # get the text attribute from the Response that requests.get returns -- and save it in a variable. This should be a bunch of html and stuff
#         program_cache.set(url, data, expire_in_days=1) # just 1 day here because news site / for an example in class
#
#
#     if form.validate():
#         flash('Please check your identical selection ' + state + activity +topic)
#         return render_template('hello.html', form=form)
#     else:
#         flash('Error: All the form fields are required. ')
#
#     # if form.validate_on_password():
#         # return redirect('/index')



#
# url = "https://www.nps.gov/findapark/advanced-search.htm?s=AK&a=3&t=4&p=1&v=0"
# FILENAME = "AK_3_4_data.json"# saved in variable with convention of all-caps constant
# program_cache = Cache(FILENAME) # create a cache -- stored in a file of this name
# data = program_cache.get(url)
#
# if not data:
#     data = requests.get(url).text # get the text attribute from the Response that requests.get returns -- and save it in a variable. This should be a bunch of html and stuff
#     program_cache.set(url, data, expire_in_days=1) # just 1 day here because news site / for an example in class
#
#
# soup = BeautifulSoup(data, "html.parser") # html.parser string argument tells BeautifulSoup that it should work in the nice html way
#
# results = soup.select("h3[class='ListingGridItem-title carrot-end']")
# # for j in range(len(results)):
# #     a=results[j].find('h3')
# #     t=[]
#     # t.append(a.get_text())
# print(results)













############???!!!
#
# for i in range(len(states_name)):
#     url = "https://www.nps.gov/findapark/advanced-search.htm?s=%s&a=%s&t=%s&p=1&v=0" % (states_name[i][0],activities_name[i][0],topics_name[i][0])
#     # url = "https://www.nps.gov/state/%s/index.htm" % states_name[i]
#     FILENAME = "%s_%s_%s_data.json" % (states_name[i][0],activities_name[i][0],topics_name[i][0])# saved in variable with convention of all-caps constant
#     program_cache = Cache(FILENAME) # create a cache -- stored in a file of this name
#     data = program_cache.get(url)
#
#     if not data:
#         data = requests.get(url).text # get the text attribute from the Response that requests.get returns -- and save it in a variable. This should be a bunch of html and stuff
#         program_cache.set(url, data, expire_in_days=1) # just 1 day here because news site / for an example in class
