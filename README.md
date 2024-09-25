# Sales Data ETL Pipeline with Apache Airflow on Google Cloud

## Overview

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline for processing sales data using Apache Airflow and Google Cloud Platform. The pipeline extracts raw sales data from Google Cloud Storage, transforms it by aggregating monthly profit, and stores the processed data back into a separate Cloud Storage bucket.

The pipeline is orchestrated using Apache Airflow, which runs on Google Compute Engine, ensuring the ETL process is automated, scalable, and easily maintainable.

## Architecture

### Components

1. **Google Cloud Storage**
   - **Source Bucket:** `incoming-data-etl` (Raw sales data stored as CSV)
   - **Destination Bucket:** `processed_data_etl` (Processed data stored as CSV after ETL)

2. **Apache Airflow**
   - Manages the ETL process, automates scheduling, and handles task orchestration.

3. **Google Cloud Compute Engine**
   - Hosts and runs Apache Airflow for efficient ETL execution.

4. **Python (ETL Script)**
   - Processes raw data and uploads transformed data back to the destination bucket.

### ETL Flow

1. **Extract** raw sales data (CSV) from the Source Data Bucket.
2. **Transform** the data:
   - Convert `Order Date` into datetime format.
   - Aggregate the `Profit` column on a monthly basis.
3. **Load** the transformed data (monthly profit) into the Processed Data Bucket.
4. The entire process is automated and scheduled via Apache Airflow, with logs and alerts for monitoring.

### Diagram:

![diagram]()
