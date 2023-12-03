from tkinter import * 
from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-a99f0d70-59bc-4565-90f8-9393b9eda5bc')

m = Tk(className=' LoL Stat Checker')

m.geometry("600x400")

Username_var = StringVar()

def submit():
    global Username
    Username = Username_var.get()
    print(Username)
    Username_var.set("")
    take_name()

def take_name():
    try:
        me = lol_watcher.summoner.by_name('eun1', Username)
        print(me)
        my_ranked_stats = lol_watcher.league.by_summoner('eun1', me['id'])
        print(my_ranked_stats)
        
    except ApiError:
        Username_entry.destroy()
        Username_label.destroy()
        btn.destroy()
        global Invalid_Txt
        global Invalid_btn
        Invalid_Txt = Label(m,text = 'Invalid Name!', font=('calibre',10, 'bold'))
        Invalid_Txt.grid(row=0,column=1)
        Invalid_btn = Button(m, text='Try Again!', command=TryAgain)
        Invalid_btn.grid(row=1,column=1)

def TryAgain():

    Invalid_btn.destroy()
    Invalid_Txt.destroy()
    global Username_entry
    global Username_label
    Username_entry = Entry(m, textvariable = Username_var, font=('calibre',10,'normal'))
    Username_label = Label(m, text = 'Username', font=('calibre',10, 'bold'))
    btn = Button(m, text = 'Submit', command=submit)
    Username_label.grid(row=0,column=0)
    Username_entry.grid(row=0,column=1)
    btn.grid(row=1, column=1)

Username_label = Label(m, text = 'Username', font=('calibre',10, 'bold'))
Username_entry = Entry(m, textvariable = Username_var, font=('calibre',10,'normal'))

btn = Button(m, text = 'Submit', command=submit)
Username_label.grid(row=0,column=0)
Username_entry.grid(row=0,column=1)
btn.grid(row=1, column=1)

m.mainloop()