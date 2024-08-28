'''
https://developer.spotify.com/documentation/web-api/reference/get-an-album
pre-sound(mp3)
앨범 제목
앨범 커버(jpg)
노래 제목
가수 이름
앨범 장르
'''

'''
python 3.10
pip install python-dotenv
pip install requests

'''

from requests import get
import json
from spotify_env import Spotify


def search_for_artist(headers, artist_name):
    url = "https://api.spotify.com/v1/search"
    query = f"?q={artist_name}&type=artist&limit=1"
    
    query_url = url + query
    result = get(query_url, headers=headers)
    print(result)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None
    return json_result[0]

def get_songs_by_artist(headers, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

def get_global_top(headers):
    url = f"https://api.spotify.com/v1/playlists/37i9dQZEVXbNG2KDcFcKOF"
    result = get(url, headers=headers)
    print(json.loads(result.content))

# headers = {'Authorization': 'Bearer BQCo1bq3_qU8EAQMVszTi28cJEqIKzjGZsrEFyS_nkkDzGA5fj7eIaXSBF-atDK3xuegRgR_TOroTVBOxW4ynZXANXsOX_wJ79jhMx5jqUVKO_bLjUA'}
headers = Spotify().get_auth_header()
print(headers)
result = search_for_artist(headers, "iu")
print(result)
# result = search_for_artist(headers, "ateez")
# print(result)
# artist_id = result["id"]
# songs = get_songs_by_artist(headers, artist_id)

# for idx, song in enumerate(songs):
#     print(f"{idx+1}. {song['name']}")

# get_global_top(headers)
