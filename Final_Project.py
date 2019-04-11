# The final project sequence has 3 total assignments, as follows:
# Final Project Proposal - Due Wednesday, April 10 - total 1000 points
# Final Project Check-In Assignment - Due Wednesday, April 17 - total 500 points
# Final Project (final submission) - Due Thursday, April 25 - total 4000 points

# flask application



from flask import Flask, render_template
# import statements

# Set up application
app = Flask(__name__)

# Routes
@app.route('/')#http://127.0.0.1:5000/
def home_page():
    nu_movie = Movie
    return '<h1> {} movies recorded</h1>'.format(nu_movie.length)
    #(results will depend upon how many movies are in your movies_clean.csv file…!)


if __name__ == '__main__':
    app.run()
