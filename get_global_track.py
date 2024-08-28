from requests import get
import json
from spotify_env import Spotify

import csv
import urllib.request
'''
글로벌 top 50 곡을 saving

해당 리스트에 있는 내용
-앨범 제목
-앨범 커버(jpg)
-해당 엘범의 가수 이름
-노래 제목
-앨범 id
-노래 id

앨범 id로 가져올 내용
-앨범 장르

노래 id로 가져올 내용
- pre-sound(mp3)

'''
def get_global_top(headers):
    url = f"https://api.spotify.com/v1/playlists/37i9dQZEVXbNG2KDcFcKOF"
    result = get(url, headers=headers)
    datas = json.loads(result.content)['tracks']['items'][:]

    for item in datas:
        print('=============')
        album = item['track']['album']
        album_img_url = album['images'][0]['url']
        album_name = album['name']
        album_url = album['href']
        album_artists = album['artists']
        artists = ''
        for artist in album_artists:
            artists += artist['name']
            artists += ' & '
        song = item['track']
        song_name = song['name']
        song_url = song['href']
        print(album_name, artists, album_url, sep=' / ')
        print(song_name, song_url, sep=' / ')

        # save song image
        song_save_as = song_name + '.jpg'
        urllib.request.urlretrieve(album_img_url, song_save_as)

        # get genres
        print('============= genres')
        result = get(album_url, headers=headers)
        album_genres = json.loads(result.content)['genres']
        genres = ''
        for genre in album_genres:
            genres += genre
            genres += ' & '
        print(genres)
        
        # save preview song
        result = get(song_url, headers=headers)
        song_preview_url = json.loads(result.content)['preview_url']
        if song_preview_url is not None:
            sound_save_as = song_name + '.mp3'
            urllib.request.urlretrieve(song_preview_url, sound_save_as)

headers = Spotify().get_auth_header()
get_global_top(headers)
