import requests
import json

# ---- Champion Patch 8.17.1 End Points ----

def get_input_champ_JSON(champion):
    url = 'http://ddragon.leagueoflegends.com/cdn/8.17.1/data/en_US/champion/' + champion + '.json'

    print("Single Champion Data:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data

def get_champs_JSON():
    # up to date now
    url = 'http://ddragon.leagueoflegends.com/cdn/8.17.1/data/en_US/champion.json'

    print("Full Champion List JSON:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


# ---- Match V4 End Points ----

def get_match_history_JSON(region, account, beginIndex, endIndex, APIKey):
    url = 'https://'+region+'.api.riotgames.com/lol/match/v4/matchlists/by-account/'+account+'&endIndex='+endIndex+'&beginIndex='+beginIndex+'&api_key='+APIKey

    print("Match History:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


def get_champ_match_history_JSON(region, account, champion, beginIndex, endIndex, APIKey):
    url = 'https://' + region + '.api.riotgames.com/lol/match/v4/matchlists/by-account/' + account + '?champion=' +champion+ '&endIndex=' + endIndex + '&beginIndex='+beginIndex+'&api_key='+APIKey

    print("Specific Champion Match History:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


# ---- Summoner V4 End Points ----

def get_single_sum_data_JSON(region, summoner, APIKey):
    url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner + "?api_key=" + APIKey

    print("Single Summoner:")
    # print out url for desired api
    print(url)

    # retrieve json
    got = requests.get(url)

    # turns into json format
    data = got.json()

    return data


def get_multi_sum_data_JSON(region, summoners, APIKey):
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

def get_status_JSON(region, APIKey):
    print("Getting LoL Service Status")
    url = 'https://' + region + '.api.riotgames.com/lol/status/v3/shard-data?api_key=' + APIKey

    print(url)

    got = requests.get(url)

    data = got.json()

    return data


# ---- Champion Rotations V3 End Points ----

def get_champ_rotation_JSON(region, APIKey):
    url = 'https://' + region + '.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=' + APIKey

    print("Getting current weeks free champion rotation:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data

# ---- Champion Master V4 End Points ----

def get_champion_mastery_by_summonerid_JSON(region,summonerID,APIKey):
    url = 'https://' + region + '.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/' + summonerID + '?api_key=' + APIKey

    print("Getting all mastery entries sorted high-low:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


def get_total_mastery_JSON(region,summonerID,APIKey):
    url = 'https://' + region + '.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/' + summonerID + '?api_key='+APIKey

    print("Getting total mastery:")
    print(url)

    got =requests.get(url)

    data = got.json()

    return data


def get_mastery_by_champion_and_summoner_id_JSON(region,summonerID,championID,APIKey):
    url = 'https://' + region + '.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/' + summonerID + '/by-champion/'+championID+'?api_key='+ APIKey

    print("Getting specific champion mastery for a player:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data

# ---- League & Queue V4 End Points ----


def get_league_data_by_summoner_JSON(region, summonerID, APIKey):
    url = "https://" + region + ".api.riotgames.com/lol/league/v4/positions/by-summoner/" + summonerID + "?api_key=" + APIKey

    print("Single Summoner League Data:")

    print(url)

    # retrieve json
    got = requests.get(url)

    data = got.json()

    return data

# more functions coming...