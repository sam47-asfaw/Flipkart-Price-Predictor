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
df['retail_price'] = np.log1p(df['retail_price'])

SEED = 42
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=SEED)

df_full_train = df_full_train.reset_index(drop=True)
y_full_train = df_full_train['retail_price'].values
del(df_full_train['retail_price'])

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

train_full_dicts = df_full_train.to_dict(orient='records')
dv = DictVectorizer(sparse=True)
X_full_train = dv.fit_transform(train_full_dicts)

test_dicts = df_test.to_dict(orient='records')
X_test = dv.transform(test_dicts)

d_full_train = xgb.DMatrix(X_full_train, label=y_full_train)
dtest = xgb.DMatrix(X_test, label=y_test)

xgbst = xgb.train(opt_params, d_full_train, num_round)
y_pred = xgbst.predict(dtest)

output_file = f'model_C={1.0}.bin'
output_file


f_out = open(output_file, 'wb')
pickle.dump((dv,xgbst), f_out)
f_out.close()