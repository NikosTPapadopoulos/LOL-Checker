#Ena app me:
#-Na vazeis to username sou kai to region kai na s dinei ta stats
#-Na exei GUI
#Gia na paro element apo to my_ranked_stats grafo my_ranked_stats[0]['wins']

import tkinter
from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-9cded8c5-680c-4fc8-a6b4-abedca8eeeb3')


available_regions = ['na is 1', 'eune is 2', 'euw is 3', 'oce is 4']
print(available_regions)
my_region = int(input('Please choose one of the following (Use numbers 1-4): '))
my_region = str(my_region)
if my_region == '1':
    my_region = 'na1'
elif my_region == '2':
    my_region = 'eun1'
    dd_my_region = 'eune'
elif my_region == '3':
    my_region = 'euw1'
elif my_region == '4':
    my_region= 'oc1'


def take_name():
    try:
        me = lol_watcher.summoner.by_name(my_region, input("Please enter a valid name: "))
        print(me)
        my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
        print(my_ranked_stats)
        
    except ApiError as err:
        if err.response.status_code == 404:
            print('Invalid name!')
            take_name()
take_name()



