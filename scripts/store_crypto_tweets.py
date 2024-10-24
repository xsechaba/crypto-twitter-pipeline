import pandas as pd
from sqlalchemy import create_engine

def store_in_database():
    # Create a connection to the PostgreSQL database
    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres/airflow')

    # Read the cleaned data
    df = pd.read_csv('cleaned_crypto_tweets.csv')
    
    # Store the data in a PostgreSQL table
    df.to_sql('crypto_tweets', engine, if_exists='replace', index=False)
    print("Data stored in the PostgreSQL database")

if __name__ == "__main__":
    store_in_database()
