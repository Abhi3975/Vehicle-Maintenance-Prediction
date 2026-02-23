import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(df, target_col='Need_Maintenance', is_training=True):
    """
    Cleans and prepares the vehicle data for ML models.
    """
    df = df.copy()
    
    # Handle missing values if any
    df = df.fillna(df.median(numeric_only=True))
    
    # Encoding categorical features
    categorical_cols = ['Vehicle_Model', 'Maintenance_History', 'Fuel_Type']
    le = LabelEncoder()
    
    for col in categorical_cols:
        if col in df.columns:
            df[col] = le.fit_transform(df[col].astype(str))
            
    # Target and Features
    if target_col in df.columns and is_training:
        X = df.drop(columns=[target_col])
        y = df[target_col]
        return X, y
    else:
        return df

if __name__ == "__main__":
    df = pd.read_csv('data/vehicle_maintenance_data.csv')
    X, y = preprocess_data(df)
    print("Features defined:", list(X.columns))
    print("Target class distribution:\n", y.value_counts())
