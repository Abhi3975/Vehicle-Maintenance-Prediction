# test_agent.py
from src.agent.workflow import run_maintenance_agent

mock_vehicle = {
    'Vehicle_Model': 'Truck',
    'Mileage': 150000,
    'Maintenance_History': 'Poor',
    'Vehicle_Age': 10
}
risk_score = 0.95
top_factors = ['Maintenance_History', 'Mileage', 'Vehicle_Age']

print("Running Agent Test...")
report = run_maintenance_agent(mock_vehicle, risk_score, top_factors)
print("\n--- AGENT REPORT ---\n")
print(report)
print("\n--- TEST COMPLETE ---")
