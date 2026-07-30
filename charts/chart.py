import matplotlib.pyplot as plt


def plot_price(df):

    plt.figure(figsize=(16, 8))

    plt.plot(df.index, df["Close"], label="BTC Price")
    plt.plot(df.index, df["EMA20"], label="EMA20")
    plt.plot(df.index, df["EMA50"], label="EMA50")

    plt.title("BTC/USD")

    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.show()