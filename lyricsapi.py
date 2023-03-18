import pandas as pd
import requests as req

# source for the api: https://github.com/akashrchandran/spotify-lyrics-api

def get_lyrics(spotifyID):
    api_url = "https://spotify-lyric-api.herokuapp.com/?trackid=" + spotifyID

    response = req.get(api_url)

    song = pd.json_normalize(response.json())
    
    return song

def print_lyrics(song):
    numLines = len(song["lines"][0])

    for i in range(numLines):
        print(song["lines"][0][i]["words"])


# example:
testID = "70kBsrDIvCCboQsMTFvnVl"
output = get_lyrics(testID)
print_lyrics(output)