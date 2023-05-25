import os

from crawler import get_bcc_news, get_bbc_news_endpoints
from save_to_bigquery import save_to_bigquery


bbc_news_data = get_bcc_news(get_bbc_news_endpoints())

current_dir = os.path.dirname(os.path.abspath(__file__))
credentials_path = os.path.join(current_dir, "credentials", "sa_gbq_crawler_credentials.json")  # noqa: E501

save_to_bigquery(bbc_news_data, "crawler", "bbc_news", credentials_path)
