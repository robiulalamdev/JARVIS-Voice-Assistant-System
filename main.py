import datetime
import logging
import os
import random
import re
import subprocess
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia

# Initialize logging configuration
os.makedirs('logs', exist_ok=True)
log_path = os.path.join('logs', 'assistant.log')

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)


def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-us')
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"API request error: {e}")
        return None
    except Exception as e:
        logging.error(f"Speech recognition error: {e}")
        return None


def clean_wikipedia_query(query):
    # Remove filler phrases to get the core topic
    patterns = [
        r"can you please tell me about",
        r"tell me about",
        r"according to wikipedia",
        r"wikipedia",
        r"who is",
        r"what is",
        r"search for",
    ]
    cleaned = query.lower()
    for pattern in patterns:
        cleaned = re.sub(pattern, "", cleaned)
    return cleaned.strip()


def greetings():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How can I help you today?")


if __name__ == "__main__":
    greetings()

    while True:
        query = recognize_speech()

        if not query:
            continue

        query = query.lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            search_query = clean_wikipedia_query(query)

            try:
                results = wikipedia.summary(search_query, sentences=2)
                speak("According to Wikipedia:")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                logging.warning(f"Disambiguation error for '{search_query}': {e}")
                speak("There were multiple results for that topic. Please be more specific.")
            except wikipedia.exceptions.PageError:
                logging.warning(f"Page not found for '{search_query}'")
                speak("I couldn't find a Wikipedia page matching that topic.")
            except Exception as e:
                logging.error(f"Wikipedia error: {e}")
                speak("Sorry, something went wrong while searching Wikipedia.")

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "open stackoverflow" in query:
            speak("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com")

        elif any(exit_cmd in query for exit_cmd in ["close", "exit", "quit", "stop", "bye"]):
            speak("Goodbye!")
            break