import pandas as pd 
import xgboost as xgb

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

FEATURE = ['MinTemp', 'MaxTemp', 'Rainfall', 'WindGustDir', 'WindGustSpeed',
            'WindDir9am', 'WindDir3pm', 'WindSpeed9am', 'WindSpeed3pm',
            'Humidity9am', 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Temp9am',
            'Temp3pm', 'RainToday']

def read_data(location):
  data = pd.read_csv('DATA/{}.csv'.format(location))
  data.drop(columns=['Unnamed: 0'], inplace=True)

  data['RainToday'] = round(data['RainToday'])
  data['RainTomorrow'] = round(data['RainTomorrow'])

  return data

def train_test(data):
  x_train, x_test, y_train, y_test = train_test_split(data.iloc[:,1:-1], data.iloc[:,-1], test_size=0.2, random_state=0)

  return x_train, y_train, x_test, y_test

"""#Train on all feature"""

def XGBoost(location):
  data = read_data(location)
  x_train, y_train, x_test, y_test = train_test(data)

  import xgboost as xgb
  params = {'objective':'binary:logistic',
            'max_depth': 3,
            'learning_rate': 1,
            'n_estimators':10,
            'random_state':21}

  xg = xgb.XGBClassifier(**params)
  xg.fit(x_train, y_train)
  y_pred = xg.predict(x_test)

  return y_test, y_pred

params = {'objective':'binary:logistic',
          'max_depth': 3,
          'learning_rate': 1,
          'n_estimators':10,
          'random_state':21}  

model = xgb.XGBClassifier(**params)

# #Test input mưa
input = {'MinTemp':13.5,
         'MaxTemp':36.1,

         'Temp3pm':35.3,

         'WindDir3pm':'ENE',

         'WindGustSpeed':43,
         'WindSpeed3pm':11,

         'Humidity9am':65,
          
         'Pressure9am':1017.1,
         }

def encode(sample_input):
  sample_data = pd.read_csv('DATA/weatherAUS.csv')
  le = LabelEncoder()

  if 'WindGustDir' in sample_input.columns:
    le_WindGustDir = le.fit(sample_data['WindGustDir'])
    sample_input['WindGustDir'] = le_WindGustDir.transform(sample_input['WindGustDir'])
  if 'WindDir9am' in sample_input.columns:
    le_WindDir9am = le.fit(sample_data['WindDir9am'])
    sample_input['WindDir9am'] = le_WindDir9am.transform(sample_input['WindDir9am'])
  if 'WindDir3pm' in sample_input.columns:
    le_WindDir3pm = le.fit(sample_data['WindDir3pm'])
    sample_input['WindDir3pm'] = le_WindDir3pm.transform(sample_input['WindDir3pm'])
  if 'RainToday' in sample_input.columns:
    le_RainToday = le.fit(sample_data['RainToday'])
    sample_input['RainToday'] = le_RainToday.transform(sample_input['RainToday'])

  return sample_input

def train_model(location, **info):
  features = list(info.keys())
  sample_input = pd.DataFrame.from_dict([info])
  sample_input = encode(sample_input)

  data = read_data(location)
  
  for feature in features:
    if feature not in data.columns:
      features.remove(feature)
      sample_input.drop(columns=feature, inplace=True)
  
  x_train, y_train, x_test, y_test = train_test(data)
  x_train = x_train[features]
  x_test = x_test[features]

  model.fit(x_train, y_train)

  result = model.predict(sample_input)

  return result