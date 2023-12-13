# update_data.py
from datetime import datetime, timedelta
from fred_api import fetch_and_store_economic_data, indicators

# Run this script periodically (e.g., every 14 hours) to update data in the database

def update_data():
    for indicator, series_id in indicators.items():
        fetch_and_store_economic_data(series_id)
        print(f'{indicator} data updated at {datetime.now()}')

if __name__ == '__main__':
    update_data()
