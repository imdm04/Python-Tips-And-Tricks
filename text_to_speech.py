import pyttsx3
# engine = pyttsx3.init()
# engine.say('HEllo friends, how are you?')
# # engine.runAndWait()

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

# # windows in-built library
# import win32com.client as wincl
# speak = wincl.Dispatch("SAPI.SpVoice")
# speak.Speak("Hello World, How are you")
from gtts import gTTS
import os
tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
# os.system("mpg321 good.mp3")