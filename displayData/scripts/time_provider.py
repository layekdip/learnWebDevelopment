from datetime import datetime


def get_time():
    today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    current_date_time = "Date-Time : {}".format(today)
    return current_date_time
