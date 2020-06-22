from datetime import timedelta


def convert_time_to_string(seconds):
    return str(timedelta(seconds=int(seconds)))
