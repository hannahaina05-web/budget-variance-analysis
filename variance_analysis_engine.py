# Python Framework for Departmental Budget Variance Analysis
# Designed to ingest, clean, and analyze corporate operational expenditures

import pandas as pd
import numpy as np

def run_variance_audit(data_source_path):
    print("[INFO] Initializing Financial Data Integrity Pipeline...")
    
    # Simulate loading corporate financial dataset
    # In practice, this maps to an enterprise SQL database dump or ERP export
    raw_data = {
        'Department': ['Finance', 'Operations', 'Sales', 'Marketing', 'Admin', 'HR', 'IT'],
        'Budgeted_Amount': [5000000, 12500000, 8000000, 4500000, 3500000, 2000000, 6000000],
        'Actual_Amount': [4950000, 13100000, 8200000, 3900000, 3550000, 1980000, 6400000]
    }
    
    # Load data into an analytical DataFrame structured with Pandas logic
    df = pd.DataFrame(raw_data)
    
    # 1. COMPUTE SYSTEMIC VARIANCE
    # Calculates the absolute numeric delta between budgeted parameters and actual data
    df['Variance'] = df['Actual_Amount'] - df['Budgeted_Amount']
    
    # 2. EVALUATE PERCENTAGE VARIANCE
    # Normalizes the dataset to show relative efficiency fluctuations
    df['Variance_Percentage'] = (df['Variance'] / df['Budgeted_Amount']) * 100
    
    # 3. APPLY CONDITIONAL ANOMALY FILTERS
    # Flags any department exceeding a standard +/- 5% baseline risk threshold
    df['Risk_Status'] = np.where(df['Variance_Percentage'].abs() > 5.0, 'CRITICAL VARIANCE', 'COMPLIANT')
    
    print("\n--- CORPORATE DATA INTEGRITY ANALYSIS REPORT ---")
    print(df.to_string(index=False))
    
    # Isolate systemic critical data points for management auditing
    critical_anomalies = df[df['Risk_Status'] == 'CRITICAL VARIANCE']
    print(f"\n[ALERT] System isolated {len(critical_anomalies)} cost centers requiring immediate operational audit review.")
    
    return df

# Execute data analysis framework
if __name__ == "__main__":
    run_variance_audit(data_source_path="corporate_ledger_dump.csv")
