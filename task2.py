# Mock stock prices (as if fetched from an API)
mock_prices = {
    "AAPL": 175.34,
    "MSFT": 320.21,
    "TSLA": 250.45
}

# Your stock portfolio (symbol: number of shares)
portfolio = {
    "AAPL": 10,
    "MSFT": 5,
    "TSLA": 3
}

# Track and display portfolio value
total_value = 0
print("Stock Portfolio Summary:\n")

for symbol, shares in portfolio.items():
    price = mock_prices.get(symbol, 0)
    value = price * shares
    total_value += value
    print(f"{symbol}: {shares} shares x ${price:.2f} = ${value:.2f}")

print(f"\nTotal Portfolio Value: ${total_value:.2f}")