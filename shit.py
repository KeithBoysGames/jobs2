from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

def load_jobs():
    try:
        return pd.read_csv('jobs.csv').to_dict('records')
    except FileNotFoundError:
        return []

def load_bids():
    try:
        return pd.read_csv('bids.csv').to_dict('records')
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    # Load data, and pass it to the template
    jobs = load_jobs()
    bids = load_bids()
    return render_template('index.html', jobs=jobs, bids=bids)

@app.route('/add_job', methods=['POST'])
def add_job():
    # Collect data from the form and save it
    # TODO: Implement this functionality
    # ... 
    # return redirect to the main page
    return redirect(url_for('index'))

# TODO: Implement other routes (add_bid, delete_job, etc.)

if __name__ == '__main__':
    app.run(debug=True)
