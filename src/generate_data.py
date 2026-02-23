import pandas as pd
import numpy as np
import os

def generate_sample_data(output_path='data/vehicle_maintenance_data.csv'):
    np.random.seed(42)
    n_samples = 1000
    
    models = ['Sedan', 'SUV', 'Truck', 'Van', 'Bus']
    fuel_types = ['Petrol', 'Diesel', 'Electric']
    histories = ['Good', 'Average', 'Poor']
    
    data = {
        'Vehicle_Model': np.random.choice(models, n_samples),
        'Mileage': np.random.randint(5000, 200000, n_samples),
        'Maintenance_History': np.random.choice(histories, n_samples),
        'Reported_Issues': np.random.randint(0, 10, n_samples),
        'Vehicle_Age': np.random.randint(1, 20, n_samples),
        'Fuel_Type': np.random.choice(fuel_types, n_samples),
        'Odometer_Reading': np.random.randint(5000, 250000, n_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Logic for target 'Need_Maintenance'
    # High mileage, poor history, or high reported issues increase maintenance need
    risk_score = (
        (df['Mileage'] / 100000) * 0.4 + 
        (df['Reported_Issues'] / 10) * 0.3 + 
        (df['Vehicle_Age'] / 20) * 0.2 +
        (df['Maintenance_History'].map({'Good': 0, 'Average': 0.5, 'Poor': 1})) * 0.5
    )
    
    df['Need_Maintenance'] = (risk_score > 0.8).astype(int)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Sample data generated at {output_path}")

if __name__ == "__main__":
    generate_sample_data()
