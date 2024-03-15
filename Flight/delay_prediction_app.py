from flask import render_template, Blueprint

delay_prediction_app = Blueprint("delay_prediction_app", __name__, template_folder = 'templates')

@delay_prediction_app.route('/Flight/delay_prediction_app')
def show_delay_prediction_app():
    return render_template('flight_delay_prediction_app.html')