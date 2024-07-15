# solana-weapon.py
import asyncio
from solana.publickey import PublicKey
from config import SOLANA_PRIVATE_KEY
from utils import fetch_pump_fun_data, analyze_pump_fun_data, fetch_dexscreener_data, analyze_market_data, generate_signals, execute_signals, handle_user_query

async def main():
    # Fetch and analyze data from Pump.Fun
    pump_fun_tokens = fetch_pump_fun_data()
    pump_fun_signals = analyze_pump_fun_data(pump_fun_tokens)
    
    # Fetch and analyze market data
    market_tokens = fetch_dexscreener_data()
    market_signals = analyze_market_data(market_tokens)
    
    # Generate final signals
    final_signals = generate_signals(market_signals, pump_fun_signals)
    print("Final Trading Signals:", final_signals)
    
    # Execute signals on the Solana network
    await execute_signals(final_signals, SOLANA_PRIVATE_KEY)

if __name__ == "__main__":
    asyncio.run(main())
