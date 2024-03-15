from flask import Flask, render_template, Blueprint

flight_home = Blueprint("flight_home", __name__, template_folder = 'templates')

@flight_home.route('/Flight')
def show_best_ball():
    return render_template('flight_home.html')