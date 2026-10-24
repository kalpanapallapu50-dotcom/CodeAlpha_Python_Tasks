# CodeAlpha - Task 2: Stock Portfolio Tracker
# Created by: Kalpana

# Step 1: Stock prices dictionary (hardcoded)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 380,
    "AMZN": 150
}

# Step 2: Portfolio - user input
portfolio = {}
total_value = 0

print("=== Stock Portfolio Tracker ===")
print("Available Stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' to finish\n")

# Step 3: Take user input
while True:
    stock = input("Enter Stock Symbol (e.g., AAPL) or 'done': ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("Stock not found! Available:", list(stock_prices.keys()))
        continue
    
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print(f"Added {quantity} of {stock}\n")
    except:
        print("Please enter a valid number!")

# Step 4: Calculate total investment
print("\n--- Your Portfolio ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares x ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Step 5: Optional - Save to file
save = input("\nDo you want to save this to file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} x ${stock_prices[stock]} = ${stock_prices[stock]*qty}\n")
        f.write(f"\nTotal Value: ${total_value}\n")
    print("Saved to portfolio.txt in same folder!")

print("\nTask 2 Completed Successfully!")