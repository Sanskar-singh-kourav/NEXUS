import pyttsx3
import webbrowser
import subprocess
import sounddevice as sd
import speech_recognition as sr

def speak(text):
    nexus = pyttsx3.init()
    nexus.say(text)
    nexus.runAndWait()
    nexus.stop()


speak("Hello, Sir. I am Nexus, your personal AI assistant.")
speak("How can I assist you today, Sir?")

def listen():
    sample_rate = 16000
    duration = 5

    print("\nListening... Speak your command.")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16",
        device=3
    )

    sd.wait()

    audio_data = sr.AudioData(audio.tobytes(), sample_rate, 2)
    recognizer = sr.Recognizer()

    try:
        command = recognizer.recognize_google(audio_data)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""

    except sr.RequestError:
        print("Speech recognition service unavailable. Check your internet.")
        return ""

def handle_command(command):
    if "open" in command and "calculator" in command:
        speak("Opening Calculator, Sir.")
        subprocess.Popen("calc.exe")

    elif "open" in command and "notepad" in command:
        speak("Opening Notepad, Sir.")
        subprocess.Popen("notepad.exe")

    elif "open" in command and "youtube" in command:
        speak("Opening YouTube, Sir.")
        webbrowser.open("https://www.youtube.com")

    elif "exit" in command or "quit" in command:
        speak("Exiting Nexus. Goodbye!")
        return False

    else:
        speak("I did not understand that command.")

    return True

while True:
    command = listen()
    if command == "":
        continue

    if handle_command(command) == False:
        break
