from flask import Flask, render_template, url_for, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/breathing')
def breathing():
    return render_template('breathing_exercises.html')