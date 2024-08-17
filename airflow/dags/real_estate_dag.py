from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
import requests
from scrape.novel_scraper import scrape_novel
from clean.novel_cleaner import clean_novel
from sql.novel_pusher import push_novel
from scrape.square_scraper import scrape_square
from clean.square_cleaner import clean_square
from sql.square_pusher import push_square

dag = DAG(
    'real_estate_pipeline',
    default_args={'start_date': days_ago(1)},
    schedule_interval='0 23 * * *',
    description='A pipeline to scrape, clean, transform, and load real estate data',
    catchup=False
)

def pass_data(**kwargs):
    return kwargs['task_instance'].xcom_pull(task_ids=kwargs['downstream_task_id'])

scrape_novel_task = PythonOperator(
    task_id='scrape_novel',
    python_callable=scrape_novel,
    provide_context=True,
    dag=dag
)

clean_novel_task = PythonOperator(
    task_id='clean_novel',
    python_callable=clean_novel,
    provide_context=True,
    dag=dag
)

push_novel_task = PythonOperator(
    task_id='push_novel',
    python_callable=push_novel,
    provide_context=True,
    dag=dag
)

scrape_square_task = PythonOperator(
    task_id='scrape_square',
    python_callable=scrape_square,
    provide_context=True,
    dag=dag
)

clean_square_task = PythonOperator(
    task_id='clean_square',
    python_callable=clean_square(),
    provide_context=True,
    dag=dag
)

push_square_task = PythonOperator(
    task_id='push_square',
    python_callable=push_square,
    provide_context=True,
    dag=dag
)

scrape_novel_task >> clean_novel_task >> push_novel_task
scrape_square_task >> clean_square_task >> scrape_square_task
