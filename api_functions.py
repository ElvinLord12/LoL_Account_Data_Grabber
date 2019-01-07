import requests
import json
from jsonmerge import merge

def getSingleSummonerData(region, summoner, APIKey):
    url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner + "?api_key=" + APIKey

    print("Single Summoner:")
    # print out url for desired api
    print(url)

    # retrieve json
    got = requests.get(url)

    # turns into json format
    data = got.json()

    return data

def getMultipleSummonersData(region, summoners, APIKey):
    count = 0

    print("Multiple Summoners:")

    # list to store json data
    json_List = []

    for summoner in summoners:
        url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner + "?api_key=" + APIKey

        # debug console statements
        print(summoner)
        print(url)

        # retrieves data from API
        got = requests.get(url)

        # converts to json format
        data = got.json()

        # adds each json item to list
        json_List.append(data)

        # saves files cause it's easier to do this in this function than creating a separate list JSON file writer
        with open('JSON_Files/' + summoners[count] + 'summoners.json', 'w') as f:
            json.dump(data, f, indent=2)

        # increments list
        count += 1

    return json_List


def saveJSON(file,filename):
    file_json = file.json()
    name = str(filename)

    # saves json file to folder
    with open('./JSON_Files/'+name+'.json') as f:
        json.dump(file_json, f, indent=2)
    # no return
    print(filename + " .json saved")

def getLoLStatus(region, APIKey):
    print("Getting LoL Service Status")
    url = 'https://' + region + '.api.riotgames.com/lol/status/v3/shard-data?api_key=' + APIKey

    print(url)

    got = requests.get(url)

    data = got.json()

    return data

def parseIssues(file):
    lolStatus = []
    for service in file['services']:
        for incidents in service['incidents']:
            for content in incidents['updates']:
                lolStatus.append(content['content'])

                return content['content']

def getChampionList():
    url = 'http://ddragon.leagueoflegends.com/cdn/8.17.1/data/en_US/champion.json'

    print(url)

    got = requests.get(url)

    data = got.json()

    # dumps json data into
    with open('./JSON_Files/champions.json', 'w') as f:
        json.dump(data, f, indent=2)

    champions = []
    for champ in data['data']:
        champions.append(champ)

    return champions

def getSingleChampionData(champion):
    url = 'http://ddragon.leagueoflegends.com/cdn/8.17.1/data/en_US/champion/' + champion + '.json'

    # changes parameter to a str so it can be used for file name
    champName = str(champion)

    champion = requests.get(url)

    champJson = champion.json()

    with open('./JSON_Files/Champions/' + champName + '.json', 'w') as f:
        json.dump(champJson, f, indent=2)

    print("Created a json file for "+champion)
    return champJson

def getAllChampData():
    # technically out of date b/c Riot is too lazy to update it on their dev site
    url = 'http://ddragon.leagueoflegends.com/cdn/8.17.1/data/en_US/champion.json'



    got = requests.get(url)

    data = got.json()

    # dumps json data into
    with open('./JSON_Files/champions.json', 'w') as f:
        json.dump(data, f, indent=2)

    print("Created all champions json file")

    return data

def getChampionInfoArray(file,champion):
    clean_data = []

    # version [0]
    champ = file['data'][champion]
    for item in champ:
        clean_data.append(file['data'][champion][item])
    '''
    ---array indices:---
    version           [0]
    champ id          [1]
    champ key         [2]
    champ name        [3]
    champ blurb       [4]
    client difficulty [5]
    images            [6]
    class tags        [7]
    resource used     [8]
    champion stats    [7]
    '''

    print("Created an array of "+champion+"'s info")

    return clean_data

def getBaseStats(file,champion):
    base_stats = []

    for stat in file['data'][champion]['stats']:
        base_stats.append(file['data'][champion]['stats'][stat])

    print("Creating array of base stats")
    '''
    ---array indices:---
    hp [0]
    hp per lvl [1]
    mana [2]
    mana per lvl [3]
    movespeed [4]
    armor [5]
    armor per lvl [6]
    magic resist [7]
    mr per lvl [8]
    range [9]
    hp regen [10]
    hp regen per lvl [11]
    
    '''
    return base_stats




champions = getChampionList()

fileName = getAllChampData()

print(getChampionInfoArray(fileName,"Aatrox"))

getBaseStats(fileName,"Zoe")