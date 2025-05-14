import logging
from binance.client import Client
from binance.enums import *

class TBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logging.info("Bot initialized with testnet=%s", testnet)

    def place_order(self, symbol, side, order_type, quantity, price=None):
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

            order = self.client.futures_create_order(**order_params)
            logging.info("Order placed: %s", order)
            return order
        except Exception as e:
            logging.error("Error placing order: %s", str(e))
            raise e