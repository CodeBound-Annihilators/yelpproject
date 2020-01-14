import pandas as pd



def find_category(data, category):
    data['__python_check'] = data['category'].apply(lambda x: True if x == category else False)
    data = data.loc[data['__python_check'], :]
    data = data.drop(columns = ['__python_check'])
    return data


def health_inspector_df(data):
    final = pd.DataFrame()
    data['number_of_violations'] = data['Violations'].apply(lambda x: len(x))
    data[]