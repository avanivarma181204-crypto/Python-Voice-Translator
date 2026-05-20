from gtts import gTTS
import speech_recognition as spr
from deep_translator import GoogleTranslator
import os

def Speech():
    r=spr.Recognizer()
    
    with spr.Microphone() as s:
        print("speak...")
        
        audio=r.listen(s,phrase_time_limit=20)
        
        text=r.recognize_google(audio)
        
        print("Original Text:",text)
        
        telugu_text=GoogleTranslator(source='auto',target='te').translate(text)
        print("Telugu Translation:", telugu_text)
        
        speech=gTTS(text=telugu_text,lang="te")
        speech.save("stt.mp3")
        os.system("stt.mp3")
        
Speech()
