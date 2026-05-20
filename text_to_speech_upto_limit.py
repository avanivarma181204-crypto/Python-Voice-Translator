from gtts import gTTS
import os 

message="How are you?,It's been a long time to meet you guys"

limit=message[0:15]

voice=gTTS(limit)

voice.save("now.mp3")

os.system("now.mp3")

print("success")
