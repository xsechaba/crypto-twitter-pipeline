from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 23),
    'retries': 1,
}

# DAG definition
with DAG(
    dag_id='crypto_twitter_dag',
    default_args=default_args,
    description='Crypto Twitter Data Pipeline with Multiple Stages',
    schedule_interval='@daily',  # Runs daily
    catchup=False,
) as dag:

    # Task 1: Extract data
    def extract_data():
        os.system("python scripts/extract_crypto_tweets.py")
    
    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )

    # Task 2: Clean data
    def clean_data():
        os.system("python scripts/clean_crypto_tweets.py")
    
    clean_task = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data
    )

    # Task 3: Store data in database
    def store_data():
        os.system("python scripts/store_crypto_tweets.py")
    
    store_task = PythonOperator(
        task_id='store_data',
        python_callable=store_data
    )

    # Task 4: Analyze data
    def analyze_data():
        os.system("python scripts/analyze_crypto_tweets.py")
    
    analyze_task = PythonOperator(
        task_id='analyze_data',
        python_callable=analyze_data
    )

    # Define the task dependencies
    extract_task >> clean_task >> store_task >> analyze_task
