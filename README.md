
# Stock Price Prediction using Prophet

## Overview
This Python project predicts future stock prices using historical data and the Prophet model, a forecasting tool developed by Facebook. The project also provides details about the stock exchange and country based on the provided stock symbol.

### Key Features:
1. Fetches stock data for the last 5 years from Yahoo Finance.
2. Uses Prophet for time series forecasting of future stock prices (next 30 days).
3. Displays the stock's exchange and country based on its symbol.
4. Visualizes the forecasted prices along with the historical data.
5. Prints forecasted prices with confidence intervals.

## Installation

To run this project, you'll need to install the following Python libraries:

```bash
pip install yfinance fbprophet matplotlib
```

## Usage

1. Clone the repository or copy the Python script.
2. Run the script in your terminal or IDE.
3. Enter a stock symbol when prompted (e.g., `AAPL`, `MSFT`, `GOOGL`).
4. The script will display the stock's exchange, country, and a forecast for the next 30 days.

```bash
Enter stock symbol (e.g., AAPL, MSFT): AAPL
Stock Symbol: AAPL
Exchange: NASDAQ
Country: United States
```

A plot showing the historical data and forecasted prices will be generated.

## Example Output:

```
Enter stock symbol (e.g., AAPL, MSFT): AAPL
Stock Symbol: AAPL
Exchange: NASDAQ
Country: United States
Forecasted prices for AAPL in the next 30 days:
          ds        yhat  yhat_lower  yhat_upper
1749 2025-04-20  192.783561   179.465870   206.106862
1750 2025-04-21  193.678485   180.601199   207.512332
1751 2025-04-22  194.392226   181.121459   208.447050
1752 2025-04-23  195.180212   181.662344   209.117907
1753 2025-04-24  195.899612   182.218419   210.314902
```

## Credits:
- **yfinance**: For fetching historical stock data.
- **Prophet**: For time series forecasting.
- **matplotlib**: For plotting the forecast.

## License:
This project is licensed under the MIT License.
