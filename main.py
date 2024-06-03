import customtkinter as ctk

win = ctk.CTk()
win.title('First Gui')
win.geometry('500x600+550+25')

title1 = ctk.CTkLabel(win, text='Hello, Username', font=('Century Gothic', 40, 'bold'))
title1.pack(pady = 9)

frame1 = ctk.CTkFrame(win, height=225, width = 300)
frame1.place(x = 30, y =75)

title2 = ctk.CTkLabel(master=frame1, text='Topic 1', font=('Century Gothic', 30, 'bold'))
title2.place(x = 105, y = 5)

frame2 = ctk.CTkFrame(master=frame1, height=7, width = 275)
frame2.place(x = 12, y = 50)

frame3 = ctk.CTkFrame(master = frame1, height = 150, width = 275)
frame3.place(x = 12, y = 65)

entry1 = ctk.CTkLabel(master=frame3, text='I AM A TITLE FOR NOW', font=('Century Gothic', 21, 'bold'), width=255)
entry1.place(x = 10, y = 10)

title3 = ctk.CTkLabel(master= frame3, text='BEST THING EVER AM I RIGHT?', font=('Century Gothic', 14, 'italic'))
title3.place(x = 50, y = 70)

win.mainloop()