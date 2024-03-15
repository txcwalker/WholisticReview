from flask import Flask, render_template, Blueprint

#Python code for the contact us page on wholisticreview.com
#Nothing requiring python is on this page for now
#Date of last edit 03/07/2024

contact_us = Blueprint("contact_us", __name__, template_folder = 'templates')

@contact_us.route('/contact_us')
def show_contact_us():
    return render_template('_contact_us.html')