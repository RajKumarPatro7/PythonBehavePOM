from datetime import datetime


def generate_email():
    datetime.now().strftime("%dd_%mm_%yyyy_%HH_%MM_%SS")
