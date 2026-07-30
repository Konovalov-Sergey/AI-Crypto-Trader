from core.logger import logger
from core.config import show_banner
from data.market_data import MarketData
from indicators.ema import ema
from charts.chart import plot_price

show_banner()

logger.info("Loading market data...")

market = MarketData()

df = market.load_history()

# Розрахунок EMA
df["EMA20"] = ema(df["Close"], 20)
df["EMA50"] = ema(df["Close"], 50)

print()
print(df[["Close", "EMA20", "EMA50"]].tail())

logger.info("EMA calculated successfully.")
plot_price(df)