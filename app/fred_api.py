# fred_api.py
from flask import Blueprint, jsonify
from pymongo import MongoClient
import requests

fred_api_bp = Blueprint('fred_api', __name__)

# MongoDB connection setup
mongo_conn_string = 'mongodb+srv://bdat1004:1004@1004.vza4tnd.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(mongo_conn_string)
db = client['economic_data']
series_collection = db['economic_series']

# FRED API key (replace with your own key)
fred_api_key = '84c9fee4c73a34c042cab0f2b48c45f2'

# Define economic indicators and their series IDs
indicators = {
    'GDP': 'GDPC1',
    'Unemployment Rate': 'UNRATE',
    'Inflation Rate': 'CPIAUCNS',
}

def fetch_and_store_economic_data(series_id):
    url = f'https://api.stlouisfed.org/fred/series/observations'
    params = {
        'series_id': series_id,
        'api_key': fred_api_key,
        'file_type': 'json',
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Ensure data is not empty
    if 'observations' in data and data['observations']:
        observations = [{'date': obs['date'], 'value': float(obs['value'])} for obs in data['observations']]
        series_collection.update_one({'id': series_id}, {'$set': {'observations': observations}}, upsert=True)
        return True
    else:
        return False

# API endpoint to fetch and store economic data
@fred_api_bp.route('/fetch-and-store/<indicator>', methods=['GET'])
def fetch_and_store_data(indicator):
    series_id = indicators.get(indicator)
    if series_id:
        fetch_and_store_economic_data(series_id)
        return jsonify({'success': True, 'message': f'{indicator} data fetched and stored successfully in MongoDB'})
    else:
        return jsonify({'success': False, 'message': 'Invalid indicator'})
