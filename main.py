import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date, timedelta
import streamlit as st

# Set the date range for the stock data
today = date.today()
start_date = (today - timedelta(days=360)).strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Streamlit UI
st.title("Real-Time Stock Price Data")
company_name = st.text_input("Enter Stock Ticker Symbol (e.g., AAPL, MSFT) >>:")

if company_name:
    try:
        # Fetch the stock data
        data = yf.download(company_name, start=start_date, end=end_date)

        if data.empty:
            st.error("No data found for the specified ticker symbol.")
        else:
            # Plotting the stock data
            fig, ax = plt.subplots()
            ax = data["Close"].plot(figsize=(12, 8), title=f"{company_name} Stock Prices", fontsize=20, label="Close Price")
            plt.legend()
            plt.grid()

            # Display the plot in Streamlit
            st.pyplot(fig)
    except Exception as e:
        st.error(f"An error occurred: {e}")
