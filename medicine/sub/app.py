import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    with open('medicine_info.csv', 'r') as f:
        reader = csv.DictReader(f)
        results = [row['Description'] for row in reader if keyword.lower() in row['Drug_Name'].lower()]
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
