# utils.py

import requests
from bs4 import BeautifulSoup
from solana.rpc.async_api import AsyncClient
from solana.transaction import Transaction
from solana.account import Account

API_URL = "https://api.mainnet-beta.solana.com"

# Function to fetch data from Pump.Fun
def fetch_pump_fun_data():
    url = "https://pump.fun/board"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tokens = []
    for item in soup.select('.token-card'):
        name = item.select_one('.token-name').text.strip()
        symbol = item.select_one('.token-symbol').text.strip()
        price = item.select_one('.token-price').text.strip()
        volume = item.select_one('.token-volume').text.strip()
        link = item.select_one('.token-link')['href'].strip()
        
        tokens.append({
            'name': name,
            'symbol': symbol,
            'price': price,
            'volume': volume,
            'link': link
        })
    return tokens

# Function to analyze data from Pump.Fun
def analyze_pump_fun_data(tokens):
    signals = {}
    for token in tokens:
        volume = float(token['volume'].replace(',', ''))
        price_change = float(token['price'].replace('$', '').replace(',', ''))

        if volume > 1000000 and price_change > 5:
            signals[token['symbol']] = 'BUY'
        elif volume < 500000 and price_change < -5:
            signals[token['symbol']] = 'SELL'
        else:
            signals[token['symbol']] = 'HOLD'
    return signals

# Function to fetch market data from DexScreener
def fetch_dexscreener_data():
    url = "https://api.dexscreener.com/latest/dex/tokens/solana"
    response = requests.get(url)
    data = response.json()
    tokens = data.get('tokens', [])
    
    formatted_tokens = []
    for token in tokens:
        formatted_tokens.append({
            'name': token.get('name'),
            'symbol': token.get('symbol'),
            'price': token.get('priceUsd'),
            'volume': token.get('volume24h'),
            'link': token.get('url')
        })
    return formatted_tokens

# Function to analyze market data from DexScreener
def analyze_market_data(tokens):
    signals = {}
    for token in tokens:
        volume = float(token['volume'].replace(',', ''))
        price_change = float(token['price'].replace('$', '').replace(',', ''))

        if volume > 1000000 and price_change > 5:
            signals[token['symbol']] = 'BUY'
        elif volume < 500000 and price_change < -5:
            signals[token['symbol']] = 'SELL'
        else:
            signals[token['symbol']] = 'HOLD'
    return signals

# Function to generate trading signals by combining analyzed data
def generate_signals(analyzed_data, signals_from_pump_fun):
    signals = {}
    for symbol, action in analyzed_data.items():
        if action == 'BUY':
            signals[symbol] = {'action': 'BUY', 'confidence': 0.9}
        elif action == 'SELL':
            signals[symbol] = {'action': 'SELL', 'confidence': 0.9}
        else:
            signals[symbol] = {'action': 'HOLD', 'confidence': 0.5'}
    
    for symbol, action in signals_from_pump_fun.items():
        if symbol in signals:
            signals[symbol]['action'] = action
        else:
            signals[symbol] = {'action': action, 'confidence': 0.7}
    return signals

# Function to execute trading signals
async def execute_signals(signals, private_key):
    async with AsyncClient(API_URL) as client:
        for symbol, signal in signals.items():
            if signal['action'] == 'BUY':
                # Implement buy logic here
                print(f"Placing BUY order for {symbol}")
                pass
            elif signal['action'] == 'SELL':
                # Implement sell logic here
                print(f"Placing SELL order for {symbol}")
                pass
            else:
                print(f"Holding {symbol}")
