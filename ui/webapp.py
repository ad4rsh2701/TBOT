import os
import streamlit as st
from dotenv import load_dotenv
from tbot.core import TBot, FUTURE_ORDER_TYPE_STOP_MARKET
from binance.enums import *


load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

bot = TBot(API_KEY, API_SECRET)

st.title("🪙 Binance Futures Trading Bot")

symbols = bot.get_symbols()

with st.form("order_form"):
    symbol = st.selectbox("Trading Pair", symbols)
    side = st.selectbox("Side", [SIDE_BUY, SIDE_SELL])
    order_type = st.selectbox("Order Type", [ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT, FUTURE_ORDER_TYPE_STOP_MARKET])
    quantity = st.number_input("Quantity", min_value=0.001, step=0.001)
    price = None
    stop_price = None
    if order_type == ORDER_TYPE_LIMIT:
        price = st.number_input("Price", min_value=0.0, step=0.1)
    elif order_type == FUTURE_ORDER_TYPE_STOP_MARKET:
        stop_price = st.number_input("Stop Price", min_value=0.0, step=0.1)

    submitted = st.form_submit_button("Place Order")

if submitted:
    try:
        result = bot.place_order(symbol, side, order_type, quantity, price, stop_price)
        st.success("Order placed successfully!")
        st.json(result)
    except Exception as e:
        st.error(f"Failed to place order: {str(e)}")