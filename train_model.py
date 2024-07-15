import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Generate synthetic data for demonstration
np.random.seed(42)
volume = np.random.randint(500000, 2000000, 1000)
price_change = np.random.uniform(-10, 10, 1000)
profitable = (volume > 1000000) & (price_change > 5)
data = pd.DataFrame({
    'volume': volume,
    'price_change': price_change,
    'profitable': profitable.astype(int)
})

# Features and target
X = data[['volume', 'price_change']]
y = data['profitable']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy}")

# Save the model
joblib.dump(model, 'trade_model.pkl')
