from abc import abstractstaticmethod

import requests
from email_implementation import send_email

api_key = "487045a82f2649fda9dd43d48c8a77d3"
url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=487045a82f2649fda9dd43d48c8a77d3"

request = requests.get(url)
content = request.json()

article_string = ""

for article in content["articles"]:
    if article['title'] and article["description"]is not None:
        article_string += article["title"] + "\n" + article["description"] + 2*"\n"


send_email(article_string)

