from gtts import gTTS
import speech_recognition as spr


def Speech():
    a=spr.Recognizer()
    
    with spr.Microphone() as m:
        print("Avani...")
        
        audio=a.listen(m,phrase_time_limit=10)
        
        text=a.recognize_google(audio)
        
        print(text)
        
        speech=gTTS(text)
        speech.save("speech_to_text.mp3")
        
        
Speech()