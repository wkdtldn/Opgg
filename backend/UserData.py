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
    userInfo["level"] = data[1]["summonerLevel"]
    userInfo["name"] = data[0]["gameName"]
    userInfo["tag"] = data[0]["tagLine"]
    userInfo["tier"] = data[2][0]["tier"]
    userInfo["rank"] = data[2][0]["rank"]
    return userInfo
    
def match_data_set(data):
    print(data)