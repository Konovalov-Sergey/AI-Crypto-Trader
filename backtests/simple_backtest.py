import pandas as pd


class SimpleBacktest:

    @staticmethod
    def run(df: pd.DataFrame):

        position = None
        entry_price = None

        profit = 0

        trades = 0
        wins = 0
        losses = 0

        print("===================================")
        print("Simple Backtest")
        print("===================================")

        print(f"Rows: {len(df)}")
        print(f"Trades: {trades}")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Profit: {profit}")

        return {
            "trades": trades,
            "wins": wins,
            "losses": losses,
            "profit": profit,
        }