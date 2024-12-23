from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import schedule
import time

# API URL and Key
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
parameters = {
    'start': '1',
    'limit': '50',  # Fetch top 50 cryptocurrencies
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '89977ff1-6c25-492e-88dc-852a05bc922d',#YOUR_API_KEY
}

# Fetch live cryptocurrency data
def fetch_data():
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        # checking the data
        # print(data)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"Error fetching data: {e}")
        return None

# Analyze and save data to Excel
def analyze_and_save():
    print("Fetching data...")
    data = fetch_data()
    print(data,'my data')
    if not data or 'data' not in data:
        print("No data received.")
        return
    
    # Parse the fetched data
    crypto_list = []
    for crypto in data['data']:
        crypto_list.append({
            'Name': crypto['name'],
            'Symbol': crypto['symbol'],
            'Current Price (USD)': crypto['quote']['USD']['price'],
            'Market Capitalization': crypto['quote']['USD']['market_cap'],
            '24h Trading Volume': crypto['quote']['USD']['volume_24h'],
            '24h Price Change (%)': crypto['quote']['USD']['percent_change_24h']
        })

    # Create a DataFrame
    df = pd.DataFrame(crypto_list)

    # Data Analysis
    top_5 = df.nlargest(5, 'Market Capitalization')
    avg_price = df['Current Price (USD)'].mean()
    highest_change = df['24h Price Change (%)'].max()
    lowest_change = df['24h Price Change (%)'].min()

    print("\n--- Analysis ---")
    print("Top 5 Cryptocurrencies by Market Cap:\n", top_5[['Name', 'Market Capitalization']])
    print(f"Average Price of Top 50 Cryptocurrencies: ${avg_price:.2f}")
    print(f"Highest 24h Price Change: {highest_change:.2f}%")
    print(f"Lowest 24h Price Change: {lowest_change:.2f}%")

    # Save data to Excel
    with pd.ExcelWriter('live_crypto_data.xlsx', mode='w', engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Live Data', index=False)
        top_5.to_excel(writer, sheet_name='Top 5', index=False)
    
    print("Data saved to live_crypto_data.xlsx")

# Schedule the task to run every 5 minutes
schedule.every(5 ).minutes.do(analyze_and_save)

# Run the scheduler
print("Testing immediate data fetch...")
analyze_and_save()  # Run once immediately to test the function
print("Now starting live updates. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)