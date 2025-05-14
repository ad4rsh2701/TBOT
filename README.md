
# TBot - Binance Future Testnet Trading Bot

A simplified crypto trading bot built in Python for Binance Futures Testnet.

## Features
- Place **Market**, **Limit** and **Stop-Market** orders.
- Support for both **BUY** and **SELL** positions.
- Simple **Command Line** and **Web Interface**.
- Logging of all API calls and errors to `tbot.log`, generated automatically.
- Clean, modular and packageable codebase.

## Project Structure
    ├── main.py # CLI entry point
    ├── setup.py # Package setup
    ├── .env # Your API keys (not included in repo)
    ├── tbot/
    │ ├── __init__.py
    │ └── core.py # Bot logic
    ├── ui/
    │ ├── __init__.py
    │ ├── cli.py # CLI interface
    │ └── webapp.py # Streamlit GUI
    └── bot.log # Logs of placed orders and errors


## Setup

### 0. Create a `venv` (recommended)
```bash
py venv venv
venv/Scripts/Activate
```

### 1. Clone and Install
```bash
git clone https://github.com/ad4rsh2701/tbot.git
cd tbot
pip install -e .
```

### 2. Add your Binance Testnet API keys
Create a `.env` file in the root:
```bash
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

## Usage
### 🖥 CLI
```bash
python main.py
```
You will be prompted to enter:
- Symbol (e.g. BTCUSDT)
- Side (BUY/SELL)
- Order type (MARKET/LIMIT/STOP_MARKET)
- Quantity
- Price or Stop Price (based on order type of course)

### 🌐 Web Interface (Streamlit)
```bash
streamlit run ui/webapp.py
```
A clean form to place trades and receieve real time-feedback will be displayed in your browser.


## Note
Minimum notional value per trade must be at least 100 USDT.

## Author
Adarsh Aryan | adarsharyan2701@gmail.com