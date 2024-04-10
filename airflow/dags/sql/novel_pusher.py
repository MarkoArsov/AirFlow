import pandas as pd

def push_novel(**kwargs):
    ti = kwargs['ti']
    cleaned_data = ti.xcom_pull(task_ids='clean_novel', key='cleaned_data')
    df = pd.DataFrame.from_dict(cleaned_data)

