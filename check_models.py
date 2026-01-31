import sys
import os

# Add current directory to path
sys.path.insert(0, os.getcwd())

try:
    import joblib
    import pandas as pd
    import numpy as np
    
    # Load the metrics file to verify format
    metrics = pd.read_csv('model/metrics.csv')
    print("Current models in metrics.csv:")
    print(metrics['Model'].tolist())
    
    # Check for XGBoost
    if 'XGBoost' not in metrics['Model'].values:
        print("\nNeed to generate XGBoost model...")
    else:
        print("\n✓ XGBoost already in metrics")
    
    # Try to check if model files exist
    import glob
    models = glob.glob('model/*.pkl')
    print(f"\nExisting model files: {[os.path.basename(m) for m in models]}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
