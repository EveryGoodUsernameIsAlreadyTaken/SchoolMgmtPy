"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import SchoolMgmtWebPy2.views
app.config['SECRET_KEY'] = 'YEK_TERCES'