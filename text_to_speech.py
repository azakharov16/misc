from gtts import gTTS
import os
from pathlib import Path
path = Path(os.path.abspath(__file__)).parent
f = open(path.joinpath("speech.txt"), "r")
text = f.read()
speech = gTTS(text=text, lang='ru', slow=False)
speech.save(path.joinpath("voice.mp3"))
os.chmod(path.joinpath("voice.mp3"), 0o755)
os.system("xdg-open " + str(path.joinpath("voice.mp3")))

