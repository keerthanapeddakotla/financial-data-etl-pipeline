import sqlite3

def load_data(df):

    conn = sqlite3.connect("financial_data.db")

    df.to_sql(
        "stock_returns",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Data successfully loaded into database")