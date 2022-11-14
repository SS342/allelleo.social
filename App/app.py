import flask
from flask_bcrypt import Bcrypt
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from DataBase.User.following_peoples import UserFollowingToUserDataBase
from DataBase.User.profile import UserProfileDataBase
from Logs.logs import Logs
from DataBase.User.users import UsersDataBase, update_profile
from Defense.passwords import Passwords
from Defense.token import generate_token
from API.api import api
from Configs.app_config import config, init_app
from Components.auth import auth
from Components.error import error

UserFollowingToUserDataBase()
UserProfileDataBase()
UsersDataBase()
Logs()

app = flask.Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'sign_in'
app = init_app(app)
app.register_blueprint(api, url_prefix="/api/v1")
app.register_blueprint(auth)
app.register_blueprint(error)


# INSERT INTO users (id, nickname, email, name, surname, hashed_passwords) VALUES (0, 'allelleo', 'alex2005ov@gmail.com', 'Alexey', 'Ovchinnikov', 'fc300febae3b9a55723b7aecab31ce4469af3ad26501a982e416c6ac3471bb06:5fee1bad50e54831b1b3d9ee3c814962')


@login_manager.user_loader
def load_user(user_id):
    user = UsersDataBase().get_user_by_id(user_id)
    if user:
        return user
    return None


@app.route('/home')
@login_required
def home():
    # print(current_user.avatar)
    return flask.render_template('main_pages/home.html', user=current_user)


@app.route('/my-profile')
@login_required
def my_profile():
    return flask.render_template('user/my-profile.html', user=current_user)


@app.route('/my-profile/edit', methods=['POST', 'GET'])
@login_required
def my_profile_edit():
    if flask.request.method == 'POST':
        data = {
            'user_id': current_user.id,
            'name': flask.request.form['name1'],
            'surname': flask.request.form['surname'],
            'nickname': flask.request.form['nickname'],
            'birth_date': flask.request.form['birth_date'],
            'email': flask.request.form['email'],
            'about': flask.request.form['about']
        }

        # print(data)
        update_profile(data, current_user)

    return flask.render_template('user/settings.html', user=current_user)


@app.route('/my-profile/connections')
def my_profile_connections():
    return flask.render_template('user/my-profile-connections.html', user=current_user,
                                 following_list=UserFollowingToUserDataBase().get_following(current_user.id))


HOST = config['app']['HOST']
PORT = config['app']['PORT']

app.run(debug=True, host=HOST, port=PORT)
