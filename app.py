import os
from flask import Flask, flash, request, redirect, render_template, send_from_directory, url_for
import pilotRoy as pr

app = Flask(__name__)
app.secret_key = os.urandom(24)
# home page
@app.route('/', methods=['POST', 'GET'])
def render_home():
    if request.method == 'POST':
        print("HELLOOOO" + request.form['pages'])
        input_pages = request.form['pages']
        questions = pr.generate(input_pages)
        return questions
    # render the home page
    return render_template('index.html')
    
@app.route('/generate', methods=['POST', 'GET'])
def render_generated():
    if request.method == 'POST':
        input_pages = request.form['pages']
        questions = pr.generate(input_pages)
        return render_template('index.html', questions=questions)

# main
if __name__ == "__main__":
    app.run()