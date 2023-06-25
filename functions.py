import pandas as pd


def read_data(year) -> pd.DataFrame:
    data_path = './data/'
    file_name = f'data-jumlah-penduduk-berdasarkan-pekerjaan-per-kelurahan-tahun-{year}.csv'
    file_path = data_path + file_name
    return pd.read_csv(file_path)


def concat_data(dfs=[]) -> pd.DataFrame:
    return pd.concat(dfs, ignore_index=True)


def read_all_data() -> pd.DataFrame:
    dfs = []
    for year in range(2013, 2022):
        df = read_data(str(year))
        dfs.append(df)
    return concat_data(dfs)


def load_data(year_choice):
    if year_choice == "All":
        data = read_all_data()
    else:
        data = read_data(year_choice)
    return data