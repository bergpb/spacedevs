from datetime import timedelta


def convert_time_to_string(seconds):
    return str(timedelta(seconds=int(seconds)))


def init_app(app):
    app.jinja_env.filters["format_time_to_string"] = convert_time_to_string

