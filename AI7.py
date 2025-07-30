import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import imaplib
import email
import requests
import random
import subprocess

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speed
engine.setProperty('volume', 1.0)  # Adjust volume


def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()


def greet_user():
    """Greet the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        greeting = "Good morning!"
    elif 12 <= hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    speak(f"{greeting} I am Echo, THE AI voice assistant. What can I help you with ?")


def take_command():
    """Listen to the user's voice and return the command."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {command}")
    except Exception as e:
        print("Sorry, I didn't catch that. Please say that again.")
        return None
    return command.lower()


def read_email():
    """Read the latest email from your inbox."""
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login("nisargpandya3007@gmail.com", "verna1128")  # Replace with your credentials
        mail.select("inbox")

        _, search_data = mail.search(None, "ALL")
        mail_ids = search_data[0].split()
        latest_email_id = mail_ids[-1]

        _, data = mail.fetch(latest_email_id, "(RFC822)")
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = msg["subject"]
                from_email = msg["from"]
                speak(f"You have an email from {from_email}. The subject is {subject}.")
                print(f"From: {from_email}\nSubject: {subject}")
                break

        mail.logout()
    except Exception as e:
        speak("I couldn't access your email. Please check your login credentials or internet connection.")
        print(e)


def get_weather(city):
    """Fetch the weather for a given city."""
    try:
        api_key = "your_api_key"  # Replace with your OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            speak(f"The weather in {city} is {weather} with a temperature of {temp}°C.")
        else:
            speak("I couldn't fetch the weather. Please check the city name or your internet connection.")
    except Exception as e:
        speak("There was an error fetching the weather information.")
        print(e)


def tell_joke():
    """Tell a random joke."""
    jokes = [
        "Why don’t skeletons fight each other? Because they don’t have the guts!",
        "What do you call cheese that isn't yours? Nacho cheese.",
        "Why don’t scientists trust atoms? Because they make up everything!"
    ]
    speak(random.choice(jokes))

import subprocess

def execute_command(command):
    command = command.lower().strip()

    if any(word in command for word in ["shutdown", "shut down", "turn off", "turnoff"]):
        speak("Shutting down the system in 5 seconds.")
        subprocess.run(["shutdown", "/s", "/f", "/t", "5"], shell=True)
        print("Received command:", command)
    

    elif "restart" in command:
        speak("Restarting the system in 5 seconds.")
        os.system("shutdown /r /f /t 5")  # Force restart in 5 seconds

    else:
        speak("I am sorry, I cannot do that yet. Please try something else.")


def execute_command(command):
    """Execute the given command."""
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open twitter" in command:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")

    elif "search" in command:
        if "on youtube" in command:
            query = command.replace("search on youtube for", "").strip()
            speak(f"Searching YouTube for {query}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        elif "on google" in command:
            query = command.replace("search on google for", "").strip()
            speak(f"Searching Google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        else:
            speak("Please specify where to search, like 'search on YouTube' or 'search on Google'.")

    elif "read my email" in command or "latest email" in command:
        speak("Let me check your inbox.")
        read_email()

    elif "what's the weather" in command or "weather in" in command:
        city = command.replace("what's the weather in", "").replace("weather in", "").strip()
        get_weather(city)

    elif "tell me a joke" in command or "make me laugh" in command:
        tell_joke()

    elif "play music" in command:
        speak("Playing music")
        music_dir = "C:\\Users\\YourUsername\\Music"  # Replace with your music directory
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, random.choice(songs)))

    elif "shut down" in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /f /t 1")

    elif "restart" in command:
        speak("Restarting the system.")
        os.system("shutdown /r /t 1")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {today}")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad.exe")

    elif "exit" in command or "quit" in command:
        speak("Until we meet again. May your day be excellent!")
        exit()

    else:
        speak("I am sorry, I cannot do that yet. Please try something else.")


if __name__ == "__main__":
    greet_user()
    while True:
        user_command = take_command()
        if user_command:
            execute_command(user_command)
        else:
            # Handle the case where user_command is empty or invalid
            pass