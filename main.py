import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import music_player
import client  # Import client file for OpenAI API interactions
import music_player
print(dir(music_player))  # This will list all available functions

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
        return ""

def execute_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "play" in command:
        song_name = command.replace("play", "").strip()
        if song_name:
            music_player.play_music(song_name)  # Use module.function() format
        else:
            speak("Please specify a song name.")
    elif "chat" in command:
        response = client.chat_with_openai(command.replace("chat", "").strip())
        print("Jarvis:", response)
        speak(response)
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I can't do that yet.")

def main():
    speak("Hello! I am Jarvis. How can I assist you?")
    while True:
        command = recognize_command()
        if command:
            execute_command(command)

if __name__ == "__main__":
    main()
