from pytube import YouTube
from sys import argv
import os
import random as rd

PATH = "C:/Users/..." # Your path
run = True
symbol_list = ["☆", "❀", "✠", "✡", "✌", "☯", "☮"]


def fill_with_symbols():
    chosen = rd.choice(symbol_list)
    return chosen

while run:
    s = fill_with_symbols()
    link = input("Copy YouTube video URL here: ")
    yt = YouTube(link)
    print(f"""


 ╔══════════════════════════╗
{"  " + s * 16}
{s}    𝚈𝚘𝚞𝚝𝚞𝚋𝚎 to Mp4/Mp3   {s}
{s}         ❶ 🎞️            {s}
{s}         ❷ 🎵            {s}
{s}         ❸ ➲            {s}
{"  " + s * 16}
 ╚══════════════════════════╝
 
        """)
    choice = int(input(">>>"))
    if choice == 1:
        print("Title: ", yt.title)
        print("View: ", yt.views)
        yd = yt.streams.get_highest_resolution()
        yd.download(PATH)
        print(yt.title + " mp4 file has been successfully downloaded.")
    if choice == 2:
        video = yt.streams.filter(only_audio=True).first()
        destination = PATH
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '_audio_only' + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " mp3 file has been successfully downloaded.")
    if choice == 3:
        run = False
    else:
        print("Invalid choice. Try again.")
