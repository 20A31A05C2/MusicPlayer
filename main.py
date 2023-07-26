from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from pygame import mixer

# colors
c01 = '#000000'  # Black
c02 = '#ADD8E6'  # Lightblue
c03 = '#808080'  # Grey
c04 = '#CFC7F8'

window = Tk()
window.title('Music Player')
window.geometry("350x255")
window.configure(bg=c01)
window.resizable(False, False)

# frames
left_frame = Frame(window, width=150, height=150, bg=c03)
left_frame.grid(column=0, row=0, padx=0, pady=0, sticky=W)

right_frame = Frame(window, width=200, height=150, bg=c02)
right_frame.grid(column=1, row=0, padx=0, pady=0, sticky=W)

down_frame = Frame(window, width=350, height=100, bg=c04)
down_frame.grid(column=0, row=1, columnspan=2)

# right Frame
listbox = Listbox(right_frame, selectmode=SINGLE, width=25,
                  height=9, bg=c02, fg=c01, font='Arial 9 bold')
listbox.grid(column=0, row=0, padx=2, pady=0, sticky=W)


w = Scrollbar(right_frame, bg=c03)
w.grid(row=0, column=1, sticky=W)


def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()


def pause_music():
    mixer.music.pause()


def continue_music():
    mixer.music.unpause()


def stop_music():
    mixer.music.stop()


def next_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index+1
    playing = songs[new_index]
    running_song['text'] = playing
    mixer.music.load(playing)
    mixer.music.play()


def prev_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index-1
    playing = songs[new_index]
    running_song['text'] = playing
    mixer.music.load(playing)
    mixer.music.play()


# Images
img_1 = Image.open('Icons/music.jpg')
img_1 = img_1.resize((150, 150))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, width=150, height=150, image=img_1, padx=0)
app_image.place(x=0, y=0)

img_2 = Image.open('Icons/play.png')
img_2 = img_2.resize((30, 30))
img_2 = ImageTk.PhotoImage(img_2)
play_button = Button(down_frame, width=30, height=30,
                     image=img_2, padx=10, font=('Ivy 10'), command=play_music)
play_button.place(x=25+35, y=35)

img_3 = Image.open('Icons/rewind.png')
img_3 = img_3.resize((30, 30))
img_3 = ImageTk.PhotoImage(img_3)
prev_button = Button(down_frame, width=30, height=30,
                     image=img_3, padx=10, font=('Ivy 10'), command=prev_music)
prev_button.place(x=25, y=35)

img_4 = Image.open('Icons/fastforward.png')
img_4 = img_4.resize((30, 30))
img_4 = ImageTk.PhotoImage(img_4)
forward_button = Button(down_frame, width=30, height=30,
                        image=img_4, padx=10, font=('Ivy 10'), command=next_music)
forward_button.place(x=60+35, y=35)

img_5 = Image.open('Icons/pause.png')
img_5 = img_5.resize((30, 30))
img_5 = ImageTk.PhotoImage(img_5)
forward_button = Button(down_frame, width=30, height=30,
                        image=img_5, padx=10, font=('Ivy 10'), command=pause_music)
forward_button.place(x=95+35, y=35)

img_6 = Image.open('Icons/resume.png')
img_6 = img_6.resize((30, 30))
img_6 = ImageTk.PhotoImage(img_6)
forward_button = Button(down_frame, width=30, height=30,
                        image=img_6, padx=10, font=('Ivy 10'), command=continue_music)
forward_button.place(x=130+35, y=35)

img_7 = Image.open('Icons/stop.png')

img_7 = img_7.resize((30, 30))
img_7 = ImageTk.PhotoImage(img_7)
forward_button = Button(down_frame, width=30, height=30,
                        image=img_7, padx=10, font=('Ivy 10'), command=stop_music)
forward_button.place(x=165+35, y=35)


running_song = Label(down_frame, text='Choose a song', font=(
    'Ivy 10'), width=44, height=1, bg='#ffffff', anchor=W)
running_song.place(x=0, y=1)


print("Select Songs  Folder")
path = filedialog.askdirectory()
os.chdir(path)
songs = os.listdir(path)


def show():
    for i in songs:
        listbox.insert(END, i)


show()

mixer.init()


window.mainloop()
