from tkinter import *
import pafy

m = Tk()
m.geometry("400x250")
m.title('Download from YouTube')

link = StringVar()
v = IntVar()

def dnldaudio(m, url):
    if url!='\n':
        video = pafy.new(url)
        try:
            dnd=video.getbestaudio("m4a")
        except:
            prompt.configure(text="Error")
        print(dnd)
        dnd.download(r'C:\Users\pranj\Documents\PyDnldsYT\PyAudio')
        prompt.configure(text='Audio Dnld Completed!')

def dnldvideo(m, url):
    if url!='\n':        
        video = pafy.new(url)
        print(video.title)
        try:
            dnd=video.getbest()
        except:
            prompt.configure(text="Error")
        print(dnd)
        dnd.download(r'C:\Users\pranj\Documents\PyDnldsYT\PyVideo')
        prompt.configure(text='Video Dnld Completed!')

def dnld():
    prompt.configure(text='Downloading...')
    if v.get() == 1:
        dnldaudio(m, link.get())
    else:
        dnldvideo(m, link.get())

yt = Frame(m)
yt.pack(padx=30, pady=30, fill='x', expand=True, anchor="n")

link_label = Label(yt, text="Enter Youtube Link")
link_label.pack(anchor='nw')

link_entry = Entry(yt, textvariable=link)
link_entry.pack(fill='x', expand=True)
link_entry.focus()

Radiobutton(yt, text='Audio', variable=v, value=1).pack(anchor=W)
Radiobutton(yt, text='Video', variable=v, value=2).pack(anchor=W)
v.set(1)

submit_button = Button(yt, text="Download", command=dnld)
submit_button.pack(pady=10)

prompt = Label(yt, text="")
prompt.pack(anchor='s')

mainloop()