userInfo = { "level" : "", "name" : "", "tag" : "", "tier" : "" , "rank" : "" }
matchInfo = [
    {
        "team" : "",
        "lane" : "",
        "name" : "",
        "tag" : "",
        "puuid" : "",
        "championName" : "",
        "championLevel" : "",
        "kills" : "",
        "deaths" : "",
        "assist" : "",
        "damageToChampions" : "",
        "damageTaken" : "",
        "cs" : "" ,
        "items" :
            {
                0 : "", 1 : "",
                2 : "", 3 : "",
                4 : "", 5 : "",
                6 : ""
            },
    },
    {
        "team" : "",
        "lane" : "",
        "name" : "",
        "tag" : "",
        "puuid" : "",
        "championName" : "",
        "championLevel" : "",
        "kills" : "",
        "deaths" : "",
        "assist" : "",
        "damageToChampions" : "",
        "damageTaken" : "",
        "cs" : "" ,
        "items" :
            {
                0 : "", 1 : "",
                2 : "", 3 : "",
                4 : "", 5 : "",
                6 : ""
            },
    },
    {
        "team" : "",
        "lane" : "",
        "name" : "",
        "tag" : "",
        "puuid" : "",
        "championName" : "",
        "championLevel" : "",
        "kills" : "",
        "deaths" : "",
        "assist" : "",
        "damageToChampions" : "",
        "damageTaken" : "",
        "cs" : "" ,
        "items" :
            {
                0 : "", 1 : "",
                2 : "", 3 : "",
                4 : "", 5 : "",
                6 : ""
            },
    },
    {
        "team" : "",
        "lane" : "",
        "name" : "",
        "tag" : "",
        "puuid" : "",
        "championName" : "",
        "championLevel" : "",
        "kills" : "",
        "deaths" : "",
        "assist" : "",
        "damageToChampions" : "",
        "damageTaken" : "",
        "cs" : "" ,
        "items" :
            {
                0 : "", 1 : "",
                2 : "", 3 : "",
                4 : "", 5 : "",
                6 : ""
            },
    },
    {
        "team" : "",
        "lane" : "",
        "name" : "",
        "tag" : "",
        "puuid" : "",
        "championName" : "",
        "championLevel" : "",
        "kills" : "",
        "deaths" : "",
        "assist" : "",
        "damageToChampions" : "",
        "damageTaken" : "",
        "cs" : "" ,
        "items" :
            {
                0 : "", 1 : "",
                2 : "", 3 : "",
                4 : "", 5 : "",
                6 : ""
            },
    },
    {
        "team" : "",
        "lane" : "",
        "name" : "",
        "tag" : "",
        "puuid" : "",
        "championName" : "",
        "championLevel" : "",
        "kills" : "",
        "deaths" : "",
        "assist" : "",
        "damageToChampions" : "",
        "damageTaken" : "",
        "cs" : "" ,
        "items" :
            {
                0 : "", 1 : "",
                2 : "", 3 : "",
                4 : "", 5 : "",
                6 : ""
            },
    },
    {
        "team" : "",
        "lane" : "",
        "name" : "",
        "tag" : "",
        "puuid" : "",
        "championName" : "",
        "championLevel" : "",
        "kills" : "",
        "deaths" : "",
        "assist" : "",
        "damageToChampions" : "",
        "damageTaken" : "",
        "cs" : "" ,
        "items" :
            {
                0 : "", 1 : "",
                2 : "", 3 : "",
                4 : "", 5 : "",
                6 : ""
            },
    },
    {
        "team" : "",
        "lane" : "",
        "name" : "",
        "tag" : "",
        "puuid" : "",
        "championName" : "",
        "championLevel" : "",
        "kills" : "",
        "deaths" : "",
        "assist" : "",
        "damageToChampions" : "",
        "damageTaken" : "",
        "cs" : "" ,
        "items" :
            {
                0 : "", 1 : "",
                2 : "", 3 : "",
                4 : "", 5 : "",
                6 : ""
            },
    },
    {
        "team" : "",
        "lane" : "",
        "name" : "",
        "tag" : "",
        "puuid" : "",
        "championName" : "",
        "championLevel" : "",
        "kills" : "",
        "deaths" : "",
        "assist" : "",
        "damageToChampions" : "",
        "damageTaken" : "",
        "cs" : "" ,
        "items" :
            {
                0 : "", 1 : "",
                2 : "", 3 : "",
                4 : "", 5 : "",
                6 : ""
            },
    },
    {
        "team" : "",
        "lane" : "",
        "name" : "",
        "tag" : "",
        "puuid" : "",
        "championName" : "",
        "championLevel" : "",
        "kills" : "",
        "deaths" : "",
        "assist" : "",
        "damageToChampions" : "",
        "damageTaken" : "",
        "cs" : "" ,
        "items" :
            {
                0 : "", 1 : "",
                2 : "", 3 : "",
                4 : "", 5 : "",
                6 : ""
            },
    },
]

def user_data_set(data):
    userInfo["level"] = data["summonerLevel"]
    userInfo["name"] = data["gameName"]
    userInfo["tag"] = data["tagLine"]
    userInfo["tier"] = data["tier"]
    userInfo["rank"] = data["rank"]
    return userInfo
    
# def match_data_set(data):