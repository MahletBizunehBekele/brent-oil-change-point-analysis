import matplotlib.pyplot as plt


def plot_prices(df):

    plt.figure(figsize=(14,6))

    plt.plot(df["Date"], df["Price"])

    plt.title("Brent Oil Prices")

    plt.xlabel("Date")

    plt.ylabel("USD per Barrel")

    plt.grid(True)

    plt.show()


def plot_returns(df):

    plt.figure(figsize=(14,5))

    plt.plot(df["Date"], df["Log_Return"])

    plt.title("Daily Log Returns")

    plt.grid(True)

    plt.show()