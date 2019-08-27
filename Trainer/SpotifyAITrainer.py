import sys, os
import spotipy
import spotipy.util as util
import numpy as np
import keras
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical
from keras.optimizers import RMSprop, Adam
from keras.layers.advanced_activations import LeakyReLU
import h5py
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from tqdm import tqdm
os.system('clear')
song_train_id = []
x_train=[]
y_train=[]
x_test=[]
y_test=[]
username = "21fpmnq7rdbpn6nsjsoxrc6lq"
clientId = "080ec5426f3b47678789e27613642e9f"
clientSecret = "866a4d2d91864f8395f1c34117e32063"
redirectURI = "http://localhost/"
scope = 'playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private streaming ugc-image-upload user-follow-read user-library-modify user-read-private user-read-birthdate user-read-email user-top-read user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-recently-played'
token = util.prompt_for_user_token(username,scope,client_id=clientId,client_secret=clientSecret, redirect_uri='http://localhost/')
sp = spotipy.Spotify(auth=token)
os.system("clear")
print('██████╗ ██╗   ██╗███████╗███████╗███████╗████████╗██████╗  █████╗ ██╗███╗   ██╗███████╗██████╗ ')
print('██╔══██╗██║   ██║██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██╔══██╗')
print('██████╔╝██║   ██║███████╗███████╗█████╗     ██║   ██████╔╝███████║██║██╔██╗ ██║█████╗  ██████╔╝')
print('██╔══██╗██║   ██║╚════██║╚════██║██╔══╝     ██║   ██╔══██╗██╔══██║██║██║╚██╗██║██╔══╝  ██╔══██╗')
print('██║  ██║╚██████╔╝███████║███████║███████╗   ██║   ██║  ██║██║  ██║██║██║ ╚████║███████╗██║  ██║')
print('╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝')
print('[!] Script by JeSuisRusse')
print("[?] How many time you want to train the AI")
h = input("[*]>>")
################## Instrumental #################
song_train_id = []
for nb_song in tqdm(range(0,400,100)):
	if token:
		results = sp.user_playlist_tracks(user = username, playlist_id='32ggu5jXwIcy3ZYQsQpnH2', fields=None, limit=100, offset=nb_song, market=None)
		for item in tqdm(results['items']):
			track = item['track']
			song_train_id.append(sp.audio_features(tracks = [track['id']]))
			tab = sp.audio_features(tracks = [track['id']])
	for songs in tqdm(song_train_id):
		x_train.append([songs[0]["danceability"],songs[0]["loudness"]/(-60),songs[0]["energy"],songs[0]["valence"],songs[0]["duration_ms"]/1000000,songs[0]["tempo"]/1000,songs[0]["speechiness"],songs[0]["instrumentalness"],songs[0]["acousticness"],songs[0]["liveness"]])
		y_train.append(0)
################## ROCK ##########################
song_train_id = []
for nb_song in tqdm(range(0,400,100)):
	if token:
		resuzts = sp.user_playlist_tracks(user = username, playlist_id='6vGFMO56ypEBs3c5UpJSH6', fields=None, limit=100, offset=nb_song, market=None)
		for item in tqdm(results['items']):
			track = item['track']
			try:
				song_train_id.append(sp.audio_features(tracks = [track['id']]))
				tab = sp.audio_features(tracks = [track['id']])
			except:
				print(track['name'])
	for songs in tqdm(song_train_id):
		x_train.append([songs[0]["danceability"],songs[0]["loudness"]/(-60),songs[0]["energy"],songs[0]["valence"],songs[0]["duration_ms"]/1000000,songs[0]["tempo"]/1000,songs[0]["speechiness"],songs[0]["instrumentalness"],songs[0]["acousticness"],songs[0]["liveness"]])
		y_train.append(1)
################# SAD TRAP ######################
song_train_id = []
for nb_song in tqdm(range(0,400,100)):
	if token:
		results = sp.user_playlist_tracks(user = username, playlist_id='4xSH12p5L8p6NY6ty9shFq', fields=None, limit=100, offset=nb_song, market=None)
		for item in tqdm(results['items']):
			track = item['track']
			song_train_id.append(sp.audio_features(tracks = [track['id']]))
			tab = sp.audio_features(tracks = [track['id']])
	for songs in tqdm(song_train_id):
		x_train.append([songs[0]["danceability"],songs[0]["loudness"]/(-60),songs[0]["energy"],songs[0]["valence"],songs[0]["duration_ms"]/1000000,songs[0]["tempo"]/1000,songs[0]["speechiness"],songs[0]["instrumentalness"],songs[0]["acousticness"],songs[0]["liveness"]])
		y_train.append(2)
################## hip hop ######################
song_train_id = []
for nb_song in tqdm(range(0,400,100)):
	if token:
		results = sp.user_playlist_tracks(user = username, playlist_id='3EQDkqoyFRtG6kKfDLVcq5', fields=None, limit=100, offset=nb_song, market=None)
		for item in tqdm(results['items']):
			track = item['track']
			song_train_id.append(sp.audio_features(tracks = [track['id']]))
			tab = sp.audio_features(tracks = [track['id']])
	for songs in tqdm(song_train_id):
		x_train.append([songs[0]["danceability"],songs[0]["loudness"]/(-60),songs[0]["energy"],songs[0]["valence"],songs[0]["duration_ms"]/1000000,songs[0]["tempo"]/1000,songs[0]["speechiness"],songs[0]["instrumentalness"],songs[0]["acousticness"],songs[0]["liveness"]])
		y_train.append(3)
################### RAP ########################
song_train_id = []
for nb_song in tqdm(range(0,400,100)):
	if token:
		results = sp.user_playlist_tracks(user = username, playlist_id='65OXlKUb9uVo7sPtTAWKgu', fields=None, limit=100, offset=nb_song, market=None) #### Recupere id de la playlist
		for item in tqdm(results['items']):
			track = item['track']
			try:
				song_train_id.append(sp.audio_features(tracks = [track['id']]))
				tab = sp.audio_features(tracks = [track['id']])
			except:
				print(track['name'])
	for songs in tqdm(song_train_id):
		x_train.append([songs[0]["danceability"],songs[0]["loudness"]/(-60),songs[0]["energy"],songs[0]["valence"],songs[0]["duration_ms"]/1000000,songs[0]["tempo"]/1000,songs[0]["speechiness"],songs[0]["instrumentalness"],songs[0]["acousticness"],songs[0]["liveness"]]) ### recupere les parametres
		y_train.append(4)
song_train_id = []
#################### ELECTRO ###################
for nb_song in tqdm(range(0,400,100)):
	if token:
		results = sp.user_playlist_tracks(user = username, playlist_id='5VS7swN06mPSUgi8LWcFDf', fields=None, limit=100, offset=nb_song, market=None)
		for item in tqdm(results['items']): ## debut de la boucle
			track = item['track'] # declare track
			song_train_id.append(sp.audio_features(tracks = [track['id']])) ##### audio features de spotipy
			tab = sp.audio_features(tracks = [track['id']]) ## recup id
	for songs in tqdm(song_train_id): ## debut de la boucle
		x_train.append([songs[0]["danceability"],songs[0]["loudness"]/(-60),songs[0]["energy"],songs[0]["valence"],songs[0]["duration_ms"]/1000000,songs[0]["tempo"]/1000,songs[0]["speechiness"],songs[0]["instrumentalness"],songs[0]["acousticness"],songs[0]["liveness"]])
		y_train.append(5)
################## PREPARE DATA ##############
x_train = np.array(x_train)
x_train = x_train.reshape(5445,10)
y_train = to_categorical(y_train, 6)
x_train,y_train = shuffle(x_train,y_train)
x_train, x_test, y_train, y_test = train_test_split(x_train,y_train, test_size = 0.2)
################## MODEL #####################
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(10,)))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(6, activation='softmax'))
model.summary()
model.compile(loss='categorical_crossentropy',
	optimizer = Adam(),
	metrics=['accuracy'])
################## TRAIN ####################
model.fit(x_train, y_train,
	batch_size = 128,
	epochs=int(h),
	verbose=1,
	validation_data=(x_test, y_test))
#################### SAVE #######################
os.chdir('..')
model.save("model3.h5")