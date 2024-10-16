from data_fetcher import fetch_stock_data
from predictor import prepare_data, train_model, predict_price

def main():
    symbol = "AAPL"  # Example: Apple Inc.
    data = fetch_stock_data(symbol)
    df = prepare_data(data)
    model, X_test, y_test = train_model(df)
    
    # Make a prediction for the next day
    last_data = df.iloc[-1][["Open", "High", "Low", "Close", "Volume"]].values.reshape(1, -1)
    prediction = predict_price(model, last_data)
    
    print(f"Predicted price for {symbol}: ${prediction[0]:.2f}")

if __name__ == "__main__":
    main()
