import urllib.request

def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)

image_url = 'https://i.scdn.co/image/ab6761610000e5ebc4c77549095c86acb4e77b37'
image_save_as = 'image.jpg'

download_image(image_url, image_save_as)

sound_url = 'https://p.scdn.co/mp3-preview/31c4dc781b786be086f887a310e695085618ac4d?cid=fc815c404eca43fa82057df735fc6169'
sound_save_as = 'sound.mp3'
download_image(sound_url, sound_save_as)