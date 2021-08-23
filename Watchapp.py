import tkinter as tk
import time
import youtube_dl as yd
import os


ydl_opts = {}

ydl_opts2 = {
    "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }],
}



#defs'
def dwl_vid():
    url = entry.get()
    link = url.strip()
    with yd.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def dwl_sound():
    url = entry1.get()
    link = url.strip()
    with yd.YoutubeDL(ydl_opts2) as ydl:
        ydl.download([link]) 

    #os.chdir("c:\\")
    
    migrate_cache = bytes()

    for file in os.listdir("./"):
        os.rename(file, link)
        migrate_cache = open(link,"rb").read()
        os.remove(link)
        
    os.chdir("..")
    open(f"{link}", "wb").write(migrate_cache)

#window
window = tk.Tk()
window.title('Youtube Video Downloader')
window.geometry("800x450")

#Label 1 & 2
label = tk.Label(
    text="Hello Welcome to the Youtube video downloader",
    foreground="#580F00",
    background=None,
    width=None,
    height=None
)
label2 = tk.Label(
    text= "Type url of the video you want to download",
    foreground="#580F00",
    background=None,
    width=None,
    height=None
)
label.pack()
label2.pack()

#Entry
entry = tk.Entry(
    fg="black",
    bg="white",
    width=100
)
entry.delete(0, tk.END)


entry.pack()

#label 3
label3 = tk.Label(text="-----------------------------------")
label3.pack()

#Button
button = tk.Button(
    text="Download video",
    bg="#A99591",
    fg="black",
    command=dwl_vid
)
button.pack()

#label 5
label5 = tk.Label(text="-----------------------------------")
label5.pack()

#label 4
label4 = tk.Label(
    text= "Type url of video you want to extract into mp3",
    foreground="#580F00",
    background=None,
    width=None,
    height=None
)
label4.pack()

#Entry 1
entry1 = tk.Entry(
    fg="black",
    bg="white",
    width=100
)
entry1.delete(0, tk.END)

entry1.pack()

#label 6
label6 = tk.Label(text="-----------------------------------")
label6.pack()

#Button 1
button1 = tk.Button(
    text="Download Sound",
    bg="#A99591",
    fg="black",
    command=dwl_sound
)
button1.pack()

#label 7
label7 = tk.Label(text="-----------------------------------")
label7.pack()

#Exit Button
quitbutton = tk.Button(
    text="Exit program :D",
    command=window.quit
)
quitbutton.pack()


#Start
window.mainloop()