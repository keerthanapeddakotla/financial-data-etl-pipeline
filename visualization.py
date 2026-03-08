import matplotlib.pyplot as plt

def plot_returns(df):

    df = df.copy()
    df.set_index("Date", inplace=True)

    df.plot(figsize=(10,5))

    plt.title("Stock Daily Returns")
    plt.xlabel("Date")
    plt.ylabel("Returns")

    plt.savefig("stock_returns_plot.png")