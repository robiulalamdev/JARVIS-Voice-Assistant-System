# JARVIS Voice Assistant System

This project is a simple voice assistant inspired by JARVIS. It listens to your voice, recognizes speech, and can answer basic requests such as searching Wikipedia and opening popular websites.

## Features

- Greets the user when the program starts
- Recognizes voice input using the microphone
- Searches Wikipedia for information
- Opens YouTube, Google, and Stack Overflow in the browser
- Exits the assistant when you say words like "close", "exit", "quit", "stop", or "bye"

## Requirements

- Python 3.8 or newer
- A working microphone
- Internet connection for speech recognition and Wikipedia lookup

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd JARVIS-Voice-Assistant-System
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. On macOS, if `pyaudio` installation fails, install PortAudio first:
   ```bash
   brew install portaudio
   ```

## How to Use

Run the assistant:

```bash
python main.py
```

Once it starts, speak clearly into your microphone. Example commands:

- "Wikipedia, tell me about Python"
- "Open Google"
- "Open YouTube"
- "Open Stack Overflow"
- "Bye"

The assistant will respond with voice and print messages in the terminal.

## Notes

- The program writes logs to the `logs/assistant.log` file.
- If speech recognition fails, make sure your microphone is connected and allowed to access your system.
- If the assistant cannot understand you, speak a little slower and more clearly.
