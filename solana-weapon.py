import asyncio
from dotenv import load_dotenv
from utils import (
    fetch_dexscreener_data,
    analyze_market_data,
    generate_signals,
    execute_signals
)

# Load environment variables from .env file
load_dotenv()

async def main():
    try:
        # Fetch and analyze market data
        market_tokens = fetch_dexscreener_data(query="solana")
        print("Market Tokens:", market_tokens)  # Debugging print statement
        market_signals = analyze_market_data(market_tokens)
        print("Market Signals:", market_signals)  # Debugging print statement
        
        # Generate final signals
        final_signals = generate_signals(market_signals)
        print("Final Trading Signals:", final_signals)
        
        # Execute signals on the Solana network
        execute_signals(final_signals)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
