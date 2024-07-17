# Warning
The project is currently being created. Want to contribute? Contact https://warpcast.com/itachiseyez

# Solana Weapon

**Solana Weapon** is advanced for the Solana blockchain. It analyzes market data and community sentiment to generate trading signals for Solana tokens.

Be sure to, 

python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate` 

pip install -r requirements.txt

# Solana Wallet

Create a .env file in the root directory of the project to store environment variables such as PRIVATE_KEY. This is essential for the execution of trading signals.

PRIVATE_KEY=your_solana_private_key

#Train Model 

Train the model using the train_model.py script. This script generates synthetic data and trains a RandomForestClassifier model.

python train_model.py

#Execute 

Execute the solana-weapon.py script to fetch, analyze, and act on market data.

python solana-weapon.py

