# fetch_data_script.py
from app.fred_api import fetch_and_store_economic_data
from apscheduler.schedulers.blocking import BlockingScheduler

# Add your series IDs here
series_ids = ['GDPC1', 'UNRATE', 'CPIAUCNS']

def fetch_data_job():
    for series_id in series_ids:
        success = fetch_and_store_economic_data(series_id)
        if success:
            print(f'Data fetched and stored for {series_id}')
        else:
            print(f'Failed to fetch data for {series_id}')

# Create scheduler
scheduler = BlockingScheduler()
# Run the job every 14 hours
scheduler.add_job(fetch_data_job, 'interval', hours=24)
# Start the scheduler
scheduler.start()
