import urllib.request as url
import json

category = input("Enter News Category : Sports/Business/Entertainment/Health/Science/Technology : ")
category = category.lower()

API_KEY = "695e07af402f4b119f0703e9b19f4683"

path = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={API_KEY}"
response = url.urlopen(path)

data = json.load(response)
articles = data["articles"]
n = len(articles)

for i in range(n):
    print(articles[i]["title"])