from flask import render_template, Blueprint

finding_flights = Blueprint("finding_flights", __name__, template_folder = 'templates')

@finding_flights.route('/Flight/finding_flights')
def show_finding_flights():
    return render_template('flight_finding.html')