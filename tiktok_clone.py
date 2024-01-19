"""
README
- Install ImageMagick using ==> sudo apt install ImageMagick
- May need to modify /etc/ImageMagick-6/policy.xml by
- commenting out the line ==> <policy domain="path" rights="none" pattern="@*"/>
- Create a virtual environment in your workspace using ==> python3 -m venv .venv
- Activate the virtual environment using ==> source .venv/bin/activate
- Install dependencies in your workspace w/ virtual environment activated using ==> python -m pip install -r requirements.txt
"""

"""
NOTE 1: The following lines of code are in blocks, each with
a comment that describes the function of the block of code.
Your task is to create the correct algorithm that will
sequentially piece together all of the code to produce your
TikTok video.
NOTE 2: You can make many variations with the program.  Please
see the documentation for imported libraries and/or ask your
instructor.
"""

# Welcome message to user
print("Welcome to my TikTok clone!")
print("Please place a short video")
print("in the same folder as this file.")
print("This program is designed to produce")
print("a 'TikTok-like' video mixing the")
print("input video with text.")
print()

# Bring video into moviepy and remove audio if desired
video = VideoFileClip(file)
video = video.without_audio()

# Use google speech to text to create an audio file
tts = gTTS(text, lang=lang)
tts.save("output.mp3")

# Use google translate to tranlate text to another language
translator = Translator()
text = translator.translate(text, lang).text

# Manipulate video using moviepy.editor
# NOTE: May need to run the conditional if statement below if your video is
# a .mov file type and has been imported rotated.  Fix found at
# https://github.com/Zulko/moviepy/issues/586
if video.rotation == 90:
    video = video.resize(video.size[::-1])
    video.rotation = 0

# Import necessary libraries
from googletrans import Translator # Google's translation service
from gtts import gTTS # Google'stext to speech library
from moviepy.editor import * # MoviePy library to manipulate video

# Write final video out
video.write_videofile("output.mp4")

# Get language from user
# NOTE: you can add any language that google translate is able to handle - see the following link for language codes:
# https://py-googletrans.readthedocs.io/en/latest/
lang = input("What language would you like you text to be in? Enter 'en' for English, 'fr' for Frenc, 'es' for Spanish: ")

# Manipulate text
text = TextClip(text, color='white', fontsize=75, size=((800,0)), method='caption')
text = text.set_position('top')
text = text.set_duration(5)

# Get text input from user
text = input("What text would you like to overlay on your video?: ")

# Bring audio into moviepy
audio = AudioFileClip("output.mp3")

# Get size of video - video_size is a list, list[0] = width, list[1] = height
video_size = video.size
print(video_size)

# Combine video, text, and audio
video = CompositeVideoClip([video, text])
video.audio = audio

# Ask user for video file name
print("Please place your starter video in the same file location as this program")
file = input("and please input the precise file name: ")
