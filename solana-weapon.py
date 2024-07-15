# solana_weapon.py

import asyncio
from config import PRIVATE_KEY, API_URL
from utils import fetch_pump_fun_data, analyze_pump_fun_data, fetch_dexscreener_data, analyze_market_data, generate_signals, execute_signals

async def main():
    pump_fun_data = fetch_pump_fun_data()
    signals_from_pump_fun = analyze_pump_fun_data(pump_fun_data)
    
    dexscreener_data = fetch_dexscreener_data()
    signals_from_dexscreener = analyze_market_data(dexscreener_data)
    
    signals = generate_signals(signals_from_dexscreener, signals_from_pump_fun)
    await execute_signals(signals, PRIVATE_KEY)

if __name__ == "__main__":
    asyncio.run(main())
