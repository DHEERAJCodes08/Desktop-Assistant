import speech_recognition as sr
import subprocess

recognizer = sr.Recognizer()

installed_apps = {
    "chrome": "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "C:/Windows/System32/calc.exe",
    # Add more applications here
}



# Variable to track whether the program should continue running
running = True
while running:
 with sr.Microphone() as source:
    print("Listening for the Voice Command")
    try:

                
                    audio = recognizer.listen(source, timeout=10)
                    command = recognizer.recognize_google(audio).lower()

                    commands_words = command.split()

                    for app_name, app_path in installed_apps.items():
                        if f"open {app_name}" in commands_words:
                            subprocess.Popen([app_path])
                            print(f"Opening {app_name.capitalize()}")

                    open_multiple_apps = [app_path for app_name, app_path in installed_apps.items(
                    ) if f"open {app_name}" in commands_words]
                    if open_multiple_apps:
                        subprocess.Popen(open_multiple_apps)
                        app_names = [
                            app_name for app_name, app_path in installed_apps.items() if app_path in open_multiple_apps]
                        print(f"Opening {' , '.join(app_names)}")

                    # Check if the "Stop" command is given
                    if "stop" in commands_words:
                        print("Stopping the AI program.")
                        break

    except sr.UnknownValueError:
        print("********************")
