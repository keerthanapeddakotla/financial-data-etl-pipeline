import pandas as pd

def detect_anomalies(df):

    print("\nChecking for anomalies in stock returns...")

    # calculate z-score
    z_scores = (df.iloc[:,1:] - df.iloc[:,1:].mean()) / df.iloc[:,1:].std()

    anomalies = (z_scores.abs() > 3)

    print("Anomalies detected:")
    print(anomalies.sum())