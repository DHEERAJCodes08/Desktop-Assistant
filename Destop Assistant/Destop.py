import pyttsx3
import speech_recognition as sr
import subprocess
import pyautogui

# for Applying the Text to Speech Recognition


def say(text):
    # Step 1: We Initalise the Speech Recognition
    engine = pyttsx3.init()

    # Step 2: We add the Text to the "text" Object
    engine.say(text)
    # Step 3: We Run
    engine.runAndWait()


recognizer = sr.Recognizer()

# Identify the installed applications on My Computer in Set Format
installed_apps = {
    "chrome": "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "C:/Windows/System32/calc.exe",
    # We can add more here
}

triggerWord = "ok ai"

with sr.Microphone() as source:
    say("Ai is Listening for the Voice Command")
    print("AI is Listening for the Voice Command")

    try:
        # recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        print("Listning...")
        command = recognizer.recognize_google(audio,language="en-in").lower()
        print(f"Recognized Command: {command}")

        if triggerWord in command:
            say("Thanks for Calling me!! ")
            print("Thanks for Calling me!! ")
            # Add PyAutoGUI code to display GIF
            # Replace with the actual path to your GIF

            while True:
                try:
                    recognizer.pause_threshold = 1
                    audio = recognizer.listen(source, timeout=10)
                    print("Recognizing...")
                    command = recognizer.recognize_google(audio,language="en-in").lower()

                    # we need to Seperate the Words in the Commands
                    # to handdle complex commands

                    commands_words = command.split()  # this seperates the Complete Command

                    # To Check if the recognized command matches an installed app
                    for app_name, app_path in installed_apps.items():
                        # f is used so we can imbbed values in the String
                        if f"open {app_name}" in command:
                            say(f"Opening {app_name.capitalize()}")
                            subprocess.Popen([app_path])

                            print(f"Opening {app_name.capitalize()}")

                        # Check if multiple apps are mentioned and open them in parallel



                        # we are Creating an array "open_multiples_apps  which store the app path of the apps that are been
                        # identified in the Command_words"
                        open_multiple_apps = [app_path for app_name, app_path in installed_apps.items() if f"open{app_name}" in commands_words]
                        if open_multiple_apps:
                            # new array "app_names" to store Application names to be Print in the Console
                            app_names = [
                                app_name for app_name, app_path in installed_apps if app_path in open_multiple_apps]
                            say(f"Opening {' , '.join(app_names)}")
                            subprocess.Popen(open_multiple_apps)
                            print(f"Opening {' , '.join(app_names)}")

                        else:
                            print("Sorry, the app name is not recognized.")

                except sr.WaitTimeoutError:
                    say("No voice command detected")
                    print("No voice command detected")

        else:
            say("Ai not Activated , please start with ok Ai  and try again")
            print("Ai not Activated , please start with ok Ai")

    except sr.UnknownValueError:
        say("closing")
        print("********************")
