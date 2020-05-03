from gtts import gTTS
text = 'Global warming is the long-term rise in the average temperature of the Earth’s climate system'
language = 'en'
speech = gTTS(text=text, lang=language, slow=True)
speech.save(r'D:\_english\hello.mp3')