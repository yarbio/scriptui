import customtkinter as ctk


# @yarbio on discord
# hiihhihi :D
# oh dear god

win = ctk.CTk()
win.title('ScriptUI v0.28')
win.geometry('750x600+550+25')

# title

title1 = ctk.CTkLabel(win, text='scriptUI |Public| Dev Beta', font=('Segoe UI Semibold', 22,))
title1.pack(pady = 5)

# Script Hub

frame1 = ctk.CTkFrame(win, height=275, width = 300)
frame1.place(x = 30, y =100)

title2 = ctk.CTkLabel(master=frame1, text='Faded', font=('Segoe UI Semibold', 30))
title2.place(x = 105, y = 5)


frame2 = ctk.CTkFrame(master=frame1, height=275, width = 275)
frame2.place(x = 12, y = 65)



frame3 = ctk.CTkFrame(master = frame1, height = 100, width = 275)
frame3.place(x = 12, y = 65)

title3 = ctk.CTkLabel(master= frame3, text='Da Hood', font=('Segoe UI Italic', 10))
title3.place(x = 111, y = 6)

title3 = ctk.CTkLabel(master= frame3, text='Many functions, Fly, Lock, ESP, and a sleek UI.', font=('Segoe UI Semibold', 12))
title3.place(x = 13, y = 82)


frame4 = ctk.CTkFrame(master= frame1, height=75, width= 125 )
frame4.place(x = 73, y = 222)

# View function, following with it making text appear, that SHOULD be copyable.

def fadeds():
    dhflabel.configure(text= 'loadstring blalala')

button = ctk.CTkButton(master= frame4,text='View Script', command=fadeds)
button.pack(pady=4)

dhflabel= ctk.CTkLabel(root, text='')
dhflabel.pack(pady=6)
