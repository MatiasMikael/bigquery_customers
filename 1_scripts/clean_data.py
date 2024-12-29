import pandas as pd
import os
import logging
from datetime import datetime

def setup_logging():
    log_folder = "C:/Users/Matias/Desktop/bigquery_customers/5_logs"
    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, f"clean_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

def clean_data(input_file, output_file):
    logging.info("Starting data cleaning...")
    try:
        # Read the dataset
        logging.info(f"Reading data from {input_file}")
        print(f"Reading data from {input_file}")
        df = pd.read_csv(input_file)

        # Drop unwanted columns
        columns_to_drop = ["Work Experience", "Family Size"]
        logging.info(f"Dropping columns: {columns_to_drop}")
        print(f"Dropping columns: {columns_to_drop}")
        df = df.drop(columns=columns_to_drop, errors='ignore')

        # Save cleaned dataset
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        df.to_csv(output_file, index=False)
        logging.info(f"Cleaned data saved to {output_file}")
        print(f"Cleaned data saved to {output_file}")
    except Exception as e:
        logging.error(f"Error during data cleaning: {e}")
        print(f"Error during data cleaning: {e}")
        raise

if __name__ == "__main__":
    setup_logging()
    input_path = "C:/Users/Matias/Desktop/bigquery_customers/2_data/Customers.csv"
    output_path = "C:/Users/Matias/Desktop/bigquery_customers/2_data/cleaned_customers.csv"
    try:
        clean_data(input_path, output_path)
        print("Cleaned data process completed successfully.")
    except Exception as e:
        print("An error occurred. Check logs for details.")