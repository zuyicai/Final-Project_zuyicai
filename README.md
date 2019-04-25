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

My Project is designed for people who want to search detailed information of National Parks in the US and who want to get a straightforward instruction of all parks. In my Flask application, users are able to get identical park travel plan determined by their own interests, which means they can view the information for specific park and make interaction with the application in order to get the result satisfied their demands.



## How to run

* Anaconda installed
* Open your terminal window! `cd` to the place where you want this project to go.
* This repository cloned to somewhere in your computer (the place).
```
git clone <git url>
```
* `cd` into where the project lives
* Attention!!! Before you run the application, please change the path of "chromedriver" in the code file "SI507project_tools.py" to the place you installed "chromedriver" in.
```
chromedriver =  "/Users/<user_name>/Downloads/<the place>/Final_Project_zuyicai/chromedriver"
```
Just like the following picture:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/5.png)
* Because I need "chromedriver" installed and ran appropriatly to make sure the fifth route in Flask running well! After this step, go ahead!
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
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.18.30%20PM.png)
* And the place where you cloned to will create the following files:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.18.57%20PM.png)
* The file called "states_info.csv" looks like:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.19.21%20PM.png)
* The file called "topics_info.csv" looks like:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.19.33%20PM.png)
* The file called "activities_info.csv" looks like:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.19.43%20PM.png)
* And the created database contains five tables: National_Park, States, Topics, Types and Activities.
* This picture is for Activities:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.20.09%20PM.png)
* This picture is for National_Park:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.20.29%20PM.png)
* This picture is for States:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.20.47%20PM.png)
* This picture is for Topics:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.20.56%20PM.png)
* This picture is for Types:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.21.21%20PM.png)




## How to use
1. You may need first loading http://localhost:5000/[also the first route] to make the application running.
2. Then you can either go to other routes by the links on the home page or type the URLs of other four routes to go to other pages.
3. Be careful about the fifth route because it requires you to make a plan by route four(`/plan`) before then follow the instruction to go to the fifth route.
4. Please follow the instruction listed on the page and listed following to make sure the application running well. Enjoy it!

## Routes in this application
### First route(`/`)
- `/` -> The home page of the Flask application. This page is a form that users need to input their name, email and password to register(used a new module called "wtforms"). After they submit the information and click the button they will directly go to the '/all_info' page.
* In this page, you will see a following picture. And this is a reusable form that users can input their information to register, once they register successfully, they will be directed to the second route without typing in the URL bar. And I have links in the views of the Flask application page/s that allow a user to navigate the application and view all its routes without typing in the URL bar (after first loading http://localhost:5000/[this first route] with the application running).
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.32.35%20PM.png)
* The following picture is what users will see after they register successfully.
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.32.56%20PM.png)

### Second route(`/all_info`)
- `/all_info` ->  In this route, the application shows all parks with their type, all topics with their values, all activities with their values and all states with their values. Here I used the JavaScript files in the application that affect the view in html template.
* Once you submit successfully in the home page or you type the url of second route or you click the link of second route, you will be directed to all_info page. And you will see the following picture:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.24.54%20PM.png)
* And you will see this page looks like the following picture, it shows all National_Park names with their type.
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.25.30%20PM.png)
* And this following picture shows all topics with their values.
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.25.52%20PM.png)
* And this following picture shows all activities with their values.
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.26.17%20PM.png)
* And this following picture shows all states with their values.
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.26.26%20PM.png)


### Third route(`/parks`)
- `/parks` -> The detailed information of all parks including name, type, location, description and states. Here I also used the JavaScript files in the application that affect the view in html template, and I used table in the html in order to make the parks information in order.
* You will see the following picture once you go to this route. And here I used a table to show the parks information.
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.33.15%20PM.png)

### Fourth route(`/plan`)
- `/plan` -> In this route, there is an instruction telling users how to input values into the pop-up Dialog Box. In this way, the application will give users a url. Once users input the url, they will directly go to the next route `/query_example` to get their searching results.
* This picture shows the instruction of this route, please follow this instruction while inputting values:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.51.56%20PM.png)
* Once you click the "Enter Value" button, you will see the following picture. First please input the value of you selected state (here I choose "UT")
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.39.22%20PM.png)
* Secondly, please input the value of your selected activity(here I choose "31")
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.39.34%20PM.png)
* Finally, please input the value of your selected topic(here I choose "6")
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.39.45%20PM.png)
* Then you will get the URL of your selection result.
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.40.57%20PM.png)
* The following pictures are another example with state value="MI", activity value="3", topic value="9":
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.42.55%20PM.png)
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.43.04%20PM.png)
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.43.36%20PM.png)




### Fifth route(`/query_example`)
- `/query-example` -> The detail of a user's selection.(e.g.http://127.0.0.1:5000/query-example?state=AK&activity=3&topic=4) After users run this route, the original website including the parks satisfied their inputs and the clear information will automatically show up(used a new module called "selenium"), and the flask page will show the result text and parks' name of the searching results.
* You will see the following picture in the flask page:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%2011.29.33%20PM.png)
* Followed by the example given in fourth route(state value="UT", activity value="31", topic value="6"), once the user input the given url, they will see a pop-up website like this, this website id the original website of user selection. Here please wait with patience because it usually need 10 seconds to make everything in order.
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.41.43%20PM.png)
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.41.51%20PM.png)
* And the flask page will give the result like this(Because there is no park satisfying this selection):
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/2.png)
* Followed by the example(state value="MI", activity value="3", topic value="9"), users will see:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.44.11%20PM.png)
* And the flask page will give the result like this:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/1.png)
* And if you have a selection like state value="MI", you will see the following result:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/3.png)





## How to run tests
1. `cd` into where the project lives, run the "SI507project_tools.py" First
```
python SI507project_tools.py
```
2. Then just run the "SI507project_tests.py" file to see whether this program going well
```
python SI507project_tests.py
```
3. Then you will see the following picture:
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/4.png)

## In this repository:
- Templates
  - index.html
  - all_info.html
  - parks.html
  - plan.html
  - query_example.html
- SI507project_tools.py
- SI507project_tests.py
- parks.csv
- advanced_expiry_caching.py
- chromedriver
- README.md
- requirements.txt
- db.final
* ![Alt text](https://github.com/zuyicai/image/blob/master/final_project/Screen%20Shot%202019-04-24%20at%209.17.27%20PM.png)

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

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
