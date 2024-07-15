# utils.py

import requests
from bs4 import BeautifulSoup
from solana.rpc.async_api import AsyncClient

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

def fetch_market_data():
    crypto_data = requests.get("https://crypto.com/price/categories/Solana-ecosystem").json()
    step_finance_data = requests.get("https://analytics.step.finance/defionsolana").json()
    return {
        "crypto_data": crypto_data,
        "step_finance_data": step_finance_data
    }

def analyze_market_data(data):
    signals = {}
    for coin in data['crypto_data']['coins']:
        volume = coin['volume_24h']
        price_change = coin['price_change_percentage_24h']
        
        if volume > 1000000 and price_change > 5:
            signals[coin['symbol']] = 'BUY'
        elif volume < 500000 and price_change < -5:
            signals[coin['symbol']] = 'SELL'
        else:
            signals[coin['symbol']] = 'HOLD'
    return signals

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
