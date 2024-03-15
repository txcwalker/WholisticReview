#__init__ file needed when flask is read into apache/ubuntu. This is the first file read and defines all of the below for the project
#This also allows for better organization so that not all of the files are in the same folder and stuff is easier to find
#Date of last edit: 03/07/2024

#Import statements
from flask import Flask, render_template

#Import base website pages
from .home import home
from .contact_us import contact_us
from .about import about
from .pricing import pricing

#Import project based webpages
#Import Yelp/Zillow Pages
from .YelpZillow import (yelp_data_home, yelp_tag_graph_tool, yelp_heat_map_tool, yelp_jacksonville_example,
                         yelp_search_score_report, zillow_analysis)
#Import Bestball Pages
from .BestBall import best_ball_home, tournament_selection, portfolio_discussion, team_structure

#Import Flight Data Pages
from .Flight import flight_home, delay_prediction_app, finding_flights

#Defining the app
app = Flask(__name__)

#Blueprint Registration
#Standard Webpage definitions
app.register_blueprint(home)
app.register_blueprint(contact_us)
app.register_blueprint(about)
app.register_blueprint(pricing)

#YelpZillow definitions
app.register_blueprint(yelp_data_home)
app.register_blueprint(yelp_tag_graph_tool)
app.register_blueprint(yelp_heat_map_tool)
app.register_blueprint(yelp_jacksonville_example)
app.register_blueprint(yelp_search_score_report)
app.register_blueprint(zillow_analysis)

#BestBall definitions
app.register_blueprint(best_ball_home)
app.register_blueprint(tournament_selection)
app.register_blueprint(portfolio_discussion)
app.register_blueprint(team_structure)

#Flight definitions
app.register_blueprint(flight_home)
app.register_blueprint(delay_prediction_app)
app.register_blueprint(finding_flights)


@app.route('/home')
@app.route('/')
def home():
    return render_template("_home.html")

if __name__ == '__main__':
    app.run(debug=True)


