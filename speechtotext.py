#version of speech_recognition module
import speech_recognition as sr
#print(sr.__version__)
r = sr.Recognizer() #initialize
with sr.Microphone() as source:
    text = r.listen(source)

    try:
        recognized_text = r.recognize_google(text)
        print(recognized_text)
    except sr.UnknownValueError:
        print("can't hear")
    except sr.RequestError as e:
        print(" error on requesting")