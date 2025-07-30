from sklearn.preprocessing import LabelEncoder, StandardScaler

# 1. Check for missing values (though dataset shows no nulls, confirm)
missing_values = df.isnull().sum()

# 2. Encode categorical features
label_encoders = {}
for col in ['Location_Type', 'Source_Label']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# 3. Scale numerical features (exclude encoded categorical columns)
numerical_cols = df.drop(columns=['Location_Type', 'Source_Label']).columns
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Return the processed dataset
df.head(), missing_values
