# Cryptocurrency Data Fetcher & Analyzer

This Python script fetches live cryptocurrency data from CoinMarketCap, analyzes it, and saves the results to an Excel file. It fetches the top 50 cryptocurrencies, performs analysis on their market capitalizations, price changes, and trading volumes, and stores the data in a structured format for further use.

## Requirements

Before you begin, ensure you have the following libraries installed:

* `requests`: For making HTTP requests to the CoinMarketCap API.
* `pandas`: For data manipulation and analysis.
* `schedule`: For scheduling tasks at regular intervals.
* `openpyxl`: For writing Excel files.

You can install them using pip:

<pre class="!overflow-visible">
  <code class="!whitespace-pre hljs language-bash">
    pip install requests pandas schedule openpyxl
  </code>
</pre>

## Setup

### 1. API Key

You need a valid API key from CoinMarketCap to access the data. You can obtain your API key by signing up for the [CoinMarketCap API](https://coinmarketcap.com/) service.

Replace `'YOUR_API_KEY'` in the script with your actual API key.

### 2. Configuration

The script fetches the latest cryptocurrency data for the top 50 cryptocurrencies, with their prices, market capitalizations, and 24-hour trading volume in USD.

### 3. Script Functions

* **`fetch_data()`** : This function sends a GET request to the CoinMarketCap API to fetch live cryptocurrency data.
* **`analyze_and_save()`** : This function fetches the data, performs the following analyses, and saves the results to an Excel file:
* **Top 5 Cryptocurrencies by Market Capitalization**
* **Average Price of Top 50 Cryptocurrencies**
* **Highest and Lowest 24h Price Changes**
* The data is saved in two Excel sheets:
  * `Live Data`: Contains data for the top 50 cryptocurrencies.
  * `Top 5`: Contains data for the top 5 cryptocurrencies by market capitalization.

### 4. Scheduling

The script uses the `schedule` library to fetch and analyze the data every 5 minutes. It starts by fetching data immediately upon running and then continues fetching live updates at the specified interval.

### 5. Running the Script

To run the script, simply execute the Python file:

<pre class="!overflow-visible">
  <code class="!whitespace-pre hljs language-bash">
    python assignment.py
  </code>
</pre>

The script will:

1. Fetch the data immediately.
2. Perform analysis and save the results to an Excel file.
3. Continue to fetch data and perform analysis every 5 minutes.

### 6. Output

The script generates an Excel file named `live_crypto_data.xlsx` containing the following sheets:

* **Live Data** : Displays data for the top 50 cryptocurrencies, including name, symbol, price in USD, market cap, 24h trading volume, and price change in the last 24 hours.
* **Top 5** : Displays the top 5 cryptocurrencies by market capitalization.

You can open this file with Excel or any compatible spreadsheet software.

## Example Output

<pre class="!overflow-visible">
  <code class="!whitespace-pre hljs language-bash">
  
 
Fetching data...
{'status': {'timestamp': '2024-12-23T12:00:00Z', 'error_code': 0, 'error_message': '', 'elapsed': 10, 'credit_count': 1, 'notice': ''}, 'data': [...]}

--- Analysis ---
Top 5 Cryptocurrencies by Market Cap:
      Name  Market Capitalization
0   Bitcoin          880000000000
1   Ethereum         400000000000
2   Binance Coin     65000000000
3   Cardano          47000000000
4   XRP              38000000000

Average Price of Top 50 Cryptocurrencies: $1050.50
Highest 24h Price Change: 12.50%
Lowest 24h Price Change: -7.10%

Data saved to live_crypto_data.xlsx
 </code>
</pre>

## Notes

* The script only fetches data for the top 50 cryptocurrencies.
* The data is refreshed every 5 minutes, but you can adjust the interval in the `schedule.every(5).minutes` line of the script.
* Ensure that API key remains secure and is not exposed in public repositories.
