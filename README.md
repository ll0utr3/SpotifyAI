# 🎶 SpotifyAI
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
* Predict music style : Rock, Hip Hop, Rap, Sad Trap, Instrumental, Electro
* Requirements : Linux (Tested on Kali Linux and Ubuntu 18.04 TLS) and Python 3
## 🛠 Installation 
```
git clone https://github.com/JeSuisRusse/SpotifyIA.git
cd SpotifyIA
pip3 install -r requirements.txt
export FLASK_APP=webapp.py
export FLASK_ENV=development
python3 -m flask run --host 0.0.0.0
```
* Your browser will open
* Sign in to your spotify account
* Agree with IA
* Copy the URL that will open (http://localhost:[CODE]) **(FULL URL)**
* Paste the URL in the terminal where you launched flask and press 3 x enter
* Open a new tab and go to https://127.0.0.1:5000
* Paste the song ID (<a href=https://github.com/JeSuisRusse/SpotifyIA/wiki/ID-of-a-song>How ?</a>) or type the song name and you will have the style of the music
* If you have any error please remove the "__ pycache __" repository (without spaces) or report an Issue.
* ***Enjoy SpotifyIA***
# 🏹 Trainer
```
cd Trainer
python3 SpotifyAITrainer.py
```
* First you need to have lauched webapp.py (signing into your spotify account) before training the model.
* Follow the Instructions
* model3.h5 will be automaticaly added to the webapp folder
## 📌 Manual predictor
```
cd Trainer
python3 SpotifyAIPredict.py
```
* First you need to have lauched webapp.py (signing into your spotify account) before training the model.
* You need to use the ID of a song (<a href=https://github.com/JeSuisRusse/SpotifyIA/wiki/ID-of-a-song>How ?</a>)
# ✨ Other
* Other persons on your network can use SpotifyIA : [YOUR PRIVATE IP:5000]
* This project is free and Open Source so use it as you want 
 
