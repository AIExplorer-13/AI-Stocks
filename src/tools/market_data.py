import yfinance as yf

def get_stock_data(ticker):

    stock = yf.Ticker(ticker)

    info = stock.info

    return {
        "name": info.get("longName"),
        "current_price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "sector": info.get("sector")
    }


if __name__ == "__main__":

    data = get_stock_data("RELIANCE.NS")

    print(data)