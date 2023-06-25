import pandas as pd


def read_data(year) -> pd.DataFrame:
    data_path = './data/'
    file_name = f'data-jumlah-penduduk-berdasarkan-pekerjaan-per-kelurahan-tahun-{year}.csv'
    file_path = data_path + file_name
    return pd.read_csv(file_path)


def concat_data(dfs=[]) -> pd.DataFrame:
    return pd.concat(dfs, ignore_index=True)