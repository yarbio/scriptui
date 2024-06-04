import customtkinter as ctk
import datetime as dtm

current_date = dtm.datetime.now()
date1 = (current_date.strftime('%y/%m/%d                               %H:%M'))

win = ctk.CTk()
win.title('Tasks')
win.geometry('750x600+550+25')

title1 = ctk.CTkLabel(win, text='Tasks', font=('Century Gothic', 40, 'bold'))
title1.pack(pady = 5)

dropdownitems = ['Dahood', 'MM2', 'Universal']
dropdown1 = ctk.CTkComboBox(win, values=dropdownitems, dropdown_text_color='#BFA0FF', text_color='#BFA0FF', border_color='#BFA0FF', dropdown_font=('Century Gothic', 20, 'bold'), font=('Century Gothic', 20, 'bold'))
dropdown1.place(x = 30, y = 65)

frame1 = ctk.CTkFrame(win, height=225, width = 300)
frame1.place(x = 30, y =100)

title2 = ctk.CTkLabel(master=frame1, text='Topic 1', font=('Century Gothic', 30, 'bold'))
title2.place(x = 105, y = 5)

frame2 = ctk.CTkFrame(master=frame1, height=7, width = 275)
frame2.place(x = 12, y = 50)

frame3 = ctk.CTkFrame(master = frame1, height = 150, width = 275)
frame3.place(x = 12, y = 65)

entry1 = ctk.CTkEntry(master=frame3, placeholder_text='Title', font=('Century Gothic', 22, 'bold'), width=255)
entry1.place(x = 10, y = 10)

title3 = ctk.CTkLabel(master= frame3, text='| Description |', font=('Century Gothic', 22, 'bold'))
title3.place(x = 50, y = 55)

textbox1 = ctk.CTkTextbox(master= frame3, font=('Century Gothic', 22, 'bold'), width=250,  height=25)
textbox1.place(x = 10, y = 100)

title4 = ctk.CTkLabel(win, text=date1, font=('Courier', 28, 'bold'))
title4.place(x = 10, y = 560)

win.mainloop()