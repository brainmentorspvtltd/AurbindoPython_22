import bs4
import urllib.request as url

product_name = "apple iphone 14"
product_name = product_name.replace(" ", "+")
path = f"https://www.flipkart.com/search?q={product_name}"
# make http request and will return http response
response = url.urlopen(path)
# we are fetching HTML of the page
page = bs4.BeautifulSoup(response, "lxml")

images = page.find_all("img", {"class" : "_396cs4 _3exPp9"})

for i in range(len(images)):
    img_url = images[i]["src"]
    url.urlretrieve(img_url, "images/img_{}.png".format(i))





