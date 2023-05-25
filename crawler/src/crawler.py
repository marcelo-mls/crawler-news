import requests
from parsel import Selector


def get_parsed_selector(url):
    headers = {"User-Agent": "python-requests/2.31.0"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
    except requests.ReadTimeout:
        response = requests.get(url, headers=headers, timeout=5)
    finally:
        print(response.status_code, response.url)
        if response.status_code == 200:
            return {
                "url": response.url,
                "selector": Selector(text=response.text),
            }
