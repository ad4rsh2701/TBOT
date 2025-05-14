def get_user_input():
    """
    Get user input for the parameters of an order.

    Returns:
        (symbol, side, order_type, quantity, price, stop_price)
    """
    
    print("Welcome to the TBot CLI!")
    print("Please enter the following details:")
    
    symbol = input("Enter symbol: ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    order_type = input("Enter order type (MARKET/LIMIT/STOP_MARKET): ").upper()
    quantity = float(input("Enter quantity: "))
    
    price = None
    stop_price = None

    if order_type == "LIMIT":
        price = float(input("Enter price: "))
    elif order_type == "STOP_MARKET":
        stop_price = float(input("Enter stop price: "))
    
    return symbol, side, order_type, quantity, price, stop_price