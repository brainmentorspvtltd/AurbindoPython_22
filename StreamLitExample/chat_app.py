import streamlit as st
from datetime import datetime as dt
import os, random, glob
import json
import urllib.request as url

# intent
greetIntent = ["hi", "hey", "hello", "hi there", "hello there", "hey there"]
dateIntent = ["what's the date","tell me date","date","today's date"]
timeIntent = ["what's the time","tell me time","time","time please","current time"]
songIntent = ["play song", "please play song", "start music", "song", "music"]
newsIntent = ["tell me news", "tell me sports news", "tell me entertainment news", "tell me health news", "tell me science news"]

songsPath = r"D:\Batches\Songs\new_songs"

# display title of website
st.title("Chat Application")
# some text you want to display below title
st.write("Simple Chat App...")

# will build a form
form = st.form(key="search_form")
# will create text box
msg = form.text_input(label="Enter Your Message: ")
# will create submit button
submit_btn = form.form_submit_button(label="Submit...")

# will check if we have clicked on submit button
if submit_btn:

    st.write("You clicked on submit...")
    msg = msg.lower()

    # if msg == "hi" or msg == "hello" or msg == "hey" or msg == "hi there" or msg == "hello there":
    #     print("Hello User")

    if msg in greetIntent:
        st.write("Hello User")
    elif msg in dateIntent:
        current_date = dt.now().date()
        st.write("Date is : {}".format(current_date.strftime("%d %b,%y,%a")))
    elif msg in timeIntent:
        current_time = dt.now().time()
        st.write("Time is : {}".format(current_time.strftime("%I:%M:%S,%p")))
    elif msg in songIntent:
        os.chdir(songsPath)
        # songs = os.listdir()
        songs = glob.glob("*.mp3")
        song = random.choice(songs)
        os.startfile(song)
    elif msg in newsIntent:
        API_KEY = "695e07af402f4b119f0703e9b19f4683"
        category = msg.split()[-2]
        path = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={API_KEY}"
        response = url.urlopen(path)

        data = json.load(response)
        articles = data["articles"]
        n = len(articles)

        for i in range(n):
            st.write(articles[i]["title"])
    elif msg == "bye":
        st.write("Bye User")
        chat = False
    else:
        st.write("I don't understand...")


