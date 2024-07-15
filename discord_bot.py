import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.rpc.async_api import AsyncClient
from solana.transaction import Transaction
from solana.system_program import transfer, TransferParams
from utils import (
    fetch_pump_fun_data, analyze_pump_fun_data, fetch_dexscreener_data,
    analyze_market_data, generate_signals, execute_signals, handle_user_query
)

# Load environment variables
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
API_URL = os.getenv("API_URL")

# Set up Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command(name='ask', help='Ask the bot a question')
async def ask(ctx, *, query: str):
    response = handle_user_query(query)
    await ctx.send(response)

@bot.command(name='trade', help='Execute trading signals')
async def trade(ctx):
    pump_fun_data = fetch_pump_fun_data()
    signals_from_pump_fun = analyze_pump_fun_data(pump_fun_data)
    
    dexscreener_data = fetch_dexscreener_data()
    signals_from_dexscreener = analyze_market_data(dexscreener_data)
    
    signals = generate_signals(signals_from_dexscreener, signals_from_pump_fun)
    await execute_signals(signals, PRIVATE_KEY)
    
    await ctx.send("Trading signals executed.")

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
