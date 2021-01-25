import pandas as pd


def read_excel(file_path):
    df = pd.read_excel(file_path, engine='openpyxl')
    df = df.fillna('')
    return df


def read_vpon_geo_excel(file_path):
    df = read_excel(file_path)
    df = df.drop(columns=['ON_DSP_WEB', 'ID', 'IGNORE_PM_SORT', 'IGNORE_COUNTRY_NAME',
                          'IGNORE_DSP_UPDATE_VERSION', 'IGNORE_PM_NOTE',
                          'IGNORE_PDO_NOTE', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18',
                          'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21'])
    name_list = [s for idx, s in enumerate(df['IGNORE_GEOGRAPHIC_NAME'])]
    df['Name'] = name_list
    df = df.reindex(columns=['Name', 'IGNORE_GEOGRAPHIC_NAME', 'IGNORE_GEO_LEVEL', 'DESC_1_TIER',
                             'DESC_2_TIER', 'DESC_3_TIER', 'IGNORE_ID',
                             'IGNORE_TIER_1_COUNTRY', 'IGNORE_TIER_2_REGION', 'IGNORE_COUNTRY_CODE'])
    return df


def read_csv(file_path):
    result_table = pd.read_csv(file_path)
    result_table = result_table.fillna('')
    return result_table




def save_file(file_path, content):
    try:
        with open(file_path, 'w') as fp:
            fp.writelines(content)
        return True
    except Exception as e:
        raise Exception("save_file error", e)
