from flask import Flask, render_template, Blueprint

#Python code for the contact us page on wholisticreview.com
#Nothing requiring python is on this page for now
#Date of last edit 03/07/2024

pricing = Blueprint("pricing", __name__, template_folder = 'templates')

@pricing.route('/Pricing') #path name
def show_pricing():
    return render_template('_pricing.html') #file name