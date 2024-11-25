from datetime import datetime


def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%H:%M:%S")
