import os
import logging
from dotenv import load_dotenv
from binance.enums import *
from tbot.core import TBot, FUTURE_ORDER_TYPE_STOP_MARKET
from ui.cli import get_user_input

# Load env vars
load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Logging
logging.basicConfig(
    filename='tbot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    """Main entrypoint for the bot."""
    bot = TBot(API_KEY, API_SECRET)
    symbol, side, order_type, quantity, price, stop_price = get_user_input()

    if side not in [SIDE_BUY, SIDE_SELL]:
        print("Invalid side. Must be one of: BUY, SELL")
        return
    if order_type not in [ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT, FUTURE_ORDER_TYPE_STOP_MARKET]:
        print("Invalid order type, Must be one of: MARKET, LIMIT, STOP_MARKET")
        return

    try:
        result = bot.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price
        )
        print(f"Order placed successfully: {result}")
    except Exception as e:
        print(f"Failed to place order: {str(e)}")

if __name__ == "__main__":
    main()
