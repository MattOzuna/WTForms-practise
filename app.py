from flask import Flask, render_template, flash, redirect, render_template
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)

@app.route('/')
def home_page():
    '''shows list of pets'''
    pets= Pet.query.all()
    return render_template('home-page.html', pets=pets)

@app.route('/add')
def add_pet():
    '''shows form to add pet to db'''
    form = AddPetForm()
    return render_template('add-pet.html', form=form)