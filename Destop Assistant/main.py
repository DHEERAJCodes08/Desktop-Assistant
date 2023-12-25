""" pip install SpeechRecognition
    pip install pyautogui 
    pip install pyaudio
    pip install pocketsphinx pyaudio"""
    
    

""" Now we will be importing this module example speech_recognition for understanding voice commands 
and subprocess which will handle the External Operations Such as Opening and Closing """
import speech_recognition as sr
import subprocess




""" We will be using the Recognizer Module so we will add it into an object variable ie recognizer """ 
recognizer = sr.Recognizer()




"""Now using the With sr.Microphone we are setting it to the Microphone for audio input"""
with sr.Microphone() as source:
    
    print("Hey Listining for the Voice Command")
    try:
        audio = recognizer.listen(source, timeout=5)
        
        """ This sends the recognized Words to google Services for translation
        insted of this we can use an Offline Ingine ie CMP Sphinx"""
        
        command = recognizer.recognize_google(audio).lower()

        print(command)

        if "open chrome" in command:
          chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
          subprocess.Popen([chrome_path])
          print("Opening Chrome")
        else:
          print("Sorry Command not recognized")
    
    except sr.WaitTimeoutError:
        print("No voice command Detected  , please try again")