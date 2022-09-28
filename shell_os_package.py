Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os
os.startfile("song_1.mp3")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    os.startfile("song_1.mp3")
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'song_1.mp3'
os.getcwd()
'C:\\Python310'
os.listdir()
['DLLs', 'Doc', 'etc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python310.dll', 'pythonw.exe', 'Scripts', 'share', 'tcl', 'Tools', 'vcruntime140.dll', 'vcruntime140_1.dll']
os.chdir("D:\Batches\Songs")
os.chdir("D:\Batches\Songs\Users")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 16-17: truncated \UXXXXXXXX escape
os.chdir("D:\Batches\Songs\new_songs")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    os.chdir("D:\Batches\Songs\new_songs")
OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: 'D:\\Batches\\Songs\new_songs'
path = ""D:\Batches\Songs\new_songs""
SyntaxError: invalid syntax
path = "D:\Batches\Songs\new_songs"
path
'D:\\Batches\\Songs\new_songs'
print(path)
D:\Batches\Songs
ew_songs
os.chdir("D:\\Batches\\Songs\\new_songs")
os.chdir("D:/Batches/Songs/new_songs")
path = r"D:\Batches\Songs\new_songs"
# r- raw string
path
'D:\\Batches\\Songs\\new_songs'
print(path)
D:\Batches\Songs\new_songs
os.listdir()
['bang-bang.mp3', 'Faded.mp3', 'FadedCopy.mp3', 'fifa world cup.mp3', 'song.mp3', 'songCopy.mp3']
import random
songs = os.listdir()
random.choice(songs)
'songCopy.mp3'
random.choice(songs)
'fifa world cup.mp3'
random.choice(songs)
'songCopy.mp3'
os.startfile(random.choice(songs))
os.getcwd()
'D:\\Batches\\Songs\\new_songs'
path = r"D:\Batches\Songs"
os.chdir(path)
for root, folders, files in os.walk(path):
    print(root, folders, files)

    
D:\Batches\Songs ['new_songs', 'Users'] []
D:\Batches\Songs\new_songs [] ['bang-bang.mp3', 'Faded.mp3', 'FadedCopy.mp3']
D:\Batches\Songs\Users [] ['fifa world cup.mp3', 'song.mp3', 'songCopy.mp3']
files_path = []
for root, folders, files in os.walk(path):
    if len(files) > 0:
        f = files[i]
        song_path = root + "\\" + f
        print(song_path)
        files_path.append(song_path)

        
Traceback (most recent call last):
  File "<pyshell#36>", line 3, in <module>
    f = files[i]
NameError: name 'i' is not defined. Did you mean: 'id'?
for root, folders, files in os.walk(path):
    if len(files) > 0:
        for i in range(len(files)):
            f = files[i]
            song_path = root + "\\" + f
            print(song_path)
            files_path.append(song_path)

            
D:\Batches\Songs\new_songs\bang-bang.mp3
D:\Batches\Songs\new_songs\Faded.mp3
D:\Batches\Songs\new_songs\FadedCopy.mp3
D:\Batches\Songs\Users\fifa world cup.mp3
D:\Batches\Songs\Users\song.mp3
D:\Batches\Songs\Users\songCopy.mp3
os.startfile(random.choice(files_path))
os.startfile(random.choice(files_path))
os.startfile(random.choice(files_path))
os.listdir()
['new_songs', 'Users']
os.chdir("new_songs")
os.listdir()
['471551_RlI2lBF7EevSIYjva7WRBw.png', 'bang-bang.mp3', 'DBSCAN_tutorial.gif', 'Faded.mp3', 'FadedCopy.mp3', 'fifa world cup.mp3', 's20-5-Copy-2.png', 'song.mp3', 'songCopy.mp3']
import glob
glob.glob("*.mp3")
['bang-bang.mp3', 'Faded.mp3', 'FadedCopy.mp3', 'fifa world cup.mp3', 'song.mp3', 'songCopy.mp3']
path_1 = "D:\Batches\Songs\new_songs"
path_2 = r"D:\Batches\Songs\Users"
path_1 = r"D:\Batches\Songs\new_songs"
