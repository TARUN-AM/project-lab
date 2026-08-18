from gtts import gTTS
text = "Hello everyone this is L!"

tts = gTTS(text=text,lang="en")
tts.save("audio.mp3")

print("AUDIO SAVED!!")