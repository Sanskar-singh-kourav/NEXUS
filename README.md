````markdown
# NEXUS

NEXUS is a personal assistant I'm building with Python.

I'm starting with simple computer commands and slowly adding more features as I learn. The current version can launch a few applications and websites, respond with speech, and exit cleanly from the terminal.

The long-term idea is to make NEXUS capable of handling useful tasks on my computer and eventually across my devices.

## Current version — v0.2

NEXUS currently:

- Takes commands from the terminal
- Opens Calculator
- Opens Notepad
- Opens YouTube
- Responds using text-to-speech
- Handles unknown commands with a spoken response
- Accepts `exit` and `quit` commands
- Keeps running until an exit command is given

Example:

```text
open calculator
open notepad
open youtube
hello
exit
````

Commands don't need to match the examples exactly. NEXUS currently checks for certain words in the command and then runs the corresponding action.

## How it works

The current version is intentionally simple.

```text
Command
   ↓
input()
   ↓
handle_command()
   ↓
Check command
   ↓
Run action / Speak response
```

For example:

```python
if "open" in command and "calculator" in command:
    subprocess.run("calc.exe")
```

For speech, NEXUS uses a small `speak()` function that creates a speech engine when needed:

```python
def speak(text):
    nexus = pyttsx3.init()
    nexus.say(text)
    nexus.runAndWait()
    nexus.stop()
```

So, at this point NEXUS is **not an AI assistant yet**. It is a Python program using basic logic, keyword matching, and text-to-speech.

## Setup

You need:

* Windows
* Python
* `pyttsx3`

Clone the repository:

```bash
git clone https://github.com/Sanskar-singh-kourav/NEXUS.git
cd NEXUS
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependency:

```bash
pip install -r requirements.txt
```

Run NEXUS:

```bash
python nexus.py
```

## Development

I'm building NEXUS in versions instead of trying to write the whole thing at once.

### v0.1 — Command Launcher

Completed.

The first version introduced:

* Terminal commands
* Calculator launcher
* Notepad launcher
* YouTube launcher
* Basic text-to-speech
* Keyword-based command handling

### v0.2 — Better Commands

Completed.

Added:

* `exit` and `quit` commands
* Repeated command handling
* Spoken responses for unknown commands
* A dedicated `speak()` function
* More reliable text-to-speech
* Cleaner command flow

### v0.3 — Voice Input

Next, I want to experiment with microphone input.

The goal is to let NEXUS:

* Listen to commands
* Convert speech to text
* Execute the command
* Reply using speech

### v0.4 — Assistant Features

The next stage will focus on making NEXUS more useful.

Possible features include:

* Reminders
* Timers and alarms
* Notifications
* Opening files and folders
* System information
* Command/activity history

### v0.5+ — Automation

Once the basic assistant is working, I want to experiment with computer automation.

The idea is for NEXUS to handle simple multi-step tasks instead of only opening individual programs.

Examples could include:

* Managing files
* Running scripts
* Opening several applications
* Carrying out repetitive tasks

### Later

The longer-term ideas are:

* AI/LLM integration
* Natural-language commands
* Memory and context
* Multi-step task execution
* Better computer control
* Phone/laptop communication
* Cross-device features

The version numbers and features may change as the project develops.

## Project status

**Early development**

NEXUS is mainly a learning project right now. I'm using it to learn Python, automation, and how the different parts of a personal assistant fit together.

The code will probably change a lot as I learn more.

```
```
