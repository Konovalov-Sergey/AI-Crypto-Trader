from core.logger import logger
from core.config import show_banner
from data.market_data import MarketData
from indicators.ema import EMA
from charts.chart import plot_price
from indicators.rsi import RSI

show_banner()

logger.info("Loading market data...")

market = MarketData()

df = market.load_history()

# Розрахунок EMA, RSI
df = EMA.calculate(df, 20)
df = EMA.calculate(df, 50)

df = RSI.calculate(df)

print()
print(df[["Close", "EMA20", "EMA50", "RSI"]].tail())

logger.info("EMA calculated successfully.")
plot_price(df)