from core.logger import logger
from core.config import show_banner
from data.market_data import MarketData
from indicators.ema import EMA
from charts.chart import plot_price
from indicators.rsi import RSI
from strategies.ema_rsi_strategy import EmaRsiStrategy

show_banner()

logger.info("Loading market data...")

market = MarketData()

df = market.load_history()

# Розрахунок EMA, RSI
df = EMA.calculate(df, 20)
df = EMA.calculate(df, 50)

# Розрахунок RSI
df = RSI.calculate(df)

# Розрахунок EMA, RSI
df = RSI.calculate(df)

df = EmaRsiStrategy.generate_signals(df)

print()
print(
    df[
        [
            "Close",
            "EMA20",
            "EMA50",
            "RSI",
            "Signal"
        ]
    ].tail(20)
)

logger.info("EMA calculated successfully.")
plot_price(df)