import requests
import json

# ---- Static Data ---- {

def get_icons_JSON():
    url = 'http://ddragon.leagueoflegends.com/cdn/8.24.1/data/en_US/profileicon.json'

    print("Profile Icons:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


def get_items_JSON():
    url = 'http://ddragon.leagueoflegends.com/cdn/8.24.1/data/en_US/item.json'

    print("Items Data:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


def get_sum_spells_JSON():
    url = 'http://ddragon.leagueoflegends.com/cdn/8.24.1/data/en_US/summoner.json'

    print("Summoner Spells:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


def get_version_JSON():
    url = 'https://ddragon.leagueoflegends.com/api/versions.json'

    print("Versions:")
    print(url)

    got = requests.get(url)

    data = got.json()

    with open('./JSON_Files/versions.json', 'w') as f:
        json.dump(data,f,indent=2)

    # latest version
    version = data[0]



    return data
# ---- Champion Patch 8.17.1 End Points ----

def get_input_champ_JSON(champion):
    url = 'http://ddragon.leagueoflegends.com/cdn/8.24.1/data/en_US/champion/' + champion + '.json'

    print("Single Champion Data:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data

def get_champs_JSON():
    # up to date now
    url = 'http://ddragon.leagueoflegends.com/cdn/8.24.1/data/en_US/champion.json'

    print("Full Champion List JSON:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


# ---- Match V4 End Points ----

def get_match_history_JSON(region, account, beginIndex, endIndex, APIKey):
    url = 'https://'+region+'.api.riotgames.com/lol/match/v4/matchlists/by-account/'+account+'?endIndex='+str(endIndex)+'&beginIndex='+str(beginIndex)+'&api_key='+APIKey

    print("Match History:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


def get_champ_match_history_JSON(region, account, champion, beginIndex, endIndex, APIKey):
    url = 'https://' + region + '.api.riotgames.com/lol/match/v4/matchlists/by-account/' + account + '?champion=' +str(champion)+ '&endIndex=' + str(endIndex) + '&beginIndex='+str(beginIndex)+'&api_key='+APIKey

    print("Specific Champion Match History:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


def get_match_JSON(region, matchID, APIKey):
    url = 'https://'+ region + '.api.riotgames.com/lol/match/v4/matches/'+matchID+'?api_key='+APIKey

    print("Single Match")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


def get_match_timeline_JSON(region, matchID, APIKey):
    url = 'https://'+region+ '.api.riotgames.com/lol/match/v4/timelines/by-match/'+matchID+'?api_key='+APIKey

    print("Timeline of Match:")
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


def get_sum_by_account_id_JSON(region, accountID, APIKey):
    url = 'https://'+region+'.api.riotgames.com/lol/summoner/v4/summoners/by-account/'+accountID+'?api_key='+APIKey

    print("Single Account:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


def get_multi_account_data_JSON(region, accountIDs, APIKey):
    count = 0

    print("Multiple Accounts:")

    # list to store json data
    data_List = []

    for account in accountIDs:
        url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-account/" + account + "?api_key=" + APIKey

        # debug console statements
        print(account)
        print(url)

        # retrieves data from API
        got = requests.get(url)

        # converts to json format
        data = got.json()

        # adds each json item to list
        data_List.append(data)

        # saves files cause it's easier to do this in this function than creating a separate list JSON file writer
        with open('JSON_Files/' + accountIDs[count] + '.json', 'w') as f:
            json.dump(data, f, indent=2)

        # increments list
        count += 1

    return data_List

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


# ---- Spectator Data V4 End Points ----

def get_spectator_JSON(region,summonerID,APIKey):
    url = 'https://'+region+'.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/'+summonerID+'api_key='+APIKey

    print("Getting active spectator data:")
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


def get_challenger_JSON(region, queueName,APIKey):
    url = 'https://'+region+'.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/'+queueName+'?api_key='+APIKey

    print("Challenger League:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


def get_grandmaster_JSON(region, queueName, APIKey):
    url = 'https://'+region+'.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/'+queueName+'?api_key='+APIKey

    print("Grand-Master League:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data


def get_master_JSON(region, queueName, APIKey):
    url = 'https://' + region + '.api.riotgames.com/lol/league/v4/masterleagues/by-queue/' + queueName + '?api_key=' + APIKey

    print("Masters League:")
    print(url)

    got = requests.get(url)

    data = got.json()

    return data




get_version_JSON()

accounts = ["WhFFc9KhU8OuPhShQCc-YLMklbgZ97fsZOcY4ahUm4OXaW4","J0Go30yeOcsPshID6tpm8mFf8zOCCE9w8IueGKwjoqd7SZ0","DansRpqXLigB3Q2kAbp4jI1ZfBLIApaJRmiWVUrrZfrOHVnrGltfZW9M"]

api = "RGAPI-55f82a01-d2ec-4092-93da-6829172a436d"
# get_multi_account_data_JSON("na1",accounts,api)
account = "WhFFc9KhU8OuPhShQCc-YLMklbgZ97fsZOcY4ahUm4OXaW4"

print(get_match_history_JSON("na1", account,0,100,api))
print(get_champ_match_history_JSON("na1",account,516,0,100,api))
print(get_single_sum_data_JSON("na1","DrunkenSkarl",api))
# more functions coming...