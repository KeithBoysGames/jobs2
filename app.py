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
    with open('C:\\Users\\dusti\\OneDrive\\Desktop\\Jobs\\bids.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([client_name, contact_info, address, material_total, labor_total, timeframe])


@app.route('/submit_job', methods=['POST'])
def submit_job():
    client_name = request.form.get('client_name')
    contact_info = request.form.get('contact_info')
    location = request.form.get('location')
    start_date = request.form.get('start_date')
    estimated_enddate = request.form.get('estimated_enddate')
    onsite_workers = request.form.get('onsite_workers')
    total_price = request.form.get('total_price')
    progress = request.form.get('progress')

    # Write to jobs.csv
    with open('C:\\Users\\dusti\\OneDrive\\Desktop\\Jobs\\jobs.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([client_name, contact_info, location, start_date, estimated_enddate, onsite_workers, total_price, progress])

    # Redirect back to the home page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
