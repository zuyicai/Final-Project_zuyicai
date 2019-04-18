# Final-Project_zuyicai

Zuyi Cai

[Link to this repository](https://github.com/zuyicai/Final-Project_zuyicai)

---

## Project Description

My Project is designed for people who want to search detailed information of National Parks in the US and who want to get a straightforward instruction of all parks. In my Flask application, users are able to get identical park travel plan determined by their own interests.

## How to run

1. First, you should ... (e.g. install all requirements with `pip install -r requirements.txt`)
2. Second, you should ... (e.g. run `python SI507project_tools.py` or whatever else is appropriate)
3. Anything else

## How to use

1. A useful instruction goes here
2. A useful second step here
3. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg)

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
