from google.cloud import storage
import pandas as pd
import io
from datetime import datetime

# Initialize the Google Cloud Storage client
client = storage.Client()

def run_etl():
    # Define the source bucket and file path
    source_bucket_name = 'incoming-data-etl'
    source_file_name = 'sales.csv'

    # Define the destination bucket and file path
    destination_bucket_name = 'processed_data_etl'

    # Generate a timestamp for the output file name
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    destination_file_name = f'sales_monthly_{timestamp}.csv'

    # Get the source bucket and blob (file)
    source_bucket = client.get_bucket(source_bucket_name)
    source_blob = source_bucket.blob(source_file_name)

    # Download the CSV data as a string
    data = source_blob.download_as_text()

    # Read the CSV data into a DataFrame
    df = pd.read_csv(io.StringIO(data))

    # Convert the 'Order Date' column to datetime format
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')

    # Extract the year and month from the 'Order Date'
    df['YearMonth'] = df['Order Date'].dt.to_period('M')

    # Group by 'YearMonth' and sum the 'Profit' column for each month
    monthly_profit = df.groupby('YearMonth')['Profit'].sum().reset_index()

    # Save the processed DataFrame to a CSV string
    csv_data = monthly_profit.to_csv(index=False)

    # Get the destination bucket
    destination_bucket = client.get_bucket(destination_bucket_name)

    # Create a new blob and upload the CSV data to the destination bucket
    destination_blob = destination_bucket.blob(destination_file_name)
    destination_blob.upload_from_string(csv_data, content_type='text/csv')

    print(f"Processed data saved to gs://{destination_bucket_name}/{destination_file_name}")

