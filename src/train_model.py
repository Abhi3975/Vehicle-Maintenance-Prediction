import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from data_prep import preprocess_data
import os

def train_vehicle_model(data_path='data/vehicle_maintenance_data.csv'):
    # Load data
    df = pd.read_csv(data_path)
    
    # Preprocess
    X, y = preprocess_data(df)
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    
    # Feature Importance
    importances = model.feature_importances_
    feature_names = X.columns
    feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
    print("\nTop Features:\n", feature_importance_df.sort_values(by='Importance', ascending=False))
    
    # Save Model
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/vehicle_model.pkl')
    print("\nModel saved to models/vehicle_model.pkl")

if __name__ == "__main__":
    train_vehicle_model()
