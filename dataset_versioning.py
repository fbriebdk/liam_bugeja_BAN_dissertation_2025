import os
import pandas as pd
from datetime import datetime

DATASET_FOLDER = "datasets_versions"

if not os.path.exists(DATASET_FOLDER):
    os.makedirs(DATASET_FOLDER)

def save_dataset_version(data, stage):
    timestamp = datetime.now().strftime("%Y%m%d")
    filename = os.path.join(DATASET_FOLDER, f"EPL_dataset_{stage}_{timestamp}.csv")
    
    # Save to CSV
    data.to_csv(filename, index=False)
    print(f"Dataset saved as: {filename}")


def clean_dataset(data):
    data = pd.read_csv(file_path)

    # Define columns to remove
    columns_to_drop = ['Div', 'Date', 'Time', 'Referee', 'FTHG', 'FTAG']

    # Drop columns if they exist
    data_cleaned = data.drop(columns=columns_to_drop, errors='ignore')

    # Save cleaned dataset as  NEW file
    save_dataset_version(data_cleaned, "cleaned")

    return data_cleaned

if __name__ == "__main__":
    file_path = "EPL_2019_2024.csv"  
    clean_dataset(file_path)
