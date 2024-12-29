### bigquery_customers

#### Project Overview

This project focuses on managing customer data using BigQuery. It includes fetching raw data from Kaggle, cleaning the data using Python, and loading the cleaned data into a BigQuery table. SQL queries are then executed on the data, and their results are saved in the 3_results directory. The project structure is as follows:

#### bigquery_customers/

1_scripts - Python scripts for data processing

2_data - Raw and cleaned data files

3_results - Query results and analysis

4_docs - Documentation

5_logs - Log files

#### Key Steps

1. Data Fetching: Downloaded raw data from Kaggle using curl. *Note: Using the curl command for data fetching is not the most optimal approach in this case, but it was used for practice purposes.*

2. Data Cleaning: Processed the data using the clean_data.py script. The cleaned file is saved as 2_data/cleaned_customers.csv.

3. BigQuery Integration: Loaded the cleaned data into a BigQuery table: bigquerycustomers.customers_dataset.cleaned_customers.

4. SQL Queries: Executed multiple SQL queries and saved their results in 3_results.

#### License

This project is licensed under the MIT License. The dataset https://www.kaggle.com/datasets/datascientistanna/customers-dataset is sourced from Kaggle under the Open Database License for both the database and its contents.
