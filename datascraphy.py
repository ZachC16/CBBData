import requests
from bs4 import BeautifulSoup
from pandas import *
import os
from time import sleep

gameNum = 2108
fileNames = ["AwayBasic.csv","AwayAdvanced.csv","HomeBasic.csv","HomeAdvanced.csv"]

for year in range (2011,2020):
    for month in range (1,13):
        for day in range (1,32):
            print("Starting games on "+str(month)+"/"+str(day)+"/"+str(year)+".")
            if len(str(day)) == 1:
                fixedDay = "0"+str(day)
            else:
                fixedDay = day
            if len(str(month)) == 1:
                fixedMonth = "0"+str(month)
            else:
                fixedMonth = month
            try:
                site = requests.get("https://www.sports-reference.com/cbb/boxscores/index.cgi?month="+str(fixedMonth)+"&day="+str(fixedDay)+"&year="+str(year))
            except:
                sleep(20)
                break
            soup = BeautifulSoup(site.content, 'html.parser')
            linkTds = soup.find_all('td', class_='gamelink')
            links = []
            if (month == 1) or (month == 2 and day in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]) and year == 2011:
                print("Skipping, already got these games.")
                break
            for link in range (len(linkTds)):
                aHref = linkTds[link].find('a')
                try:
                    links.append("https://www.sports-reference.com"+str(aHref['href']))
                except:
                    print("No games on "+str(month)+"/"+str(day)+"/"+str(year)+". Skipping.")
                    break


            for game in range(len(links)):
                gameNum += 1
                print("Starting game #"+str(gameNum))
                gamefile = "game" + str(gameNum)
                os.mkdir("/Users/zcahoone/PycharmProjects/CBBModel2/Games/game"+str(gameNum))
                try:
                    theGame = requests.get(links[game])
                except:
                    print("Connection failed. Skipping day.")
                    break
                soup = BeautifulSoup(theGame.text.replace("<!--","").replace("-->",""), 'html.parser')
                tables = soup.find_all('table')
                finalTables = tables[-5:]
                dfs = list()
                for table2 in range (len(finalTables)):
                    if len(dfs) == 0:
                        dataframe = pandas.read_html(str(finalTables[table2]), header=1)
                    elif len(dfs) != 0:
                        dataframe = pandas.read_html(str(finalTables[table2]), header=1)
                    dfs.append(dataframe)
                for table in range(0,5):
                    df = dfs[table]
                    if table != 0:
                        open("/Users/zcahoone/PycharmProjects/CBBModel2/Games/"+str(gamefile)+"/"+str(fileNames[table-1]), "w+").close()
                        df[0].to_csv("/Users/zcahoone/PycharmProjects/CBBModel2/Games/"+str(gamefile)+"/"+str(fileNames[table-1]), mode="w+")
                    else:
                        open("/Users/zcahoone/PycharmProjects/CBBModel2/Games/"+str(gamefile)+"/"+"FourFactors.csv", "w+").close()
                        df[0].to_csv("/Users/zcahoone/PycharmProjects/CBBModel2/Games/"+str(gamefile)+"/"+"FourFactors.csv", mode="w+")