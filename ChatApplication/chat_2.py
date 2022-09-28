# import datetime as dt
from datetime import datetime as dt
import os, random, glob

# intent
greetIntent = ["hi", "hey", "hello", "hi there", "hello there", "hey there"]
dateIntent = ["what's the date","tell me date","date","today's date"]
timeIntent = ["what's the time","tell me time","time","time please","current time"]
songIntent = ["play song", "please play song", "start music", "song", "music"]

songsPath = r"D:\Batches\Songs\new_songs"

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    # if msg == "hi" or msg == "hello" or msg == "hey" or msg == "hi there" or msg == "hello there":
    #     print("Hello User")

    if msg in greetIntent:
        print("Hello User")
    elif msg in dateIntent:
        current_date = dt.now().date()
        print("Date is :",current_date.strftime("%d %b,%y,%a"))
    elif msg in timeIntent:
        current_time = dt.now().time()
        print("Time is :",current_time.strftime("%I:%M:%S,%p"))
    elif msg in songIntent:
        os.chdir(songsPath)
        # songs = os.listdir()
        songs = glob.glob("*.mp3")
        song = random.choice(songs)
        os.startfile(song)
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand...")
