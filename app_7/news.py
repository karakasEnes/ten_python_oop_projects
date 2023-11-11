
import requests
from dotenv import dotenv_values


class NewsFeed:
    base_url = 'https://newsapi.org/v2/everything'
    api_key = dotenv_values('.env').get('API_KEY_NEWS')

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = (f"{self.base_url}?"
               f"q={self.interest}&"
               f"from={self.from_date}&"
               f"to={self.to_date}&"
               f"language={self.language}&"
               f"apiKey={self.api_key}")

        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ""
        for article in articles:
            email_body += article['title'] + "\n" + article['url'] + "\n\n"

        return email_body


# news_feed = NewsFeed(interest='nasa',
#                      from_date='2023-11-9',
#                      to_date='2023-11-10',
#                      language='en')
#
# print(news_feed.get())
