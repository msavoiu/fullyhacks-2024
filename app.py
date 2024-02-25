from flask import Flask, render_template, url_for, request, redirect
import random
# from turtle import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/breathing-exercises')
def breathing():
    return render_template('breathing.html')

@app.route('/getting-leaves')
def leaves():
    return render_template('get_leaves.html')

@app.route('/getting-leaves', methods=['POST'])
def leavesPost():
    leaves = request.form['leaf'] #comma separated string 'list'
    leaves_list = leaves.split(', ') # separating items into a real list
    return render_template('leaves.html', leaves = leaves_list)

@app.route('/leaves-on-a-stream')
def gettingLeaves():
    leaf_text = input("Enter your cause of stress: ")
    return render_template('leaves.html', leaf = leaf_text)

@app.route('/drawing')
def drawing():
    return render_template('drawings.html')

@app.route('/drawing-prompt')
def drawingPrompt():
    prompts_list = ["Something or someone that brings you comfort", "Something or someone that you are grateful for", "Different kinds of flowers", "Different kinds of animals", "Swiggles and ripples (ex. drop in water)", "Fanart of your favorite media", "Design clothing that you would want to wear", "The feeling of happiness", "The feeling of sadness", "The feeling of loneliness", "The feeling of love",  "The feeling of loneliness",  "The feeling of anger",  "The feeling of grief",  "The feeling of disgust",  "The feeling of jealousy",  "The feeling of excitement",  "The feeling of anxiety",  "The feeling of empowerment", "The feeling of acceptance", "Your brave space (an enviroment where you feel brave enough to express yourself)", "Family or friends", "Pets", "Favorite place", "Favorite food", "Favorite color"]
    index = random.randint(0, 25)
    random_prompt = prompts_list[index]

    return render_template('drawing_prompt.html', prompt = random_prompt)

@app.route('/reflection')
def reflection():
    return render_template('reflection.html')

if __name__ == '__main__':
    app.run(debug=True)