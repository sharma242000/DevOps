import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("kuch to bolo:")
    audio = r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said: ", text)
    except:
        print("sorry unable to understand your voice")

