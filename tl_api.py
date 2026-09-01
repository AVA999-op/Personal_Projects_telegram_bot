import requests


def get_music_info_by_artist(artist):
    url = "https://itunes.apple.com/search"
    params = {
        "term": artist,
        "media": "music",
        "entity": "song",
        "limit": 3
    }
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        return 'ERROR'
    
    else:
        response = response.json()
        songs = []
        for song in response["results"]:
            title = song["trackName"]
            genre = song["primaryGenreName"]
            album = song["collectionName"]
            address = song["trackViewUrl"]
            songs.append((title , genre , album , address))
        return songs
print(get_music_info_by_artist("Travis scott"))