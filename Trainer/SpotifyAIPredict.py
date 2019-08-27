import os, sys
os.system('clear')
import keras
import spotipy.util as util
import numpy as np
from keras.models import load_model
import h5py
import spotipy
from PIL import Image
username = "21fpmnq7rdbpn6nsjsoxrc6lq"
clientId = "080ec5426f3b47678789e27613642e9f"
clientSecret = "866a4d2d91864f8395f1c34117e32063"
redirectURI = "http://localhost/"
scope = 'playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private streaming ugc-image-upload user-follow-read user-library-modify user-read-private user-read-birthdate user-read-email user-top-read user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-recently-played'
token = util.prompt_for_user_token(username,scope,client_id=clientId,client_secret=clientSecret, redirect_uri='http://localhost/')
sp = spotipy.Spotify(auth=token)
os.system("clear")
model = load_model("model3.h5")
os.system("clear")
print('██████╗ ██╗   ██╗███████╗███████╗███████╗██████╗ ██████╗ ███████╗██████╗ ██╗ ██████╗████████╗ ██████╗ ██████╗ ')
print('██╔══██╗██║   ██║██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗')
print('██████╔╝██║   ██║███████╗███████╗█████╗  ██████╔╝██████╔╝█████╗  ██║  ██║██║██║        ██║   ██║   ██║██████╔╝')
print('██╔══██╗██║   ██║╚════██║╚════██║██╔══╝  ██╔═══╝ ██╔══██╗██╔══╝  ██║  ██║██║██║        ██║   ██║   ██║██╔══██╗')
print('██║  ██║╚██████╔╝███████║███████║███████╗██║     ██║  ██║███████╗██████╔╝██║╚██████╗   ██║   ╚██████╔╝██║  ██║')
print('╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝')
print('[!] Script by OSCARINUU and JeSuisRusse')
print('[?] What is the id of the song wou want to predict')
z = input('[*]>>')
song = sp.audio_features(tracks = z)
tab = []
tab.append([song[0]["danceability"],song[0]["loudness"]/(-60),song[0]["energy"],song[0]["valence"],song[0]["duration_ms"]/1000000,song[0]["tempo"]/1000,song[0]["speechiness"],song[0]["instrumentalness"],song[0]["acousticness"],song[0]["liveness"]])
os.system("clear")
tab = np.array(tab)
tab = tab.reshape(1,10)
p = model.predict(tab)
p = np.argmax(p)
print('██████╗ ██╗   ██╗███████╗███████╗███████╗██████╗ ██████╗ ███████╗██████╗ ██╗ ██████╗████████╗ ██████╗ ██████╗ ')
print('██╔══██╗██║   ██║██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗')
print('██████╔╝██║   ██║███████╗███████╗█████╗  ██████╔╝██████╔╝█████╗  ██║  ██║██║██║        ██║   ██║   ██║██████╔╝')
print('██╔══██╗██║   ██║╚════██║╚════██║██╔══╝  ██╔═══╝ ██╔══██╗██╔══╝  ██║  ██║██║██║        ██║   ██║   ██║██╔══██╗')
print('██║  ██║╚██████╔╝███████║███████║███████╗██║     ██║  ██║███████╗██████╔╝██║╚██████╗   ██║   ╚██████╔╝██║  ██║')
print('╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝')    
if p ==  2:
	p = 'Sad Trap'
elif p == 1:
	p = "Rock"
elif p  == 0:
	p = "Instrumental"
elif p == 3:
	p = "Hip Hop"
elif p == 4:
	p = "Rap"
elif p == 5:
	p = "Electro"
track = sp.track(z)['name']
print(track+" is " +str(p))
