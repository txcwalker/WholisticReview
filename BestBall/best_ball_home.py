from flask import Flask, render_template, Blueprint

best_ball_home = Blueprint("best_ball_home", __name__, template_folder = 'templates')

@best_ball_home.route('/BestBall')
def show_best_ball():
    return render_template('best_ball_home.html')