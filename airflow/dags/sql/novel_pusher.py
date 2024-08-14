import pandas as pd
from sqlalchemy import create_engine

def push_novel(**kwargs):
    ti = kwargs['ti']
    cleaned_data = ti.xcom_pull(task_ids='clean_novel', key='cleaned_data')
    df = pd.DataFrame.from_dict(cleaned_data)

    engine = create_engine('postgresql+psycopg2://airflow:airflow@localhost:54320/airflow')

    df.to_sql('Property', engine, schema='RealEstate', if_exists='replace', index=False)
    engine.dispose()

