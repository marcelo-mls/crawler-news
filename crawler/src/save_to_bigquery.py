from google.cloud import bigquery
from google.oauth2 import service_account


def save_to_bigquery(data, dataset_id, table_id):
    # Instantiate the BigQuery client with credentials
    credentials_path = 'src/credentials/sa_gbq_crawler_credentials.json'
    credentials = service_account.Credentials.from_service_account_file(credentials_path)  # noqa: E501
    client = bigquery.Client(credentials=credentials)
    print("\nBigQuery: Connection established with BigQuery")
    print("BigQuery: Connection closed\n")
