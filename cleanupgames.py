from pandas import *
import warnings
import csv

warnings.simplefilter(action='ignore', category=FutureWarning)


game_folders = ["2016-17 Games", "2017-18 Games"]

game_numbers = [24811, 29347, 33846]

basicStatHeader = ["FG%", "2P%", "3P%", "FT", "FT%", "TRB", "TOV", "PF", "PTS"]
advancedStatHeader = ["TS%", "eFG%", "3PAr", "FTr", "ORB%", "DRB%", "TRB%", "STL%", "BLK%", "TOV%", "ORtg", "DRtg"]

colList = ["Game #", "Away Team", "Home Team", "Point Diff", "Home FG%", "Home 2P%", "Home 3P%", "Home FT", "Home FT%",
           "Home TRB", "Home TOV", "Home PF", "Home PTS", "Home TS%", "Home eFG%", "Home 3PAr", "Home FTr", "Home ORB%",
           "Home DRB%", "Home TRB%", "Home STL%", "Home BLK%", "Home TOV%", "Home ORtg", "Home DRtg", "Away FG%",
           "Away 2P%", "Away 3P%", "Away FT", "Away FT%", "Away TRB", "Away TOV", "Away PF", "Home PTS", "Away TS%",
           "Away eFG%", "Away 3PAr", "Away FTr", "Away ORB%", "Away DRB%", "Away TRB%", "Away STL%", "Away BLK%",
           "Away TOV%", "Away ORtg", "Away DRtg"]
writeString = ""
for col in range(len(colList)):
    writeString += colList[col]+","
with open("cleanedupgames2.csv", "a") as file:
    file.write(writeString+"\n")
    file.close()

for year in range(0, 2):
    for game in range(game_numbers[year], game_numbers[year + 1]):
        try:
            gameWriteString = str(game)+","
            FourFactors = pandas.read_csv("/Users/zcahoone/PycharmProjects/CBBModel2/Games/"+game_folders[year]+"/game"+str(game)+"/FourFactors.csv")
            HomeBasic = pandas.read_csv("/Users/zcahoone/PycharmProjects/CBBModel2/Games/"+game_folders[year]+"/game"+str(game)+"/HomeBasic.csv")
            HomeBasicTotalsIndex = int(HomeBasic[HomeBasic['Starters'] == "School Totals"].index.tolist()[0])
            HomeAdvanced = pandas.read_csv("/Users/zcahoone/PycharmProjects/CBBModel2/Games/" + game_folders[year]+"/game"+str(game)+"/HomeAdvanced.csv")
            HomeAdvancedTotalsIndex = int(HomeAdvanced[HomeAdvanced['Starters'] == "School Totals"].index.tolist()[0])
            AwayBasic = pandas.read_csv("/Users/zcahoone/PycharmProjects/CBBModel2/Games/"+game_folders[year]+"/game"+str(game)+"/AwayBasic.csv")
            AwayBasicTotalsIndex = int(AwayBasic[AwayBasic['Starters'] == "School Totals"].index.tolist()[0])
            AwayAdvanced = pandas.read_csv("/Users/zcahoone/PycharmProjects/CBBModel2/Games/" + game_folders[year]+"/game"+str(game)+"/AwayAdvanced.csv")
            AwayAdvancedTotalsIndex = int(AwayAdvanced[AwayAdvanced['Starters'] == "School Totals"].index.tolist()[0])
            gameWriteString += str(FourFactors['School'][0])+","+str(FourFactors['School'][1])+","+str(int(HomeBasic["PTS"][HomeBasicTotalsIndex]) - int(AwayBasic["PTS"][AwayBasicTotalsIndex]))+","
            for stat in basicStatHeader:
                gameWriteString += str(HomeBasic[stat][HomeBasicTotalsIndex])+","
            for stat in advancedStatHeader:
                gameWriteString += str(HomeAdvanced[stat][HomeAdvancedTotalsIndex])+","
            for stat in basicStatHeader:
                gameWriteString += str(AwayBasic[stat][AwayBasicTotalsIndex])+","
            for stat in advancedStatHeader:
                gameWriteString += str(AwayAdvanced[stat][AwayAdvancedTotalsIndex])+","
            with open("cleanedupgames2.csv", "a") as theCSV:
                theCSV.write(gameWriteString+"\n")
            print("Game #"+str(game)+" recorded.")
        except:
            print("Game #"+str(game)+" failed.")

# stats = []
# filepath = "/Users/zcahoone/PycharmProjects/CBBModel2/Games/2013-14 Games/game11447/AwayBasic.csv"
# df = pandas.read_csv(filepath)
# print(df)
# totalsIndex = int(df[df == "School Totals"].stack().index.tolist()[0][0])
# for stat in basicStatHeader:
#     stats.append(df[stat][totalsIndex])
#
# filepath = "/Users/zcahoone/P"
#
# print(basicStatHeader)
# print(stats)

