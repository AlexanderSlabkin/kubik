from flask import render_template

from egg_break import my_app

@my_app.route('/')
@my_app.route('/home')
def home_page():
    return render_template('base.html')
