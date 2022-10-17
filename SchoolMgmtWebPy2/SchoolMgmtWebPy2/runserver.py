"""
This script runs the SchoolMgmtWebPy2 application using a development server.
"""

from distutils.log import debug 
from os import environ
from SchoolMgmtWebPy2 import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug = True)