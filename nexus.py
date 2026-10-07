import pyttsx3
import webbrowser
import subprocess


def speak(text):
    nexus = pyttsx3.init()
    nexus.say(text)
    nexus.runAndWait()
    nexus.stop()


speak("Hello, Sir. I am Nexus, your personal AI assistant.")
speak("How can I assist you today, Sir?")


def handle_command(command):

    if "open" in command and "calculator" in command:
        print("Opening calculator...")
        subprocess.run("calc.exe")

    elif "open" in command and "notepad" in command:
        print("Opening notepad...")
        subprocess.run("notepad.exe")

    elif "open" in command and "youtube" in command:
        print("Opening Youtube...")
        webbrowser.open("https://www.youtube.com")

    elif "exit" in command or "quit" in command:
        print("Exiting Nexus. Goodbye!")
        speak("Exiting Nexus. Goodbye!")
        return False

    else:
        speak("I did not understand that command.")


while True:
    command = input("Type your command: ").lower()

    if handle_command(command) == False:
        break
