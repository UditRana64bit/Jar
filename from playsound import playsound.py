import speech_recognition as sr
import time

def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for activation word...")
        audio = r.listen(source,0,2)

    try:
        text = r.recognize_google(audio)
        if "Jarvis" in text:
            print("Jarvis activated!")
            speak("Always At Your Service Sir")
            return True
        else:
            return False
    except sr.UnknownValueError:
        print("Could not understand audio")
        return False
    except sr.RequestError as e:
        print("Could not request results from speech recognition service; {0}".format(e))
        return False

def command():
    if listen_for_command():
        try:
            r=sr.Recognizer()
            print("Listening for command...")
            with sr.Microphone() as source:
                audio = r.listen(source,0,8)  # Listen for 5 seconds
            command = r.recognize_google(audio)
            return (command)
            # Process the command here
        except sr.UnknownValueError:
            print("Sorry, I could not understand your command.")
            print("Please enter your command as text: ")
            command = input()
            print(f'User: {command}')
            return command
        except sr.RequestError as e:
            print("Could not request results from speech recognition service; {0}".format(e))


command()