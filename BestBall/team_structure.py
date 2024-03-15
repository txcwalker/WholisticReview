from flask import render_template, Blueprint

team_structure = Blueprint("team_structure", __name__, template_folder = 'templates')

@team_structure.route('/BestBall/team_structure')
def show_team_structure():
    return render_template('best_ball_team_structure.html')