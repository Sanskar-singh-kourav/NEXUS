# NEXUS

Nexus is my personal AI assistant project, built with Python. I'm developing it step by step to understand how voice assistants work.

## Current Features — v0.3

* Speaks a startup greeting.
* Listens to voice commands through a microphone.
* Recognizes speech using Google's online speech recognition service.
* Opens Calculator and Notepad.
* Opens YouTube in a web browser.
* Exits when told to quit.

## Technologies Used

* Python
* pyttsx3
* SpeechRecognition
* sounddevice
* NumPy

## How to Run

1. Install Python.

2. Install the required packages:

   `pip install -r requirements.txt`

3. Run the program:

   `python nexus.py`

## Current Limitations

* Records audio for five seconds per command.
* Requires an internet connection for Google's online speech recognition.
* Uses a configured microphone device index, which may need changing on another computer.
* Understands only a small set of predefined commands.

## Future Plans

* Improve voice recognition and listening.
* Add reminders and timers.
* Automate repetitive computer tasks.
* Explore ways to connect Nexus with other devices.

This project is a learning journey. I'll add features as I build and understand them.
