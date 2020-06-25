from flask import Blueprint, render_template, session

page_home = Blueprint('page_home', __name__, template_folder='../templates')
@page_home.route("/", methods=['GET'])
def home():
    if 'user' in session:
        user = session['user']
    else:
        user = None
    print(user)
    return render_template('home.html', user=user)  # render a template
