def transform_data(df):

    df.ffill(inplace=True)

    returns = df.set_index("Date").pct_change(fill_method=None)

    # volatility calculation
    volatility = returns.std()

    print("\nStock Volatility:")
    print(volatility)

    returns.reset_index(inplace=True)

    return returns