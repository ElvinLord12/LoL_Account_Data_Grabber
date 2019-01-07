import requests
import json

# ---- Champion Patch 8.17.1 End Points ----
def getSingleChampionJSON(champion):
    url = 'http://ddragon.leagueoflegends.com/cdn/8.17.1/data/en_US/champion/' + champion + '.json'

    print("Single Champion Data:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data

def getChampionsJSON():
    # up to date now
    url = 'http://ddragon.leagueoflegends.com/cdn/8.17.1/data/en_US/champion.json'

    print("Full Champion List JSON:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


# ---- Match V4 End Points ----

def getMatchHistoryJSON(region, account, beginIndex, endIndex, APIKey):
    url = 'https://'+region+'.api.riotgames.com/lol/match/v4/matchlists/by-account/'+account+'&endIndex='+endIndex+'&beginIndex='+beginIndex+'&api_key='+APIKey

    print("Match History:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data

def getChampionMatchHistoryJSON(region, account, champion, beginIndex, endIndex, APIKey):
    url = 'https://'+region+'.api.riotgames.com/lol/match/v4/matchlists/by-account/'+account+'?champion='+champion+'&endIndex='+endIndex+'&beginIndex='+beginIndex+'&api_key='+APIKey

    print("Specific Champion Match History:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data

# ---- Summoner V4 End Points ----

def getSingleSummonerDataJSON(region, summoner, APIKey):
    url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner + "?api_key=" + APIKey

    print("Single Summoner:")
    # print out url for desired api
    print(url)

    # retrieve json
    got = requests.get(url)

    # turns into json format
    data = got.json()

    return data

def getMultipleSummonersDataJSON(region, summoners, APIKey):
    count = 0

    print("Multiple Summoners:")

    # list to store json data
    data_List = []

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
        data_List.append(data)

        # saves files cause it's easier to do this in this function than creating a separate list JSON file writer
        with open('JSON_Files/' + summoners[count] + 'summoners.json', 'w') as f:
            json.dump(data, f, indent=2)

        # increments list
        count += 1

    return data_List

# ---- LoL-Status V3 End Points ----

def getLoLStatusJSON(region, APIKey):
    print("Getting LoL Service Status")
    url = 'https://' + region + '.api.riotgames.com/lol/status/v3/shard-data?api_key=' + APIKey

    print(url)

    got = requests.get(url)

    data = got.json()

    return data