# Solana Weapon

**Solana Weapon** is an advanced trading bot for the Solana blockchain ecosystem. It analyzes market data and community sentiment to generate trading signals for Solana tokens.

## Features

- **Data Collection**: Fetches data from Pump.Fun, Crypto.com, and Step Finance.
- **Market Analysis**: Analyzes token trends and community sentiment.
- **Signal Generation**: Provides trading signals based on market conditions.
- **Trading Execution**: Places buy and sell orders on Solana-based platforms.

## Getting Started 1.0

### Prerequisites
- Python 3.7 or higher
- Solana private key
- API access to relevant platforms

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Waste1and/Solana-Weapon.git
   cd Solana-Weapon

Automated Installation Script:

Create a file named install_and_run.sh with the following content:#!/bin/bash

# Update and install required packages
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt update
    sudo apt install -y git python3 python3-pip
elif [[ "$OSTYPE" == "darwin"* ]]; then
    brew update
    brew install git python3
elif [[ "$OSTYPE" == "msys" ]]; then
    echo "Please install Git and Python3 manually."
    exit 1
else
    echo "Unsupported OS"
    exit 1
fi

# Clone the repository
git clone https://github.com/Waste1and/Solana-Weapon.git
cd Solana-Weapon

# Create and populate the .env file with provided credentials
cat <<EOF > .env
DISCORD_TOKEN=$1
PRIVATE_KEY=$2
API_URL=https://api.mainnet-beta.solana.com
EOF

# Install Python dependencies
pip3 install -r requirements.txt

# Run the bot
python3 discord_bot.py

***Make the script executable and run it with your credentials as arguments***

chmod +x install_and_run.sh
./install_and_run.sh your-discord-bot-token your-private-key

Or

Linux Installation Commands: 

sudo apt update
sudo apt install -y git python3 python3-pip

git clone https://github.com/Waste1and/Solana-Weapon.git
cd Solana-Weapon

***Create a .env File: Create a .env file in the root directory with your credentials***

DISCORD_TOKEN=your-discord-bot-token
PRIVATE_KEY=your-private-key
API_URL=https://api.mainnet-beta.solana.com

***Configure discord-bot-token and your-private-key with your credentials***

pip3 install -r requirements.txt

***RUN THE BOT***

python3 discord_bot.py


USAGE: 

Ask the Bot:

In your Discord server, type !ask <your question> to ask the bot a question.

Example: !ask what's trending?

Execute Trades: 

Type !trade to fetch the latest data, generate signals, and execute trades.

Example: !trade
