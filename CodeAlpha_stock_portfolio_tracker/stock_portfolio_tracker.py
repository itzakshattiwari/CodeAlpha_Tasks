import os

def track_portfolio():
    stock_prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "GOOGL": 140.0,
        "AMZN": 130.0,
        "MSFT": 330.0
    }
    
    user_portfolio = {}
    
    print("Welcome to the Simple Stock Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("(Type 'done' to finish)\n")
    
    while True:
        symbol = input("Enter stock symbol: ").upper().strip()
        
        if symbol == 'DONE':
            break
            
        if symbol not in stock_prices:
            print("Stock not found. Please choose from available stocks.")
            continue
            
        try:
            quantity = float(input(f"Enter quantity of {symbol} shares: "))
            if quantity < 0:
                print("Quantity cannot be negative. Try again.")
                continue
                
            user_portfolio[symbol] = user_portfolio.get(symbol, 0) + quantity
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("\n" + "="*30)
    print("PORTFOLIO SUMMARY")
    print("="*30)
    
    total_investment = 0.0
    summary_lines = []
    
    if not user_portfolio:
        print("Your portfolio is empty.")
    else:
        for sym, qty in user_portfolio.items():
            price = stock_prices[sym]
            value = price * qty
            total_investment += value
            
            line = f"{sym}: {qty} shares @ ${price:.2f} = ${value:.2f}"
            print(line)
            summary_lines.append(line)
            
        total_line = f"\nTOTAL INVESTMENT VALUE: ${total_investment:.2f}"
        print(total_line)
        summary_lines.append(total_line)

        save_option = input("\nSave summary to text file? (y/n): ").lower().strip()
        if save_option == 'y':
            file_name = "portfolio_summary.txt"
            try:
                with open(file_name, "w") as file:
                    file.write("PORTFOLIO SUMMARY\n")
                    file.write("=================\n")
                    file.write("\n".join(summary_lines))
                print(f"Summary saved to {os.path.abspath(file_name)}")
            except IOError as e:
                print(f"Error saving file: {e}")

if __name__ == "__main__":
    track_portfolio()