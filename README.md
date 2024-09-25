## Sales Data ETL Pipeline with Apache Airflow on Google Cloud

### Overview
This project implements an end-to-end ETL (Extract, Transform, Load) Pipeline for processing sales data using Apache Airflow and Google Cloud Platform. The pipeline extracts raw sales data from Google Cloud Storage, transforms it (aggregating monthly profit), and stores the processed data back in a separate Cloud Storage bucket.

The pipeline is orchestrated using Apache Airflow, running on Google Compute Engine, ensuring that the ETL process is automated, scalable, and easily maintainable.
