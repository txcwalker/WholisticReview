#This is the program that actually runs everything, the __init__ file just defines the programs as part of homemade package
#The Blueprints allow multiple instance of flask to be running at the same time
#Date of last edit: 03/07/2024

#Import statements
from flask import Flask, render_template
from home import home
from contact_us import contact_us
from about import about
from pricing import pricing
from YelpZillow import yelp_data_home, yelp_tag_graph_tool, yelp_heat_map_tool, yelp_jacksonville_example, yelp_search_score_report , zillow_analysis
from BestBall import best_ball_home, tournament_selection, portfolio_discussion, team_structure
from Flight import flight_home, delay_prediction_app, finding_flights

#Defining the app, if the name "app" changes then a whole bunch of things in the ubuntu/apache set up need to be changed to this name as well
app = Flask(__name__)

#Blueprints calling the different pages
#Base site pages
app.register_blueprint(home)
app.register_blueprint(contact_us)
app.register_blueprint(about)
app.register_blueprint(pricing)

#Project based blueprints
#Yelp/Zillow
app.register_blueprint(yelp_data_home)
app.register_blueprint(yelp_tag_graph_tool)
app.register_blueprint(yelp_heat_map_tool)
app.register_blueprint(yelp_jacksonville_example)
app.register_blueprint(yelp_search_score_report)
app.register_blueprint(zillow_analysis)

#BestBall
app.register_blueprint(best_ball_home)
app.register_blueprint(tournament_selection)
app.register_blueprint(portfolio_discussion)
app.register_blueprint(team_structure)

#Flight
app.register_blueprint(flight_home)
app.register_blueprint(delay_prediction_app)
app.register_blueprint(finding_flights)

#Default route
@app.route('/home')
@app.route('/')
def home():
    return render_template("_home.html")

#Running the flask app
if __name__ == '__main__':
    app.run(debug=True)
