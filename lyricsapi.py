import pandas as pd
import requests as req

# source for the api: https://github.com/akashrchandran/spotify-lyrics-api
def get_song(spotifyID):
    api_url = "https://spotify-lyric-api.herokuapp.com/?trackid=" + spotifyID

    response = req.get(api_url)

    song = pd.json_normalize(response.json())
    
    return song

def print_lyrics(song):
    numLines = len(song["lines"][0])

    for i in range(numLines):
        print(song["lines"][0][i]["words"])

def extract_lyrics(song):
    return '\n'.join([line["words"] for line in song["lines"][0]])


if __name__ == "__main__":
    # example:
    testID = "70kBsrDIvCCboQsMTFvnVl"
    output = get_song(testID)
    print_lyrics(output)