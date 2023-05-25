import re
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


def get_bbc_news_endpoints():
    selector = get_parsed_selector("https://www.bbc.com/news")["selector"]

    news_urls = selector.css("a.gs-c-promo-heading::attr(href)").getall()
    regex_pattern = r"/news/[a-z-]+\d+"

    # Filter only news URLs and eliminate possible duplicate URLs
    filtered_news = list(
        set(
            "https://www.bbc.com" + news
            for news in news_urls
            if re.match(regex_pattern, news)
        )
    )
    return filtered_news
