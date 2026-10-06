import pyttsx3
import webbrowser
import subprocess
nexus = pyttsx3.init()

nexus.say("Hello, Sir. I am Nexus, your personal AI assistant.")
nexus.say("How can I assist you today, Sir?")
nexus.runAndWait()

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
        else:
            nexus.say("I'm sorry, I didn't understand that command. Please try again.")
            nexus.runAndWait()

while True:

    command = input("Type your command: ").lower()
    handle_command(command)
