import pandas as pd


def remove_substrings(string):
    if not string or isinstance(string, list) or not isinstance(string, str):
        return string
    for item in ['\r', '\t', '\n', '€']:
        string = string.replace(item, '')
    return string if string else None


def clean_square(**kwargs):
    ti = kwargs['ti']
    scraped_data = ti.xcom_pull(task_ids='scrape_square', key='scraped_data')
    df = pd.DataFrame.from_dict(scraped_data)

    new_columns = []
    for key in list(df):
        new_columns.append(key.strip())

    df.columns = new_columns

    for column in df.columns:
        df[column] = df[column].apply(remove_substrings)

    df = df.drop(columns=['Да', 'Не', '1', '4'])
    df.rename(columns={
        'Линк': 'link',
        'Шифра': 'code',
        'Опис': 'description',
        'Слики': 'images',
        'Последна промена': 'lastmodifiedon',
        'Населба': 'municipality',
        'Локација': 'location',
        'Површина': 'surfacearea',
        'Број на соби': 'numberofrooms',
        'Број на спални': 'numberofsleepingroms',
        'Кат': 'floornumber',
        'Ентериер': 'interior',
        'Број на купатила': 'numberofbathrooms',
        'Тераса': 'balcony',
        'Двор': 'yard',
        'Клима': 'airconditioning',
        'Сопствено парно': 'heating',
        'Имотен лист': 'propertysheet',
        'Цена': 'price',
        'Депозит': 'deposit',
        'Провизија': 'commission',
        'Лифт': 'elevator',
        'Нова Зграда': 'newbuilding',
        'Краток престој': 'shortstay',
        'Греење на струја': 'electricheating',
        'Ориентација': 'orientation',
        'Кујнски елементи': 'kitchenappliances',
        'Година на градба': 'yearofconstruction',
        'Реновиран': 'renovated',
        'Паркинг': 'parking',
        'Подрум': 'basement',
        'Интернет': 'internet',
        'Кабловска ТВ': 'cabletv',
        'Студенти': 'students',
        'Структура': 'structure',
        'Наместен': 'setup',
        'Достапно од': 'available from',
        'Спални соби': 'numberofsleepingroms',
        'Греење': 'heating',
        'Обезбедување': 'security',
        'Камери': 'cameras',
        'Камин': 'fireplace',
        'Нов': 'new',
    }, inplace=True)

    kwargs['ti'].xcom_push(key='cleaned_data', value=df.to_dict())
