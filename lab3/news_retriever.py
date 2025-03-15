import requests
import json
import config


class Retriever:
    BASE_URL = "https://newsapi.org/v2/everything"

    def __init__(self):
        self.api_key = "9570dc4a629f432b9f729c8991fefd9a"

    def fetch_articles(self, topic, page_size=5):
        """Fetches news articles for a given topic."""
        params = {
            "q": topic,
            "apiKey": self.api_key,
            "language": "en",
            "pageSize": page_size,
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()

        if data.get("status") != "ok":
            print("Error fetching news:", data.get("message"))
            return []

        return data.get("articles", [])

