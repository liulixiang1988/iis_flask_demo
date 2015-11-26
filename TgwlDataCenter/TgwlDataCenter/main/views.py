# -*- coding:utf-8 -*-


from datetime import datetime
from flask import render_template

from TgwlDataCenter import db
from TgwlDataCenter.models import Fruit
from TgwlDataCenter.main import main

@main.route('/')
@main.route('/home')
def home():
    """Renders the home page."""
    fruit = Fruit(fruit=u"苹果")
    db.session.add(fruit)
    db.session.commit()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@main.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@main.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
