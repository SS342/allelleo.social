from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from DataBase.User.users import UsersDataBase, update_profile
from DataBase.User.profile import UserProfileDataBase
import flask
from Defense.passwords import Passwords
from Defense.token import generate_token

auth = flask.Blueprint("auth", __name__)

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return flask.redirect('/auth/sign-in')


@auth.route('/auth/sign-in', methods=['POST', 'GET'])
def sign_in():
    if flask.request.method == 'POST':
        email = flask.request.form['email']
        password = flask.request.form['password']
        print(f"USER LOGIN: {email} ~ {password}")
        user = UsersDataBase().get_user_by_email(email)
        if user:
            if Passwords().check_password(user.hashed_password, password):
                login_user(user)
                print(user)
                return flask.redirect(flask.url_for('home'))
    return flask.render_template('auth/sign-in.html')


@auth.route('/auth/sign-up', methods=['POST', "GET"])
def sign_up():
    if flask.request.method == 'POST':
        # : sql-injection checker;
        res = UsersDataBase().new_user(flask.request.form['nickname'], flask.request.form['email'],
                                       flask.request.form['name'], flask.request.form['surname'],
                                       Passwords().hash_password(flask.request.form['password']),
                                       token=generate_token())
        print(res['status'].type)
        if res['status'].type == "Ok":
            return flask.redirect('/auth/sign-in')
        else:
            return flask.render_template('auth/sign-up.html', error=res['status'].message)
    return flask.render_template('auth/sign-up.html', error=None)


