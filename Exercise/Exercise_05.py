def analyze_portfolio(portfolio):
    total_shares = 0
    total_value = 0
    avg_price = 0
    holdings = {}
    
    for x in portfolio:
        total_shares += x["shares"]
        total_value += x["shares"] * x["price"]
 
    for i in portfolio:
        percentage = (i["shares"] * i["price"])*100/total_value
        holdings[i["symbol"]] = {"num_shares" : i["shares"], 
                                 "total_value" : i["shares"] * i["price"],
                                 "percentage_of_portfolio" : round(percentage, 2)}
 
    avg_price = total_value / total_shares
 
    return {"total_shares" : total_shares, 
            "total_value" : total_value, 
            "average_price_per_share" : round(avg_price, 2),
            "holdings_breakdown" : holdings}
 
portfolio = [
{"symbol": "AAPL", "shares": 100, "price": 150.00},
{"symbol": "GOOG", "shares": 50, "price": 2000.00},
{"symbol": "TSLA", "shares": 25, "price": 700.00},
]
 
print(analyze_portfolio(portfolio))