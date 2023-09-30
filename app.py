from flask import Flask, render_template, request, redirect
import csv
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Normally, you'd read in 'jobs.csv' and 'bids.csv' here and pass them to the template
    # For this example, we'll pass empty lists.
    return render_template('index.html', jobs=[], bids=[])

@app.route('/submit_bid', methods=['POST'])
def submit_bid():
    client_name = request.form.get('client_name')
    contact_info = request.form.get('contact_info')
    address = request.form.get('address')
    material_total = request.form.get('material_total')
    labor_total = request.form.get('labor_total')
    timeframe = request.form.get('timeframe')

    # Write to bids.csv
    with open('bids.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([client_name, contact_info, address, material_total, labor_total, timeframe])

    # Redirect back to the home page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
