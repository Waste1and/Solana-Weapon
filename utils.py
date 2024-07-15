import requests
from bs4 import BeautifulSoup
from solana.rpc.async_api import AsyncClient
from solana.transaction import Transaction
from solana.keypair import Keypair
from gpt4free import providers, ChatGPT

API_URL = "https://api.mainnet-beta.solana.com"

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

def generate_signals(analyzed_data, signals_from_pump_fun):
    signals = {}
    for symbol, action in analyzed_data.items():
        if action == 'BUY':
            signals[symbol] = {'action': 'BUY', 'confidence': 0.9}
        elif action == 'SELL':
            signals[symbol] = {'action': 'SELL', 'confidence': 0.9}
        else:
            signals[symbol] = {'action': 'HOLD', 'confidence': 0.5}
    
    for symbol, action in signals_from_pump_fun.items():
        if symbol in signals:
            signals[symbol]['action'] = action
        else:
            signals[symbol] = {'action': action, 'confidence': 0.7}
    return signals

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

def generate_text_response(prompt):
    response = ChatGPT.Completion.create(
        providers.Bard,  # or any other free provider supported by gpt4free
        prompt=prompt,
        max_tokens=150
    )
    return response['text'].strip()

def handle_user_query(query):
    if "trending" in query.lower():
        tokens = fetch_dexscreener_data()
        trending_tokens = sorted(tokens, key=lambda x: float(x['volume'].replace(',', '')), reverse=True)[:5]
        response = f"The top trending tokens are: {[token['name'] for token in trending_tokens]}"
    elif "entry point" in query.lower():
        tokens = fetch_dexscreener_data()
        signals = analyze_market_data(tokens)
        buy_signals = [symbol for symbol, signal in signals.items() if signal == 'BUY']
        response = f"Suggested entry points: {buy_signals}"
    else:
        response = generate_text_response(query)
    
    return response
