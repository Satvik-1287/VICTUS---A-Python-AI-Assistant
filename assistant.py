# Here's my Victus (Virtual Intelligent Companion & Task-Undertaking Software)

import pyttsx3
import speech_recognition as sr
from plyer import notification
import datetime
import wikipedia
import webbrowser
import os
import sys
import speedtest
import psutil
import random
import string
import pyjokes
import time
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


file_path = 'password.txt'

try:
    with open(file_path, 'r') as file:
        passkey = file.read()

except FileNotFoundError:
    print(f"File '{file_path}' not found.")

except Exception as e:
    print(f"An error occurred: {str(e)}")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def stop_program():
    speak("Stopping the program...")
    print("Stopping the program...")
    sys.exit(0)   

def set_password(new_password):
    with open("password.txt", "w") as file:
        file.write(new_password)

def change_password():
    new_password = input("Enter the new password: ")
    set_password(new_password)
    print("Password changed successfully!")

def check_password(password):
    with open("password.txt", "r") as file:
        saved_password = file.read().strip()
    return password == saved_password

def generate_random_joke():
    joke = pyjokes.get_joke()
    return joke

def telljoke():
    joke = generate_random_joke()
    speak(joke + "\n")     
    print(joke + "\n")     

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon='icon.ico',
        timeout=10
    )

def notifier():
    notification_title = "Victus AI"
    notification_message = "Welcome to Virtual Intelligent Companion & Task-Undertaking Software (Victus)"

    show_notification(notification_title, notification_message)        

def measure_speed():
    st = speedtest.Speedtest()
    
    speak("Fetching the best server...")
    print("Fetching the best server...")
    st.get_best_server()
    
    speak("Testing download speed...")
    print("Testing download speed...")
    download_speed = st.download() / 1024 / 1024
    
    speak("Testing upload speed...")
    print("Testing upload speed...")
    upload_speed = st.upload() / 1024 / 1024
    
    speak(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    speak(f"Upload Speed: {upload_speed:.2f} Mbps")    
    print(f"Upload Speed: {upload_speed:.2f} Mbps")    

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password   

def search_youtube(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(search_url)
    speak("searching youtube")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Please speak that you want to search...")
        print("Please speak that you want to search...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand your speech.")
        print("Sorry, I couldn't understand your speech.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None 
    
def calculate_typing_speed(text, elapsed_time):
    words = len(text.split())
    wpm = (words / elapsed_time) * 60
    return wpm

def main_test():
    speak("Ok, Press Enter to start...")
    input("Press Enter to start...")
    
    text_to_type = "The quick brown fox jumps over the lazy dog."
    speak(f"Type the following text as fast as you can:\n{text_to_type}")
    print(f"Type the following text as fast as you can:\n{text_to_type}")
    
    start_time = time.time()
    speak("Start typing: ")
    user_input = input("Start typing: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    wpm = calculate_typing_speed(text_to_type, elapsed_time)

    if user_input == text_to_type:
       speak(f"\nTime elapsed: {elapsed_time:.2f} seconds")
       print(f"\nTime elapsed: {elapsed_time:.2f} seconds")
       speak(f"Your typing speed: {wpm:.2f} WPM")    
       print(f"Your typing speed: {wpm:.2f} WPM")    

    else:
        speak("Sorry.")   
    
def search_google(query):
    google_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(google_url)
    speak("searching google")

def main_google_search():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Please say your search query:")
        print("Please say your search query:")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"Search Query: {query}")
        search_google(query)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your query.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")    

def get_battery_info():
    battery = psutil.sensors_battery()

    if battery.power_plugged:
        status = "Charging"
    else:
        status = "Discharging"

    percentage = battery.percent
    time_left = battery.secsleft / 60 if battery.secsleft != psutil.POWER_TIME_UNKNOWN else None

    return {
        "Status": status,
        "Percentage": percentage,
        "Time Left (minutes)": time_left
    }

def battery_percentage():
    battery_info = get_battery_info()

    speak("Battery Information:")
    print("Battery Information:")
    speak(f"Status: {battery_info['Status']}")
    print(f"Status: {battery_info['Status']}")
    speak(f"Percentage: {battery_info['Percentage']}%")
    print(f"Percentage: {battery_info['Percentage']}%")
    
    if battery_info['Time Left (minutes)'] is not None:
        speak(f"Time Left: {battery_info['Time Left (minutes)']:.2f} minutes")
        print(f"Time Left: {battery_info['Time Left (minutes)']:.2f} minutes")
    else:
        speak("Time Left: Calculating...")    
        print("Time Left: Calculating...")    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Welcome back, I am Viccttus Sir. Please tell me how may I help you")        

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    password = input("Enter the Victus Password:  ")

    if password == passkey:
        notifier()
        wishMe()
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

        while True:
        # if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.get('chrome').open("youtube.com")
                speak("Opening youtube")

            elif 'my name' in query:
                speak("I know that you are Saatvik Sir, my developer")  
                print("I know that you are Satvik Sir, my developer")  

            elif 'open google' in query:
                webbrowser.get('chrome').open("google.com")
                speak("Opening google")

            elif 'open spotify' in query:
                webbrowser.get('chrome').open("open.spotify.com")
                speak("Opening spotify")

            elif 'open whatsapp' in query:
                webbrowser.get('chrome').open("web.whatsapp.com")    
                speak("Opening Whatsapp")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'open vs code' in query:
                codePath = "C:\\Users\\aarju\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)  
                speak("Opening VS Code")

            elif 'open calculator' in query:
                os.startfile("C:\\Windows\\System32\\calc.exe")  
                speak("Opening Calculator")

            elif 'stop' in query:
                stop_program()

            elif 'internet speed test' in query:
                speak("Internet Speed Test")
                print("Internet Speed Test")
                measure_speed()    

            elif 'battery information' in query:
                battery_percentage()

            elif 'joke' in query:
                telljoke()    

            elif 'secret password' in query:
                random_password = generate_random_password(8)
                speak("Secret Password is generated, now you can use it anywhere, remember, never share this secret password to anyone")    
                print("Generated Password:", random_password)    

            elif 'search on youtube' in query:
                queryyoutube = recognize_speech()
                if queryyoutube:
                    search_youtube(queryyoutube)    

            elif 'search on google' in query:
                main_google_search() 

            elif 'typing speed' in query:
                main_test()         

            elif 'control center' in query or 'control centre' in query:
                speak("During Operating the Control Center, you will need to enter the values and give the answers by the means of typing, you can't give voice commands.")
                print("1. Set Password")
                print("2. Change Password")
                print("3. Quit")

                choice = input("Enter your choice: ")

                if choice == "Set Password":
                    password = input("Enter the new password: ")
                    set_password(password)
                    print("Password set successfully!")
                elif choice == "Change Password":
                    current_password = input("Enter the current password: ")
                    if check_password(current_password):
                        change_password()
                    else:
                        print("Incorrect password. Please try again.")
                elif choice == "Quit":
                    break
                else:
                    print("Invalid choice. Please select a valid option.")  

            elif 'play' in query:
                song = query.replace('play', "")
                speak("Playing" + song)            
                pywhatkit.playonyt(song)

            elif 'who is' in query:
                human = query.replace('who is', "")
                info = wikipedia.summary(human, 1)           
                print(info)
                speak(info)

            else:
                pass  

    else:
        print("Sorry, That's Incorrect Password")    
        speak("Sorry, That's Incorrect Password")    