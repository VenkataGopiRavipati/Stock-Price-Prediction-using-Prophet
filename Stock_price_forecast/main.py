import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import sys

try:
    from prophet import Prophet  # Ensure correct import
except ModuleNotFoundError:
    print("Error: The 'prophet' package is not installed. Please install it using 'pip install prophet'.")
    sys.exit(1)


def get_stock_data(stock_symbol, period='1y'):
    """Fetch historical stock data."""
    stock = yf.Ticker(stock_symbol)
    df = stock.history(period=period)
    if df.empty:
        print(f"Error: No data found for stock symbol '{stock_symbol}'. Please check the symbol and try again.")
        sys.exit(1)
    stock_info = stock.info
    exchange = stock_info.get('exchange', 'Unknown')
    print(f"Stock {stock_symbol} is listed on {exchange}.")
    df.reset_index(inplace=True)
    df['Date'] = df['Date'].dt.tz_localize(None)  # Remove timezone info
    df = df[['Date', 'Close']]
    df.columns = ['ds', 'y']  # Prophet requires these column names
    return df


def predict_future_prices(stock_symbol, days=30):
    """Predict future stock prices using Facebook Prophet."""
    df = get_stock_data(stock_symbol)
    try:
        model = Prophet()
        model.fit(df)
    except Exception as e:
        print(f"Error occurred while fitting the Prophet model: {e}")
        sys.exit(1)

    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)

    return df, forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]


def plot_forecast(df, forecast, stock_symbol):
    """Plot actual vs predicted stock prices."""
    plt.figure(figsize=(10, 5))
    plt.plot(df['ds'], df['y'], label='Actual Prices', color='blue')
    plt.plot(forecast['ds'], forecast['yhat'], label='Predicted Prices', color='red')
    plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='pink', alpha=0.3)
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title(f'Stock Price Prediction for {stock_symbol}')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    stock_symbol = input("Enter stock symbol: ").strip().upper()
    df, forecast = predict_future_prices(stock_symbol)
    print(forecast.tail())
    plot_forecast(df, forecast, stock_symbol)
