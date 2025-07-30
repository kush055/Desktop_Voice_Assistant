import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


df = pd.read_csv('air_quality_dataset.csv') 
print(df.head())              
print(df.info())              

df.fillna(method='ffill', inplace=True)


df.drop_duplicates(inplace=True)


label_encoder = LabelEncoder()
df['Category'] = label_encoder.fit_transform(df['Category'])


df = pd.get_dummies(df, columns=['Category', 'Type']) 

scaler = StandardScaler()
df[['Feature1', 'Feature2']] = scaler.fit_transform(df[['Feature1', 'Feature2']]) 
print(df.head())
