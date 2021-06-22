from flask import send_from_directory

def send_image(filename):
    return send_from_directory("file",filename)