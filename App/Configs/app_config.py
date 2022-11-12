



config = {

    'information': {
        'author': 'allelleo',
        'project_version': 0.4,
        'api_version': 1,
        "DataBase_version": 1.25,
        "Defense_version": 0.1,
        'Logs_version': 0.01,
    },
    'app': {
        'SECRET_KEY': "allelleo-secret-key",
        "JSON_AS_ASCII": False,
        "APPLICATION_ROOT": "/",
        "MAX_COOKIE_SIZE": 8192,
        "HOST": "localhost",
        "PORT": 5000,
    },
    'api': {
        'version': 1,
    },
    "DataBase": {
        'driver': 'sqlite3',
        'User': {
            'profile': {
                'all_sex': {
                    '0': 'Not stated',
                    '1': 'Male',
                    '2': 'Female',
                },
                'all_status': {
                    '0': 'Not stated',
                },
            },
            "users": {},
        },
    },
    "Defense": {},
    "Logs": {},
}


def init_app(app):
    app.config['SECRET_KEY'] = config['app']['SECRET_KEY']
    app.config['JSON_AS_ASCII'] = config['app']['JSON_AS_ASCII']
    app.config['APPLICATION_ROOT'] = config['app']['APPLICATION_ROOT']
    app.config['MAX_COOKIE_SIZE'] = config['app']['MAX_COOKIE_SIZE']
    return app
