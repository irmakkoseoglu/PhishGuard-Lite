import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df = df.drop(columns=['isip'], errors='ignore')
    df['is@'] = df['is@'].fillna(df['is@'].median())
    df['isredirect'] = df['isredirect'].fillna(df['isredirect'].median())
    df['haveDash'] = df['haveDash'].fillna(df['haveDash'].median())
    df['domainLen'] = df['domainLen'].fillna(df['domainLen'].median())
    return df
