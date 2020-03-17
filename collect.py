# Program to collect per game stats for all players in the NBA during the 2015 - 2019 seasons from basketballreference.com organized by team
# Stores the stats locally in ./Team_Data/TeamName_SeasonYear.csv

# Dependencies
import pandas as pd
from bs4 import BeautifulSoup
import requests


seasons = ["2015","2016","2017","2018","2019"]
stats_per_season = [] # Initialize list to store pandas dataframes for every active player's stats each season
for season in seasons:
    # Gets the html document in string format
    source = requests.get("https://www.basketball-reference.com/leagues/NBA_"+ season +"_per_game.html").text

    # Represents the document as a nested data structure
    soup = BeautifulSoup(source, 'lxml')

    # Pulls the table containing the player stats from the document, then converts it to a dataframe
    player_info = soup.select("#per_game_stats")
    df = pd.read_html(str(player_info))[0]

    stats_per_season.append(df)

# Initiate a dictionary of dictionaries for each team. These will store the dataframes for each year
teams = {"PHI":{} ,"MIL":{} ,"CHI":{} ,"CLE":{} ,"BOS":{} ,"LAC":{} ,"MEM":{} ,"ATL":{} ,"MIA":{} ,"CHO":{} ,"UTA":{} ,"SAC":{} ,"NYK":{} ,"LAL":{} ,"ORL":{} ,"DAL":{} ,"BRK":{} ,"DEN":{} ,"IND":{} ,"NOP":{} ,"DET":{} ,"TOR":{} ,"HOU":{} ,"SAS":{} ,"PHO":{} ,"OKC":{} ,"MIN":{} ,"POR":{} ,"GSW":{} ,"WAS":{}}

for team in teams:
    count = 0 # Used for iterating through the seasons list. 0 -> 2015 ... 4 -> 2019
    for season in seasons:
        df = stats_per_season[count]

        # Pulls stats for players whose team (Tm) match the current team
        mask = df["Tm"] == team
        teams[team][season] = df[mask]


        count += 1
        teams[team][season].to_csv("./Team_Data/"+team+"_"+season+".csv",encoding='utf-8',sep='\t',index=False)

    # print(teams[x]["2015"].head(3))

