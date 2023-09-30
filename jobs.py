import tkinter as tk
from tkinter import ttk, simpledialog
import pandas as pd

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Job and Bid Management")
        self.geometry("800x600")

        self.jobs = self.load_jobs()
        self.bids = self.load_bids()

        self.create_widgets()

    def load_jobs(self):
        try:
            return pd.read_csv('jobs.csv').to_dict('records')
        except FileNotFoundError:
            return []

    def load_bids(self):
        try:
            return pd.read_csv('bids.csv').to_dict('records')
        except FileNotFoundError:
            return []

    def save_jobs(self):
        pd.DataFrame(self.jobs).to_csv('jobs.csv', index=False)

    def save_bids(self):
        pd.DataFrame(self.bids).to_csv('bids.csv', index=False)

    def add_job(self):
        new_job = {}
        new_job['Job ID'] = simpledialog.askstring("Input", "Enter Job ID:")
        new_job['Client Name'] = simpledialog.askstring("Input", "Enter Client Name:")
        new_job['Client Address'] = simpledialog.askstring("Input", "Enter Clients Address:")
        new_job['Client Contact Info'] = simpledialog.askstring("Input", "Enter Clients Contact Info:")
        new_job['Job Location'] = simpledialog.askstring("Input", "Enter Job Location:")
        new_job['Start Date'] = simpledialog.askstring("Input", "Enter Start Date:")
        new_job['Estimated Completion Date'] = simpledialog.askstring("Input", "Enter Estimated End Date:")
        new_job['Workers on site'] = simpledialog.askstring("Input", "Enter Employee Names:")
        new_job['Money Received'] = simpledialog.askstring("Input", "Enter any monies recieved:")
        # ... Collect the rest of the job details in a similar manner
        self.jobs.append(new_job)
        self.save_jobs()
        self.refresh_data()

    def add_bid(self):
        new_bid = {}
        new_bid['Client Name'] = simpledialog.askstring("Input", "Enter Client Name:")
        new_bid['Clients Address'] = simpledialog.askstring("Input", "Enter Clients Address:")
        # ... Collect the rest of the bid details in a similar manner
        self.bids.append(new_bid)
        self.save_bids()
        self.refresh_data()

    def refresh_data(self):
        for row in self.tree_jobs.get_children():
            self.tree_jobs.delete(row)
        for i, job in enumerate(self.jobs):
            self.tree_jobs.insert("", i, values=(job["Job ID"], job["Client Name"]))

    def refresh_data(self):
        for row in self.tree_bids.get_children():
            self.tree_bids.delete(row)
        for i, bid in enumerate(self.bids):
            self.tree_bids.insert("", i, values=(bid["Bid ID"], bid["Client Name"]))
        # Do the same for bids

    def create_widgets(self):
        ttk.Label(self, text="Jobs").grid(column=0, row=0)
        ttk.Label(self, text="Bids").grid(column=1, row=0)

        self.tree_jobs = ttk.Treeview(self, columns=("Job ID", "Client Name"), show="headings")
        self.tree_jobs.heading("Job ID", text="Job ID")
        self.tree_jobs.heading("Client Name", text="Client Name")
        self.tree_jobs.grid(column=0, row=1)

        self.tree_bids = ttk.Treeview(self, columns=("Client Name", "Location"), show="headings")
        self.tree_bids.heading("Client Name", text="Client Name")
        self.tree_bids.heading("Location", text="Location")
        self.tree_bids.grid(column=1, row=1)

        for i, job in enumerate(self.jobs):
            self.tree_jobs.insert("", i, values=(job["Job ID"], job["Client Name"]))

        for i, bid in enumerate(self.bids):
            self.tree_bids.insert("", i, values=(bid["Client Name"], bid["Location"]))

        ttk.Button(self, text="Add Job", command=self.add_job).grid(column=0, row=2)
        ttk.Button(self, text="Add Bid", command=self.add_bid).grid(column=1, row=2)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
