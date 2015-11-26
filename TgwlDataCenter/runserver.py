"""
This script runs the TgwlDataCenter application using a development server.
"""

from os import environ
from manage import manager

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    manager.run(default_command='runserver')
