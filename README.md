# Final-Project_zuyicai

Zuyi Cai

[Link to this repository](https://github.com/zuyicai/Final-Project_zuyicai)

---
## At This Moment(For Check in Assignment)
1. I have SI507project_tools.py including all classes(National_Park, State, Topic, Activity and Type) I will use for my project.
I have caching.py to scrape the data I will use for my project. In which it will create allinfo_parks.json and states_info.csv, topics_info.csv, activities_info.csv. And these three csvs I will use in SI507project_tools.py to write in the database.
I have parks.csv, which is copyed from project4, I will directly use this data in one of my route of flask.
In SI507project_tools.py, I created all classes and write the data into the database by three functions(get_or_create_topic, get_or_create_activities, get_or_create_states). I used a new module called selenium to create a fake chrome to scrap data from a website needed higher permission. And I used another new module called wtforms to create the form view in my flask application. 

At this point, I have access to ALL of the data I need for my project.(one is got from caching.py and another one is parks.csv from project 4)

2. I have a code file SI507project_tests.py which includes a test suite with reasonable tests for the code in SI507project_tools.py. Although it couldn't pass at this moment, I am trying to test the data input of the database.

3. I created milestones and issues at the beginning of my project and now some of them are completed.

4. This is a draft of my README.md file, using the README template. It's not complete at this time but I already did the completed parts and leave the remaining to be finished. Next, I need to write html file to design the view of flask url, such as the table and the form. And the second route(\parks) still need to write data information into the output.

5. Here I show the database schema diagram showing the tables I had in my database. Here I plan to use many to many relationship, but I haven't done it(Already satisfy 6 requirements, I decide to do it if I have time)
* [Link to this diagram](https://github.com/zuyicai/Final-Project_zuyicai/blob/master/db_final.png)
* ![Alt text](https://github.com/zuyicai/image/blob/master/db_final.png)

## Project Description

My Project is designed for people who want to search detailed information of National Parks in the US and who want to get a straightforward instruction of all parks. In my Flask application, users are able to get identical park travel plan determined by their own interests.



## How to run

* Anaconda installed
* Open your terminal window! `cd` to the place where you want this project to go.
* This repository cloned to somewhere in your computer (the place).
```
git clone <git url>
```
* `cd` into where the project lives
* Create a virtual environment for it
```
virtualenv env
```
* Activate the virtual environment
```
$ source <projectname>-env/bin/activate    # For Mac/Linux...
$ source <projectname>-env/Scripts/activate    # For Windows
(finalproject-env) $     # you've succeeded if you see this after!
```
* install all requirement
```
pip install -r requirements.txt
```
```
Deactivate
```
* Just run the program!
```
python SI507project_tools.py
```
* Check out what’s happening in your terminal window!

## How to use

1. A useful instruction goes here
2. A useful second step here

## Routes in this application
- `/` -> The home page of the Flask application
This page is a form that users need to input their name, email and password to register. After they submit the information and click the button they will directly go to the '/parks' page.

- `/parks` -> The detailed information of all parks
This page will be showed in a form or a table. (it still need to be assigned)

- `/query-example` -> The detail of a user's selection
http://127.0.0.1:5000/query-example?state=AK&activity=3&topic=4
In this url, users need to input the state value, activity value and topic value to specify their selection. And I will show them the original website including the parks satisfied their inputs and the clear information in my application window.


## How to run tests
1. First... (e.g. access a certain directory if necessary)
2. Second (e.g. any other setup necessary)
3. etc (e.g. run the specific test file)
NOTE: Need not have 3 steps, but should have as many as are appropriate!

## In this repository:
- Templates
  - index.html
  - hello.html
- SI507project_tools.py
- SI507project_tests.py
- caching.py
- parks.csv
- advanced_expiry_caching.py
- chromedriver

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [ ] This is a completed requirement.
- [x] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it.
- [ ] Includes a `requirements.txt` file containing all required modules to run program
- [ ] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [ ] Includes at least 3 different routes
- [ ] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [ ] Interactions with a database that has at least 2 tables
- [ ] At least 1 relationship between 2 tables in database
- [ ] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [x] Use of a new module
- [x] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [x] At least one form in your Flask application
- [x] Templating in your Flask application
- [x] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [x] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [x] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [x] Caching of data you continually retrieve from the internet in some way

### Submission
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [x] I included a summary of my project and how I thought it went **in my Canvas submission**!
