import pyttsx3
import speech_recognition as sr 

def speak(speak):
    engine = pyttsx3.init()
    engine.say(speak)
    engine.runAndWait()



import speech_recognition as sr 

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Anything: ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('you said : {}'.format(text))
        speak(text)
    except:
        print('sorry')


