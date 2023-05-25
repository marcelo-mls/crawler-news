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


def get_articles_details(article_selector):
    news = dict()

    sel = article_selector["selector"]
    url = article_selector["url"]

    # CSS selectors to extract the details of a BBC article
    headline = sel.css("h1#main-heading::text").get()
    author = sel.css("div.ssrcss-68pt20-Text-TextContributorName::text").get()
    subtitle = sel.css("b.ssrcss-hmf8ql-BoldText::text").get()
    text = sel.css("article.ssrcss-pv1rh6-ArticleWrapper div.ssrcss-7uxr49-RichTextContainer p.ssrcss-1q0x1qg-Paragraph::text").getall()  # noqa: E501
    timestamp = sel.css("time[datetime]").xpath("@datetime").get()

    # Adding the extracted data to the dictionary
    news["url"] = url
    news["headline"] = headline.strip()
    news["author"] = author[3:] if author is not None else "not informed"
    news["subtitle"] = subtitle.strip()
    news["text"] = " ".join(text).strip()
    news["timestamp"] = timestamp

    return news
