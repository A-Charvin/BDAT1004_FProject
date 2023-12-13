# BDAT1004_FProject
Final project for BDAT 1004

pip install -r requirements.txt

## Economic Data Dashboard with FRED API and MongoDB

This project creates a web dashboard to visualize economic data fetched from the Federal Reserve Economic Data (FRED) API and stored in a MongoDB database. It allows users to explore different economic indicators like GDP, unemployment rate, and inflation rate, and provides an interactive way to understand economic trends.

**Technologies:**

* Python
* Flask
* pymongo
* Dash
* plotly.express
* MongoDB

**Installation and Setup:**

1. Install the required dependencies:

```bash
pip install Flask pymongo requests dash dash-daq plotly pandas
```

2. Clone the repository and configure MongoDB connection details in `fred_api.py` and `economic_dashboard.py`.

3. Run the `update_data.py` script to fetch and store initial data.

4. Run the Flask app with:

```bash
python economic_dashboard.py
```

**Using the Dashboard:**

1. Open http://localhost:5000 in your web browser.
2. Choose an economic indicator from the dropdown menu.
3. The interactive line chart will display the selected indicator's data over time.

**Features:**

* Fetch and store economic data from the FRED API using a dedicated function.
* Update data periodically to maintain freshness.
* Interactive dashboard with a dropdown menu for selecting indicators.
* Plotly chart visualization with configurable axes and title.

**Future Work:**

* Implement additional filtering options like date range selection.
* Add features like comparison charts for multiple indicators.
* Explore integration with other data sources beyond FRED.

**Resources:**

* FRED API Documentation: [https://fred.stlouisfed.org/docs/api/fred/](https://fred.stlouisfed.org/docs/api/fred/)
* Dash Tutorial: [https://dash.plotly.com/tutorial](https://dash.plotly.com/tutorial)
* MongoDB Documentation: [https://www.mongodb.com/docs/](https://www.mongodb.com/docs/)

**Contributing:**

We welcome contributions to this project! Feel free to fork the repository, propose improvements, and submit pull requests.

