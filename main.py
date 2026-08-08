import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser
import random
import subprocess
import logging
import wikipedia


# Initialize the logging configuration
os.makedirs('logs', exist_ok=True)
log_path = os.path.join('logs', 'assistant.log')

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

print("Initializing JARVIS...")