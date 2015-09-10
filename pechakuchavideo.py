# Videographic Criticism using Chance Operations
# by Mark Sample http://www.samplereality.com
# based on an idea by Jason Mittell http://justtv.wordpress.com

# Inspired by the Pecha Kucha format, this program assembles
# ten random 6-second clips from a single video
# into a single 1-minute video, overlayed with a
# randomly selected 60-second audio clip from the same video

# First we need to import some helper modules
# moviepy does the bulk of the work, relying on FFMpeg as its video-editing engine
# random picks the random start and stop times
from moviepy.editor import *
import random

# Random Audio Clip
# Next we select a random audio clip from the source video
# The "begin" variable selects a random timecode, in seconds
# (0,2754) indicates the length of the video, in seconds, minus 60 seconds
begin = random.randint(0,2754)
snd = AudioFileClip('madmens7e1.mp4').subclip(begin,begin+60)
snd.write_audiofile('audiotrack.mp3')

# Random Video Clips
# Next we select the 10 random clips, 6 seconds each
# The "begin" variable once again is a random number, in seconds
# Change the end range of "begin" if the length of the video changes
# (and subtract 6)
# The "end" variable is begin+6, making each clip 6 seconds long
# clip.volumex removes the audio from each clip
# We also save each new clip with a distinct file name
for i in range(0,10):
    begin = random.randint(0,2808)
    end = begin + 6
    clip = VideoFileClip("madmens7e1.mp4").subclip(begin, end)
    clip = clip.volumex(0)
    clip.write_videofile("madmenclip"+str(i)+".mp4")

# Now we assign names to each saved clip
clip0 = VideoFileClip('madmenclip0.mp4')
clip1 = VideoFileClip('madmenclip1.mp4')
clip2 = VideoFileClip('madmenclip2.mp4')
clip3 = VideoFileClip('madmenclip3.mp4')
clip4 = VideoFileClip('madmenclip4.mp4')
clip5 = VideoFileClip('madmenclip5.mp4')
clip6 = VideoFileClip('madmenclip6.mp4')
clip7 = VideoFileClip('madmenclip7.mp4')
clip8 = VideoFileClip('madmenclip8.mp4')
clip9 = VideoFileClip('madmenclip9.mp4')

# We assemble all the clips into something called "final_clip"
final_clip = concatenate_videoclips([clip0,clip1,clip2,clip3,clip4,clip5,clip6,clip7,clip8,clip9])

# Finally, save the assembled final_clip, using the random audio file created above
final_clip.write_videofile("pechakucha.mp4",audio="audiotrack.mp3")
