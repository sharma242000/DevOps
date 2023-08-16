from gtts import gTTS
import os
mytext="my name is mohit"
language='en'
myaudio= gTTS(text=mytext, lang=language,slow=False)
myaudio.save("name.mp3")
os.system("name.mp3")

