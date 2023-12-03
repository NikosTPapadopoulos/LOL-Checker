from tkinter import *
from PIL import ImageTk, Image
import ChampsJSON
from riotwatcher import LolWatcher, ApiError

global scenes
global lol_watcher
scenes = 1

def Scene1():
    
    m = Tk(className=' LoL Stat Checker')

    m.geometry("600x400")

    m.resizable(width=False, height=False)

    def change():
        m.destroy()
        Scene2()

    img = Image.open("Welcome.jpg")

    canvas1 = Canvas(m, width = 600,height = 400)

    canvas1.pack(fill = "both", expand = False)

    resize_img = img.resize((1280,720))

    image = ImageTk.PhotoImage(resize_img)

    canvas1.create_image(-340, -180, image=image, anchor='nw')
    
    Welcome_btn = Button(m, text= 'Click Here To Begin!', command=change)

    Welcome_btn.configure(relief=FLAT, activebackground= "#178ab4", background="#0b4559")

    Welcome_btn_window = canvas1.create_window(300, 350, anchor=N, window=Welcome_btn)

    m.mainloop()

def Scene2():
    
    n = Tk(className=' LoL Stat Checker')
    
    n.geometry("250x50")

    n.resizable(width=False, height=False)

    Username_var = StringVar()

    APIKey_var = StringVar()

    def submit1():
            
        global APIKey

        APIKey = APIKey_var.get()

        print(APIKey)

        APIKey_entry.destroy()

        APIKey_label.destroy()
        
        Username_label.grid(row=0,column=0)
        
        Username_entry.grid(row=0,column=1)
        
        btn = Button(n, text = 'Submit', command=submit2)

        btn.grid(row=1, column=1)       
           
    def submit2():

        global Username

        Username = Username_var.get()

        print(Username)

        Username_var.set("")

        take_name()
    
    def take_name():
        try:
            global my_ranked_stats
            global me
            global champMasteries
            lol_watcher = LolWatcher(str(APIKey))
            me = lol_watcher.summoner.by_name('eun1', Username)
            print(me)
            my_ranked_stats = lol_watcher.league.by_summoner('eun1', me['id']) #na to kano na pairnei mono ta ranked
            champMasteries = lol_watcher.champion_mastery.by_summoner('eun1', me['id'])
            print(my_ranked_stats)
            #print(my_ranked_stats[1]['wins']) [0] ---> Flex  [1] ---> Ranked
            #print(champMasteries)
            n.destroy()
            Scene3()
        
        except ApiError as err:
            if err.response.status_code == 404:
                Username_entry.destroy()
                Username_label.destroy()
                btn.destroy()
                global Invalid_Txt
                global Invalid_btn
                Invalid_Txt = Label(n,text = 'Invalid Name!', font=('calibre',10, 'bold'))
                Invalid_Txt.grid(row=0,column=1)
                Invalid_btn = Button(n, text='Try Again!', command=TryAgain)
                Invalid_btn.grid(row=1,column=1)
            elif err.response.status_code == 403:
                Username_entry.destroy()
                Username_label.destroy()
                btn.destroy()
                Invalid_Txt = Label(n,text = 'Invalid API Key!', font=('calibre',10, 'bold'))
                Invalid_Txt.grid(row=0,column=1)
                Invalid_btn = Button(n, text='Try Again!', command=TryAgainAPI)
                Invalid_btn.grid(row=1,column=1)
        except ValueError:
            Username_entry.destroy()
            Username_label.destroy()
            btn.destroy()
            Invalid_Txt = Label(n,text = 'Please Insert API Key!', font=('calibre',10, 'bold'))
            Invalid_Txt.grid(row=0,column=1)
            Invalid_btn = Button(n, text='Try Again!', command=TryAgainAPI)
            Invalid_btn.grid(row=1,column=1)

    def TryAgainAPI():
        n.destroy()
        Scene2()

    def TryAgain():

        Invalid_btn.destroy()
        Invalid_Txt.destroy()
        global Username_entry
        global Username_label
        Username_entry = Entry(n, textvariable = Username_var, font=('calibre',10,'normal'))
        Username_label = Label(n, text = 'Username', font=('calibre',10, 'bold'))
        btn = Button(n, text = 'Submit', command=submit2)
        Username_label.grid(row=0,column=0)
        Username_entry.grid(row=0,column=1)
        btn.grid(row=1, column=1)

    global Username_entry
    global Username_label
    global btn
    Username_label = Label(n, text = 'Username', font=('calibre',10, 'bold'))
    Username_entry = Entry(n, textvariable = Username_var, font=('calibre',10,'normal'))
    APIKey_label = Label(n, text = 'API Key', font=('calibre',10, 'bold'))
    APIKey_entry = Entry(n, textvariable = APIKey_var, font=('calibre',10,'normal'))

    APIKey_label.grid(row=0,column=0)
    APIKey_entry.grid(row=0,column=1)

    btn = Button(n, text = 'Submit', command=submit1)
    btn.grid(row=1, column=1)
    
    n.mainloop()

def Scene3():
    
    l = Tk(className= ' LoL Stat Checker')
    
    l.geometry("600x400")

    l.resizable(width=False, height=False)

    img = Image.open("Welcome.jpg")

    canvas1 = Canvas(l, width = 600,height = 400)

    canvas1.pack(fill = "both", expand = False)

    resize_img = img.resize((1280,720))

    image = ImageTk.PhotoImage(resize_img)

    canvas1.create_image(-340, -180, image=image, anchor='nw')

    firstChamp = ChampsJSON.x[str(champMasteries[0]['championId'])]

    scndChamp = ChampsJSON.x[str(champMasteries[1]['championId'])]

    thirdChamp = ChampsJSON.x[str(champMasteries[2]['championId'])]

    forthChamp = ChampsJSON.x[str(champMasteries[3]['championId'])]

    fifthChamp = ChampsJSON.x[str(champMasteries[4]['championId'])]

    try:

        Username_label_1 = Label(l, text = 'Username:' + me['name'], font=('calibre',10, 'bold'))

        Rank_label_1 = Label(l, text = 'Current SoloQ Rank: ' + my_ranked_stats[1]['tier'] + ' ' + my_ranked_stats[1]['rank'], font=('calibre',10, 'bold'))

        LP_label_1 = Label(l, text= 'LP: '+ str(my_ranked_stats[1]['leaguePoints']), font=('calibre',10, 'bold'))

        Wins_label_1 = Label(l, text= 'Wins: ' + str(my_ranked_stats[1]['wins']), font=('calibre',10, 'bold'))

        Losses_label_1 = Label(l, text= 'Losses: ' + str(my_ranked_stats[1]['losses']), font=('calibre',10, 'bold'))

        WR_label_1 = Label(l, text= 'Winrate: ' + str(int(my_ranked_stats[1]['wins'] / (my_ranked_stats[1]['losses'] + my_ranked_stats[1]['wins']) * 100)) + '%', font=('calibre',10,
                                                                                                                                                                     'bold'))

    except IndexError:
        Rank_label_1 = Label(l, text = 'Current SoloQ Rank: ' + my_ranked_stats[0]['tier'] + ' ' + my_ranked_stats[0]['rank'], font=('calibre',10, 'bold'))

        LP_label_1 = Label(l, text= 'LP: '+ str(my_ranked_stats[0]['leaguePoints']), font=('calibre',10, 'bold'))

        Wins_label_1 = Label(l, text= 'Wins: ' + str(my_ranked_stats[0]['wins']), font=('calibre',10, 'bold'))

        Losses_label_1 = Label(l, text= 'Losses: ' + str(my_ranked_stats[0]['losses']), font=('calibre',10, 'bold'))

        WR_label_1 = Label(l, text= 'Winrate: ' + str(int(my_ranked_stats[0]['wins'] / (my_ranked_stats[0]['losses'] + my_ranked_stats[0]['wins']) * 100)) + '%', font=('calibre',10,
                                                                                                                                                                     'bold'))
        
    Top_label_1 = Label(l, text='Your Highest Mastery Champions:', font=('calibre',10, 'bold'))
    
    First_label_1 = Label(l, text='1. ' + firstChamp + ' Lvl ' + str(champMasteries[0]['championLevel']) + ' ' + str(champMasteries[0]['championPoints']) + ' Points', font=
                                                                                                                                                            ('calibre',10,'bold'))

    Scnd_label_1 = Label(l, text='2. ' + scndChamp + ' Lvl ' + str(champMasteries[1]['championLevel']) + ' ' + str(champMasteries[1]['championPoints']) + ' Points', font=
                                                                                                                                                            ('calibre',10,'bold'))

    Third_label_1 = Label(l, text='3. ' + thirdChamp + ' Lvl ' + str(champMasteries[2]['championLevel']) + ' ' + str(champMasteries[2]['championPoints']) + ' Points', font=
                                                                                                                                                            ('calibre',10,'bold'))
    
    Forth_label_1 = Label(l, text='4. ' + forthChamp + ' Lvl ' + str(champMasteries[3]['championLevel']) + ' ' + str(champMasteries[3]['championPoints']) + ' Points', font=
                                                                                                                                                            ('calibre',10,'bold'))

    Fifth_label_1 = Label(l, text='5. ' + fifthChamp + ' Lvl ' + str(champMasteries[4]['championLevel']) + ' ' + str(champMasteries[4]['championPoints']) + ' Points', font=
                                                                                                                                                            ('calibre',10,'bold'))

    canvas1.create_window(25,25,window= Username_label_1, anchor='nw')
    canvas1.create_window(25,50,window= Rank_label_1, anchor='nw')
    canvas1.create_window(25,75,window= LP_label_1, anchor='nw')
    canvas1.create_window(25,100,window= Wins_label_1, anchor='nw')
    canvas1.create_window(25,125,window= Losses_label_1, anchor='nw')
    canvas1.create_window(25,150,window= WR_label_1, anchor='nw')
    canvas1.create_window(25,200,window= Top_label_1, anchor='nw')
    canvas1.create_window(25,225,window= First_label_1, anchor='nw')
    canvas1.create_window(25,250,window= Scnd_label_1, anchor='nw')
    canvas1.create_window(25,275,window= Third_label_1, anchor='nw')
    canvas1.create_window(25,300,window= Forth_label_1, anchor='nw')
    canvas1.create_window(25,325,window= Fifth_label_1, anchor='nw')

    def restart():
        l.destroy()
        Scene2()

    Restart_btn = Button(l,text='Restart',font=("calibre",10,'bold'),command=restart)
    canvas1.create_window(500,350,window=Restart_btn,anchor='se')

    l.mainloop()

Scene1()