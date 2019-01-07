import requests
import json
from jsonmerge import merge
from tkinter import *


def getSingleSummonerData(region, summoner, APIKey):
    url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner + "?api_key=" + APIKey

    print("Single Summoner:")
    # print out url for desired api
    print(url)

    # retrieve json
    got = requests.get(url)

    # turns into json format
    data = got.json()

    with open('./JSON_Files/singleSummoner.json', 'w') as f:
        json.dump(data, f, indent=2)

    return data


def getMultipleSummonersData(region, summoners, APIKey):
    count = 0
    print("Multiple Summoners:")
    for summoner in summoners:
        url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner + "?api_key=" + APIKey

        print(summoner)
        print(url)

        got = requests.get(url)

        data = got.json()

        with open('JSON_Files/'+ summoners[count]+'summoners.json', 'w') as f:
            json.dump(data, f, indent=2)

        count += 1


def getLeagueData(region, summonerID, APIKey):
    url = "https://" + region + ".api.riotgames.com/lol/league/v4/positions/by-summoner/" + summonerID + "?api_key=" + APIKey

    print("Single Summoner League Data:")

    print(url)

    # retrieve json
    got = requests.get(url)

    data = got.json()

    with open('./JSON_Files/singleLeague.json', 'w') as f:
        json.dump(data, f, indent=2)

    return data


def parseLeagueData(data, league):
    name = data[league]['queueType']
    data = [data[league]['queueType'], data[league]['leagueName'], data[league]['tier'], data[league]['rank'],
              data[league]['leaguePoints'], data[league]['wins'], data[league]['losses']]

    return data

def getLoLIssues(region, APIKey):
    print("Getting LoL Service Status")
    url = 'https://'+ region + '.api.riotgames.com/lol/status/v3/shard-data?api_key=' + APIKey

    print(url)

    status = requests.get(url)

    data = status.json()

    with open('./JSON_Files/leagueStatus.json', 'w') as f:
        json.dump(data, f, indent=2)

    with open('./JSON_Files/leagueStatus.json') as f:
        cleanData = json.load(f)

    lolStatus = []
    for service in cleanData['services']:
        for incidents in service['incidents']:
            for content in incidents['updates']:
                lolStatus.append(content['content'])

                print(content['content'])




    return lolStatus

def getChampionsList():
    url = 'http://ddragon.leagueoflegends.com/cdn/8.17.1/data/en_US/champion.json'

    champs = requests.get(url)

    championsData = champs.json()

    with open('./JSON_Files/champions.json','w') as f:
        json.dump(championsData, f, indent=2)

    champions = []
    for champ in championsData['data']:
        champions.append(champ)

    return champions

def getChampionData(champion):
    url = 'http://ddragon.leagueoflegends.com/cdn/8.17.1/data/en_US/champion/' + champion + '.json'

    # changes parameter to a str so it can be used for file name
    champName = str(champion)

    champion = requests.get(url)

    champJson = champion.json()


    with open('./JSON_Files/Champions/'+champName+'.json','w') as f:
        json.dump(champJson, f, indent=2)

    return 0

def getChampionKey(champion):


    with open('JSON_Files/champions.json') as f:
        champions = json.load(f)


    #for champ in champions['data']:



def main():
    print("\nWelcome To My Riot API Fucking Around")

    # In Order: North America, Europe West, Europe Nordic East, Japan, Oceania, Brazil, Korea, Russia,
    # Latin America North, Latin America South, Turkey, Public Beta Environment

    # setup for potential GUI
    regions = ['na1', 'euw1', 'eun1', 'jp1', 'oc1', 'br1', 'kr', 'ru', 'la1', 'la2', 'tr1', 'pbe1']
    print(regions[0:len(regions)])

    # gets all the champion names in a list of strings
    championNames = getChampionsList()
    print(championNames)

    print("Enter your API Key:")
    APIKey = input()

    summoners = ['DrunkenSkarl', 'iRoboticDoom', 'PrinceDavid']
    summoner = 'DrunkenSkarl'

    sumInfo = getSingleSummonerData(regions[0], summoner, APIKey)

    print(sumInfo)

    sumID = sumInfo['id']

    print(sumID)

    # grabs all summoner data for every summoner in the list

    getMultipleSummonersData(regions[0], summoners, APIKey)
    print(getSingleSummonerData(regions[0], summoner, APIKey))

    # grabs league data for summoner (DrunkenSkarl)
    testData = (getLeagueData(regions[0], sumID, APIKey))

    league = parseLeagueData(testData, 0)
    print(league[0:len(league)])
    league1 = parseLeagueData(testData, 1)
    print(league1[0:len(league)])
    league2 = parseLeagueData(testData, 2)
    print(league2[0:len(league)])

    print(getLoLIssues(regions[0], APIKey))

    # for name in championNames:
        # getChampionData(str(name))

# window tests

    #root = Tk("Window")
    #theLabel = Label(root, text="This is a window")
    #theLabel.pack()
    #root.mainloop()


if __name__ == "__main__":
    main()
