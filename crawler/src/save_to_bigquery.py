import google.api_core.exceptions
import time
from google.cloud import bigquery
from google.oauth2 import service_account


def save_to_bigquery(data, dataset_id, table_id, credentials_path):
    # Instantiate the BigQuery client with credentials
    credentials = service_account.Credentials.from_service_account_file(credentials_path)  # noqa: E501
    client = bigquery.Client(credentials=credentials)
    print("\nBigQuery: Connection established with BigQuery")
    print("BigQuery: Connection closed\n")

    # Create the dataset if it doesn't exist
    dataset_ref = client.dataset(dataset_id)
    dataset = bigquery.Dataset(dataset_ref)
    dataset.location = "US"

    try:
        client.create_dataset(dataset)
        print("BigQuery: Dataset created:", dataset_id)
    except google.api_core.exceptions.Conflict:
        print("BigQuery: Dataset already exists:", dataset_id)
    except Exception as error:
        print("BigQuery: Error creating dataset:", error)

    # Create the table if it doesn't exist
    table_ref = dataset_ref.table(table_id)
    table = bigquery.Table(table_ref)

    table.schema = [
        bigquery.SchemaField("url", "STRING"),
        bigquery.SchemaField("headline", "STRING"),
        bigquery.SchemaField("author", "STRING"),
        bigquery.SchemaField("subtitle", "STRING"),
        bigquery.SchemaField("text", "STRING"),
        bigquery.SchemaField("timestamp", "TIMESTAMP"),
    ]

    try:
        table = client.create_table(table, exists_ok=True)
        print("BigQuery: Table created:", table_id)
    except google.api_core.exceptions.Conflict:
        print("BigQuery: Table already exists:", table_id)
    except Exception as error:
        print("BigQuery: Error creating table:", error)

    # Insert data into the table
    try:
        # Wait a while after creating the table
        time.sleep(10)
        errors = client.insert_rows_json(table, data)
    except google.api_core.exceptions.NotFound:
        print("BigQuery: Error inserting rows. Table not found. Trying again")
        time.sleep(40)
        errors = client.insert_rows_json(table, data)
    finally:
        if errors:
            print("BigQuery: Error inserting rows:", errors)
        else:
            print("BigQuery: Data inserted into BigQuery")

    print("BigQuery: Connection closed\n")
