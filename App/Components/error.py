import flask

error = flask.Blueprint("error", __name__)


@error.errorhandler(404)
def not_found_error(err):
    return flask.render_template('Error_pages/404.html'), 404


@error.errorhandler(400)
def bad_request_error(err):
    return flask.render_template('Error_pages/400.html'), 400


@error.errorhandler(401)
def unauthorized_error(err):
    return flask.render_template('Error_pages/401.html'), 401


@error.errorhandler(403)
def forbidden_error(err):
    return flask.render_template('Error_pages/403.html'), 403


@error.errorhandler(500)
def internal_server_error(err):
    return flask.render_template('Error_pages/500.html'), 500


@error.errorhandler(502)
def bad_gateway_error(err):
    return flask.render_template('Error_pages/502.html'), 502
