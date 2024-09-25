from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from sales_etl import run_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'sales_data_etl',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval='*/5 * * * *',
)

run_etl = PythonOperator(
    task_id='sales_etl_complated',
    python_callable=run_etl,
    dag=dag, 
)

run_etl
