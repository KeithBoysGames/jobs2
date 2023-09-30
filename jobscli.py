import csv
import pandas as pd

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

def save_jobs(jobs):
    pd.DataFrame(jobs).to_csv('jobs.csv', index=False)

def save_bid(bids):
    pd.DataFrame(bids).to_csv('bids.csv', index=False)


def display_menu():
    print("1: Add Job")
    print("2: View Jobs")
    print("3: Update Job")
    print("4: Delete Job")
    print("5: Add Bid")
    print("6: View Bids")
    print("7: Update Bid")
    print("8: Delete Bid")
    print("9: Exit")
    
def add_job(jobs):
    job_id = input("Enter Job ID: ")
    client_name = input("Enter Client Name: ")
    location = input("Enter Location: ")
    start_date = input("Enter start date:")
    estimated_completion_date = input("Enter Estimated Completion Date: ")
    total_price = input("Enter Total Price: ")
    team_members = input("Enter Team Members (comma-separated): ")
    progress = input("Enter Progress (%): ")
    
    new_job = {
        "Job ID": job_id,
        "Client Name": client_name,
        "Location": location,
        "Start Date": start_date,
        "Total Price": total_price,
        "Team Members": team_members,
        "Progress": progress,
        "Estimated Completion Date": estimated_completion_date
    }
    jobs.append(new_job)
    save_jobs(jobs)
    
def view_jobs(jobs):
    for job in jobs:
        print(job)
        
def update_job(jobs):
    job_id = input("Enter the Job ID to update: ")
    for job in jobs:
        if job["Job ID"] == job_id:
            for key in job.keys():
                print(f"{key}: {job[key]}")
                update = input(f"Update {key}? (y/n): ")
                if update.lower() == 'y':
                    new_value = input(f"New value for {key}: ")
                    job[key] = new_value
            save_jobs(jobs)
            return
    print("Job ID not found.")
    
def delete_job(jobs):
    job_id = input("Enter the Job ID to delete: ")
    for job in jobs:
        if job["Job ID"] == job_id:
            jobs.remove(job)
            save_jobs(jobs)
            print("Job deleted.")
            return
    print("Job ID not found.")

def add_bid(bids):
    bid_id = input("Enter Bid ID ")
    client_name = input("Enter Client Name: ")
    location = input("Enter Location: ")
    scope_of_work = input("Enter project details:")
    bid_date = input("Enter Date Of Bid:")
    total_material_estimate = input("Enter Estimate Of Material:")
    total_labor_estimate = input("Enter Total Labor Estimate")
    total_bid_estimate = input("Enter Grand Total Estimate: ")
    total_onsite_workers = input("Enter onsite workers (comma-separated): ")
    status = input("Enter Status Of Bid: ")

    new_bid = {
        "Bid ID": bid_id,
        "Client Name": client_name,
        "Location": location,
        "Scope of Work": scope_of_work,
        "Bid Date": bid_date,
        "Material Estimate": total_material_estimate,
        "Labor Estimate": total_labor_estimate,
        "Total Estimate": total_bid_estimate,
        "Total onsite Workers": total_onsite_workers,
        "Status of Bid": status 
    }

    bids.append(new_bid)
    save_bid(bids)

def view_bids(bids):
    for bid in bids:
        print(bid)

def update_bid(bids):
    bid_id = input("Enter the Bid ID to update: ")
    for bid in bids:
        if bid["bid ID"] == bid_id:
            for key in bid.keys():
                print(f"{key}: {bid[key]}")
                update = input(f"Update {key}? (y/n): ")
                if update.lower() == 'y':
                    new_value = input(f"New value for {key}: ")
                    bid[key] = new_value
            save_jobs(bids)
            return
    print("Bid ID not found.")

def delete_bid(bids):
    bid_id = input("Enter the Bid ID to delete: ")
    for bid in bids:
        if bid["Bid ID"] == bid_id:
            bids.remove(bid)
            save_jobs(bids)
            print("Bid deleted.")
            return
    print("Bid ID not found.")

def main():
    jobs = load_jobs()
    bids = load_bids()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_job(jobs)
        elif choice == '2':
            view_jobs(jobs)
        elif choice == '3':
            update_job(jobs)
        elif choice == '4':
            delete_job(jobs)
        elif choice == '5':
            add_bid(bids)
        elif choice == '6':
            view_bids(bids)
        elif choice == '7':
            update_bid(bids)
        elif choice == '8':
            delete_bid(bids)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
