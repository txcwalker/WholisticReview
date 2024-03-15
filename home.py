from flask import render_template, Blueprint

#Python code for the home page on wholisticreview.com
#Nothing requiring python is on this page for now
#Date of last edit 03/07/2024

home = Blueprint("home", __name__, template_folder = 'templates')

@home.route('/Home') #path name
def show_home():
    return render_template('_home.html')  #file name