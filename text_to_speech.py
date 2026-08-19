from gtts import gTTS
text = "yokoso!"

tts = gTTS(text=text,lang="en")
tts.save("audio.mp3")

print("AUDIO SAVED!!")