import requests
import json
from jsonmerge import merge
from end_points import *


def saveJSON(file, filename):
    file_json = file.json()
    name = str(filename)

    # saves json file to folder
    with open('./JSON_Files/'+name+'.json') as f:
        json.dump(file_json, f, indent=2)
    # no return
    print(filename + " .json saved")


def parse_issues_from_status(file):
    lolStatus = []
    for service in file['services']:
        for incidents in service['incidents']:
            for content in incidents['updates']:
                lolStatus.append(content['content'])

                return content['content']


def get_champions(file):
    champions = []
    for champ in file['data']:
        champions.append(champ)

    return champions


def get_champ_info(file, champion):
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


def get_base_stats(file, champion):
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
    mana regen [12]
    mana regen per lvl [13]
    critical % [14]
    critical per lvl [15]
    attack dmg [16]
    attack dmg per lvl [17]
    attack spd offset [18]
    attack spd per lvl [19]
    '''
    return base_stats



fileName = getChampionsJSON()

champions = get_champions(fileName)

print(get_champ_info(fileName,"Aatrox"))

stats = get_base_stats(fileName,"Aatrox")
print(stats[17])