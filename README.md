## Sales Data ETL Pipeline with Apache Airflow on Google Cloud

### Overview
This project implements an end-to-end ETL (Extract, Transform, Load) Pipeline for processing sales data using Apache Airflow and Google Cloud Platform. The pipeline extracts raw sales data from Google Cloud Storage, transforms it (aggregating monthly profit), and stores the processed data back in a separate Cloud Storage bucket.

The pipeline is orchestrated using Apache Airflow, running on Google Compute Engine, ensuring that the ETL process is automated, scalable, and easily maintainable.

### Architecture

#### Components:

1. Google Cloud Storage:
  - Source Bucket: incoming-data-etl (Raw sales data stored as CSV).
  - Destination Bucket: processed_data_etl (Processed data stored as CSV after ETL).
2. Apache Airflow:
  - Airflow is used to manage the ETL process, automate scheduling, and handle the orchestration of tasks.
3. Google Cloud Compute Engine:
  - Airflow is deployed and hosted on Google Cloud Compute Engine for efficient ETL execution.
4. Python (ETL script):
  - A Python script processes the raw data and uploads the transformed data back to the destination bucket.

#### ETL Flow:
1. Extract raw sales data (CSV) from the Source Data Bucket.
2. Transform the data:
  - Convert Order Date into datetime format.
  - Aggregate the Profit column on a monthly basis.
3. Load the transformed data (monthly profit) into the Processed Data Bucket.
4. The entire process is automated and scheduled via Apache Airflow, with logs and alerts for monitoring.
