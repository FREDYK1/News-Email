from abc import abstractstaticmethod

import requests
from email_implementation import send_email

topic = "wsj.com"

api_key = "487045a82f2649fda9dd43d48c8a77d3"
url = ("https://newsapi.org/v2/everything?"
       f"domains={topic}"
       "&apiKey=487045a82f2649fda9dd43d48c8a77d3"
       "&language=en")

request = requests.get(url)
content = request.json()

article_string = ""

for article in content["articles"]:
    if article['title'] and article["description"] is not None:
        article_string +=("Subject: Today's news "
                         + "\n" + article["title"]
                         + "\n" + article["description"]
                         + "\n" + article["url"] +  2*"\n")


send_email(article_string)

