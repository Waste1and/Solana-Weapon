# src/indicators.py
def calculate_rsi(prices, period=14):
    gains, losses = [], []
    for i in range(1, len(prices)):
        change = prices[i] - prices[i - 1]
        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))
    
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    
    rsi = [100 - (100 / (1 + (avg_gain / avg_loss)))]
    for i in range(period, len(prices)):
        gain, loss = gains[i], losses[i]
        avg_gain = (avg_gain * (period - 1) + gain) / period
        avg_loss = (avg_loss * (period - 1) + loss) / period
        rs = avg_gain / avg_loss
        rsi.append(100 - (100 / (1 + rs)))
    return [None] * (period - 1) + rsi

def calculate_atr(high, low, close, period=14):
    tr = [max(high[i] - low[i], abs(high[i] - close[i - 1]), abs(low[i] - close[i - 1])) for i in range(1, len(close))]
    atr = [sum(tr[:period]) / period]
    for i in range(period, len(tr)):
        atr.append((atr[-1] * (period - 1) + tr[i]) / period)
    return [None] * period + atr

def calculate_obv(close, volume):
    obv = [0]
    for i in range(1, len(close)):
        if close[i] > close[i - 1]:
            obv.append(obv[-1] + volume[i])
        elif close[i] < close[i - 1]:
            obv.append(obv[-1] - volume[i])
        else:
            obv.append(obv[-1])
    return obv

def calculate_macd(prices, short_period=12, long_period=26, signal_period=9):
    short_ema = calculate_ema(prices, short_period)
    long_ema = calculate_ema(prices, long_period)
    macd_line = [s - l for s, l in zip(short_ema, long_ema)]
    signal_line = calculate_ema(macd_line, signal_period)
    macd_histogram = [m - s for m, s in zip(macd_line, signal_line)]
    return macd_line, signal_line, macd_histogram

def calculate_ema(prices, period):
    ema = []
    multiplier = 2 / (period + 1)
    ema.append(sum(prices[:period]) / period)
    for price in prices[period:]:
        ema.append((price - ema[-1]) * multiplier + ema[-1])
    return [None] * (period - 1) + ema

def calculate_bollinger_bands(prices, period=20, num_std_dev=2):
    sma = calculate_sma(prices, period)
    std_dev = [sum([(p - sma[i]) ** 2 for p in prices[i-period+1:i+1]]) / period for i in range(period-1, len(prices))]
    std_dev = [s ** 0.5 for s in std_dev]
    upper_band = [sma[i] + num_std_dev * std_dev[i] for i in range(len(sma))]
    lower_band = [sma[i] - num_std_dev * std_dev[i] for i in range(len(sma))]
    return sma, upper_band, lower_band

def calculate_sma(prices, period):
    sma = [sum(prices[i-period+1:i+1]) / period for i in range(period-1, len(prices))]
    return [None] * (period - 1) + sma
