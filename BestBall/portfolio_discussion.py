from flask import render_template, Blueprint

portfolio_discussion = Blueprint("portfolio_discussion", __name__, template_folder = 'templates')

@portfolio_discussion.route('/BestBall/portfolio_discussion')
def show_portfolio_discussion():
    return render_template('best_ball_portfolio_discussion.html')