import dvc.api

path = 'Data/ADSmartdata.csv'
repo = 'C:\Users\Abreham\Desktop\10acad\abtest-mlops'
version = 'v1'

data_url = dvc.api.get_url(
    path=path,
    repo=repo,
    rev=versio
    )
