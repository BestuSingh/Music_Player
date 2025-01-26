from tkinter import filedialog
from tkinter import *
import pygame
import os

root = Tk()
root.title("Music Player")
root.geometry("500 x 300")

pygame.mixer.init()

#create menubar.

menubar  = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ""
paused = False

#define the fnuctions.

def load_music():
    global current_song
    root.directory  = filedialog.askdirectory()
    
    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)
            
    for song in songs:
        songlist.insert("end",song)
        
    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]
    
def play_music():
    global current_song, paused
    
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False
        
def pause_music():
    global pause
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global current_song, paused
    
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
def prev_music():
    global current_song, paused
    
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass 

#organise menubar.

organise_menu = Menu(menubar, tearoff = False)
organise_menu.add_command(Label = 'Select Folder', command= load_music)
menubar.add_cascade(Label='Organise', menu=organise_menu)


songlist  = Listbox(root, bg ="black", fg= "white", width = 100, heigth= 15)
songlist.pack()

#import all the images of music player.

play_btn_image = PhotoImage(file= 'play.png')
pause_btn_image = PhotoImage(file= 'pause.png')
next_btn_image = PhotoImage(file= 'next.png')
prev_btn_image = PhotoImage(file= 'prev.png')

#add frame to the window.

control_frame = Frame(root)
control_frame.pack()

#add buttons to the frame and mention their respective commands.

play_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command=play_music)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0, command=pause_music)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0, command=prev_music)
prev_btn = Button(control_frame, image=prev_btn_image, borderwidth=0, command=prev_music)

#use grid to place the buttons in the same line but different columns in the frame.

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)



root.mainloop()       