import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

df = pd.read_csv("flipkart.csv")

categorical = list(df.select_dtypes(include='O').columns)
numerical = list(df.select_dtypes(exclude='O').columns)

#fill the null values
for col in df[numerical]:
    df[col]=df[col].fillna(df[col].mean())

for col in df[categorical]:
    df[col]=df[col].fillna(df[col].mode()[0])


df['retail_price'] = np.log1p(df['retail_price'])

SEED = 42
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=SEED)

df_full_train = df_full_train.reset_index(drop=True)
y_full_train = np.log1p(df_full_train['retail_price'].values)

df_test = df_test.reset_index(drop=True)
y_test = np.log1p(df_test['retail_price'].values)

del(df_test['retail_price'])
del(df_full_train['retail_price'])

categorical = [
'pid', 'is_FK_Advantage_product', 'product_rating','overall_rating', 'brand', 
]
numerical= ['discounted_price']

def model_eval(true, predicted):
    mae = mean_absolute_error(true, predicted)
    mse = mean_squared_error(true, predicted)
    rmse = mean_squared_error(true, predicted,squared=False)
    r2 = r2_score(true, predicted)
    return mae,mse, rmse, r2

opt_params = {
'eta': 0.4, 
'max_depth': 10,
'min_child_weight': 2,

'objective': 'reg:squarederror',
'nthread': 8,

'seed': 1,
'verbosity': 1,
}
num_round = 100

train_full_dicts = df_full_train[categorical + numerical].to_dict(orient='records')
dv = DictVectorizer(sparse=True)
X_full_train = dv.fit_transform(train_full_dicts)

test_dicts = df_test.to_dict(orient='records')
X_test = dv.transform(test_dicts)

d_full_train = xgb.DMatrix(X_full_train, label=y_full_train, feature_names= dv.get_feature_names_out().tolist())
dtest = xgb.DMatrix(X_test, feature_names= dv.get_feature_names_out().tolist())

xgbst = xgb.train(opt_params, d_full_train, num_round)
y_pred = xgbst.predict(dtest)


mae,mse, rmse, r2  = model_eval(y_test, y_pred)
print(f'mae: {mae}, mse: {mse}, rmse: {rmse}, r2: {r2}')

output_file = f'model_reg={1.0}.bin'
output_file

f_out = open(output_file, 'wb')
pickle.dump((dv,xgbst), f_out)
f_out.close()

