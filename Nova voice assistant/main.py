import speech_recognition as sr
import requests
import pyttsx3

SPOTIFY_CLIENT_ID = '!@#$%^&*()'
SPOTIFY_CLIENT_SECRET = '!@#$%^&*()'
SPOTIFY_ACCESS_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_PLAY_URL = 'https://api.spotify.com/v1/me/player/play'

def get_access_token():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'client_credentials',
    }
    response = requests.post(SPOTIFY_ACCESS_TOKEN_URL, headers=headers, data=data, auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET))
    access_token = response.json().get('access_token')
    return access_token

def play_song(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    data = {
        'uris': ['spotify:track:7xGfFoTpQ2E7fRF5lN10tr']  
    }
    response = requests.put(SPOTIFY_PLAY_URL, headers=headers, json=data)
    print(response.status_code)

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None

def perform_action(intent):
    if "search" in intent:
        print("Performing a Google search for:", intent.replace("search", "").strip())
       
    elif "play song" in intent:
        print("Playing a song on Spotify.")
        access_token = get_access_token()
        play_song(access_token)
    elif "play video" in intent:
        print("Playing a video on YouTube.")
        
    else:
        print("Sorry, I don't understand that request.")

def main():
    print("Voice Assistant: How can I assist you today?")
    while True:
        query = recognize_speech()
        if query:
            perform_action(query)

if __name__ == "__main__":
    main()
