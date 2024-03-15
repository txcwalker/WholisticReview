from flask import Flask, render_template, Blueprint

#Python code for the about us page on wholisticreview.com
#Nothing requiring python is on this page for now
#Date of last edit 03/07/2024

about = Blueprint("about", __name__, template_folder = 'templates')

@about.route('/about')
def show_about():
    return render_template('_about.html')