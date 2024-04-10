import pandas as pd

def remove_substrings(string):
  if not string or isinstance(string, list) or not isinstance(string, str):
    return string
  for item in ['\r', '\t','\n']:
    string = string.replace(item, '')
  return string if string else None

def clean_novel(**kwargs):
    ti = kwargs['ti']
    scraped_data = ti.xcom_pull(task_ids='scrape_novel', key='scraped_data')
    df = pd.DataFrame.from_dict(scraped_data)
    new_columns = []
    for key in list(df):
      new_columns.append(key.replace(':', "").strip())
    df.columns = new_columns
    for column in df.columns:
      df[column] = df[column].apply(remove_substrings)
    kwargs['ti'].xcom_push(key='cleaned_data', value=df.to_dict())

