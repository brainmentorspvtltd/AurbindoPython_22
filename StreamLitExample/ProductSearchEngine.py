import streamlit as st
import bs4
import urllib.request as url
from PIL import Image

# Decorator
@st.cache(suppress_st_warning=True)
def search(product_name):
    # replace space with +, because web url bars donot understand spaces
    product_name = product_name.replace(" ", "+")
    path = f"https://www.flipkart.com/search?q={product_name}"
    # make http request and will return http response
    response = url.urlopen(path)
    # we are fetching HTML of the page
    page = bs4.BeautifulSoup(response, "lxml")

    # fetching title of the product
    titles = page.find_all("div", {"class": "_4rR01T"})
    # fetching price of the product
    priceList = page.find_all("div", {"class": "_30jeq3 _1_WHN1"})
    # fetching rating of the product
    ratingList = page.find_all("div", {"class" : "_3LWZlK"})
    # fetching images of the product
    images = page.find_all("img", {"class": "_396cs4 _3exPp9"})

    # downloading images first
    for i in range(len(images)):
        img_url = images[i]["src"]
        url.urlretrieve(img_url, "images/img_{}.png".format(i))

    for i in range(len(titles)):
        # show product title
        st.write("Title : {}".format(titles[i].text))
        # show product price
        st.write("Price : {}".format(priceList[i].text))
        # show rating of product
        st.write("Rating : {}".format(ratingList[i].text))
        # read image
        img = Image.open("images/img_{}.png".format(i))
        # display image
        st.image(img, caption=titles[i].text, width=100)
        # show 10 stars
        st.write("*" * 10)

# display title of website
st.title("Product Search Engine...")
# some text you want to display below title
st.write("Simple Product Search Engine Application using Web Scraping...")

# will build a form
form = st.form(key="search_form")
# will create text box
product_name = form.text_input(label="Enter Product Name: ")
# will create submit button
submit_btn = form.form_submit_button(label="Start Searching...")

# will check if we have clicked on submit button
if submit_btn:
    # if button is clicked then it will work only
    st.write("You clicked on submit...")
    # after clicking on submit button search() will be called...
    search(product_name)

