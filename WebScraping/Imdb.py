import urllib.request as url
import bs4
path = "https://www.imdb.com/title/tt0371746/?ref_=nv_sr_srsg_0"
response = url.urlopen(path)
page = bs4.BeautifulSoup(response, "lxml")
title = page.find("h1", {"class" : "sc-b73cd867-0 eKrKux"})
print(title.text)

rating = page.find("span", {"class" : "sc-7ab21ed2-1 jGRxWM"})
print(rating.text)

summary = page.find("span", {"class" : "sc-16ede01-2 gXUyNh"})
print(summary.text)
