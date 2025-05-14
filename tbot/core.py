import logging
from binance.client import Client
from binance.enums import *


# apparently, the enums of binanace doesn't export a constant for STOP_MARKET
# so, here we are, creating our own constant
# this constant is the actual string expected by the API under the key "type"
FUTURE_ORDER_TYPE_STOP_MARKET = "STOP_MARKET"

class TBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logging.info("Bot initialized with testnet=%s", testnet)

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            order_params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity
            }
            if order_type == ORDER_TYPE_LIMIT:
                order_params['price'] = price
                order_params['timeInForce'] = TIME_IN_FORCE_GTC
            elif order_type == FUTURE_ORDER_TYPE_STOP_MARKET:
                order_params['stopPrice'] = stop_price
                order_params['timeInForce'] = TIME_IN_FORCE_GTC

            order = self.client.futures_create_order(**order_params)
            logging.info("Order placed: %s", order)
            return order
        except Exception as e:
            logging.error("Error placing order: %s", str(e))
            raise e