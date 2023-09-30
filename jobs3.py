import tkinter as tk
from tkinter import ttk, simpledialog
import pandas as pd

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Job and Bid Management")
        self.geometry("1200x600")

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
        new_job = {
            "Job ID": simpledialog.askstring("Input", "Enter Job ID:"),
            "Client Name": simpledialog.askstring("Input", "Enter Client Name:"),
            "Location": simpledialog.askstring("Input", "Enter Job Location:"),
            "Contact Info": simpledialog.askstring("Input", "Enter Contact Info:"),
            "Start Date": simpledialog.askstring("Input", "Enter Start Date:"),
            "End Date": simpledialog.askstring("Input", "Enter End Date:")
        }
        self.jobs.append(new_job)
        self.save_jobs()
        self.refresh_jobs_data()

    def add_bid(self):
        new_bid = {
            "Client Name": simpledialog.askstring("Input", "Enter Client Name:"),
            "Location": simpledialog.askstring("Input", "Enter Location:"),
            # ... Add more fields as per your requirements
        }
        self.bids.append(new_bid)
        self.save_bids()
        self.refresh_bids_data()

    def refresh_jobs_data(self):
        for row in self.tree_jobs.get_children():
            self.tree_jobs.delete(row)
        for i, job in enumerate(self.jobs):
            self.tree_jobs.insert("", i, values=(
                job["Job ID"], job["Client Name"], job["Location"], job["Contact Info"], job["Start Date"], job["End Date"]
            ))

    def refresh_bids_data(self):
        for row in self.tree_bids.get_children():
            self.tree_bids.delete(row)
        for i, bid in enumerate(self.bids):
            self.tree_bids.insert("", i, values=(
                bid["Client Name"], bid["Location"]
                # ... Add more fields to display as per your requirements
            ))

    def create_widgets(self):
        ttk.Label(self, text="Jobs").grid(column=0, row=0)
        ttk.Label(self, text="Bids").grid(column=2, row=0)

        self.tree_jobs = ttk.Treeview(self, 
                                      columns=("Job ID", "Client Name", "Location", "Contact Info", "Start Date", "End Date"), 
                                      show="headings")
        # ... Setting headers and displaying the tree for jobs

        self.tree_bids = ttk.Treeview(self, 
                                      columns=("Client Name", "Location"), 
                                      show="headings")
        # ... Setting headers and displaying the tree for bids

        # Add buttons
        ttk.Button(self, text="Add Job", command=self.add_job).grid(column=0, row=2)
        ttk.Button(self, text="Add Bid", command=self.add_bid).grid(column=2, row=2)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
