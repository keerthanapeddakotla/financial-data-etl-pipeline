def check_missing_values(df):
    missing = df.isnull().sum()
    print("Missing values:")
    print(missing)

def check_duplicates(df):
    duplicates = df.duplicated().sum()
    print("Duplicate rows:", duplicates)