from flask import render_template, Blueprint

tournament_selection = Blueprint("tournament_selection", __name__, template_folder = 'templates')

@tournament_selection.route('/BestBall/tournament_selection')
def show_tournament_selection():
    return render_template('beset_ball_tournament_selection.html')