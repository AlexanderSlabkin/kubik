from flask import render_template, redirect, request, url_for, flash
from flask import jsonify

from flask_login import current_user, login_user, logout_user, login_required

from egg_break import my_app, db
from egg_break.forms import LoginForm
from egg_break.models import User


@my_app.route('/', methods=['GET', 'POST'])
@my_app.route('/home', methods=['GET', 'POST'])
def home_page():
#    if request.method == 'POST':
#        redirect(url_for('game'))
    return render_template('base.html')


@my_app.route('/game')
def game():
    return render_template('game.html')


@my_app.route('/login', methods=['GET', 'POST'])
def my_login():
    if current_user.is_authenticated:
        return redirect(url_for('game'))
    form = LoginForm()
    print('KEK')
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            login_user(user)
            flash(f'Welcome back {user.username}')
            return redirect(url_for('home_page'))
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        print(f'LOOOOOL {user.username}')
        login_user(user)
        flash(f'You name in current session is {user.username}', 'info')
        return redirect(url_for('game'))
    return render_template('login.html', form = form)


@my_app.route('/logout')
def my_logout():
    logout_user()
    return redirect(url_for('home_page'))


@login_required
@my_app.route('/profile/{username}')
def profile():
    return render_template('profile.html')
