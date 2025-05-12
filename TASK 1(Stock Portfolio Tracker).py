import yfinance as yf

# Store the user's portfolio
portfolio = {}

# Add stock to the portfolio
def add_stock():
    symbol = input("Enter the stock symbol you'd like to add (e.g., AAPL, TSLA): ").upper()
    try:
        shares = int(input(f"How many shares of {symbol} do you own? "))
        if shares <= 0:
            print("Please enter a positive number of shares.")
            return
    except ValueError:
        print("That doesn't look like a valid number. Please try again.")
        return

    if symbol in portfolio:
        portfolio[symbol] += shares
        print(f"Updated! You now have {portfolio[symbol]} shares of {symbol}.")
    else:
        portfolio[symbol] = shares
        print(f"{shares} shares of {symbol} added to your portfolio.")

# Remove stock or decrease shares
def remove_stock():
    symbol = input("Enter the stock symbol you'd like to remove (or reduce): ").upper()
    
    if symbol not in portfolio:
        print(f"You don’t currently have any {symbol} in your portfolio.")
        return

    try:
        shares = int(input(f"How many shares of {symbol} would you like to remove? "))
        if shares <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    if shares >= portfolio[symbol]:
        del portfolio[symbol]
        print(f"All shares of {symbol} have been removed from your portfolio.")
    else:
        portfolio[symbol] -= shares
        print(f"Removed {shares} shares of {symbol}. You now have {portfolio[symbol]} left.")

# View the current portfolio with live prices
def view_portfolio():
    if not portfolio:
        print("Your portfolio is currently empty. Add some stocks to get started!")
        return

    print("\n📊 Here's your current portfolio:\n")
    total_value = 0

    for symbol, shares in portfolio.items():
        try:
            stock = yf.Ticker(symbol)
            price = stock.history(period="1d")['Close'][0]
            value = price * shares
            total_value += value
            print(f"→ {symbol}: {shares} shares @ ${price:.2f} each = ${value:.2f}")
        except Exception as e:
            print(f"⚠️ Couldn’t retrieve data for {symbol}: {e}")

    print(f"\n💰 Total Portfolio Value: ${total_value:.2f}\n")

# Simple user menu
def menu():
    print("👋 Welcome to your Personal Stock Portfolio Tracker!")

    while True:
        print("\nWhat would you like to do?")
        print("1️⃣  Add a stock")
        print("2️⃣  Remove a stock")
        print("3️⃣  View my portfolio")
        print("4️⃣  Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_stock()
        elif choice == '2':
            remove_stock()
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            print("👋 Thanks for using the portfolio tracker. See you next time!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

# Start the program
menu()
