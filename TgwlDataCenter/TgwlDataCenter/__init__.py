"""
The flask application package.
"""
import os
from flask import Flask
from .config import config

app = Flask(__name__)
app.config.from_object(config[os.environ.get('TGWL_CONFIG')])

import TgwlDataCenter.views
