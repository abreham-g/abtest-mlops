import pandas as pd
import dvc.api

path = 'Data/ADSmartdata.csv'
repo = 'C:\Users\Abreham\Desktop\10acad\abtest-mlops'
version = 'v1'

data_url = dvc.api.get_url(
    path=path,
    repo=repo,
    rev=versio
    )
data = pd.read_csv(data_url,sep=",")

mlflow.log_params('data_url',data_url)
mlflow.log_params('data_version',data_version)
mlflow.log_params('data_rows',data.shape[0])
mlflow.log_params('data_cols',data.shape[1])

train,tast = train_tast_split(data)
