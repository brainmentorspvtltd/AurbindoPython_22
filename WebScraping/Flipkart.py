import urllib.request as url
import bs4

product_name = input("Enter product name : ")
product_name = product_name.replace(" ", "+")

path = f"https://www.flipkart.com/search?q={product_name}"
response = url.urlopen(path)
page = bs4.BeautifulSoup(response, "lxml")
# title = page.find("div", {"class" : "_4rR01T"})
# print(title.text)
#
# price = page.find("div", {"class" : "_30jeq3 _1_WHN1"})
# print(price.text)

titles = page.find_all("div", {"class" : "_4rR01T"})
priceList = page.find_all("div", {"class" : "_30jeq3 _1_WHN1"})

for i in range(len(titles)):
    print(titles[i].text)
    print(priceList[i].text)
    print("*" * 10)

