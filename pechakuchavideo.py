# Videographic Criticism using Chance Operations
# by Mark Sample http://www.samplereality.com
# based on an idea by Jason Mittell http://justtv.wordpress.com
# updated and made more generalized by Daniel Houghton 2015-16

# Inspired by the Pecha Kucha format, this program assembles
# ten random 6-second clips from a single video
# into a single 1-minute video, overlayed with a
# randomly selected 60-second audio clip from the same video

# First we need to import some helper modules
# moviepy does the bulk of the work, relying on FFMpeg as its video-editing engine
# random picks the random start and stop times
from moviepy.editor import *
import random
import sys

if ( len(sys.argv) != 2):
	print("Arguments expected in the following format: pechakuchavideo.py source_video")
	exit()


source_video_name = sys.argv[1]
source_video = VideoFileClip(source_video_name)

# Random Audio Clip
# Next we select a random audio clip from the source video
# The "begin" variable selects a random timecode, in seconds
# (0,2754) indicates the length of the video, in seconds, minus 60 seconds
begin = random.randint(0, int(source_video.duration - 60))
snd = AudioFileClip(source_video_name).subclip(begin,begin+60)
snd.write_audiofile(source_video_name.split(".")[0] + '_audiotrack.mp3')

# Random Video Clips
# Next we select the 10 random clips, 6 seconds each
# The "begin" variable once again is a random number, in seconds
# Change the end range of "begin" if the length of the video changes
# (and subtract 6)
# The "end" variable is begin+6, making each clip 6 seconds long
# clip.volumex removes the audio from each clip
# We also save each new clip with a distinct file name
clip_list = []

for i in range(0,10):
    begin = random.randint(0,int(source_video.duration - 6))
    end = begin + 6
    clip = source_video.subclip(begin, end)
    clip = clip.volumex(0)
    clip.write_videofile(source_video_name.split(".")[0]+ "_" + str(i) + ".mp4")
    clip_list.append(clip)

# Now we assign names to each saved clip


# We assemble all the clips into something called "final_clip"
final_clip = concatenate_videoclips(clip_list)

# Finally, save the assembled final_clip, using the random audio file created above
final_clip.write_videofile(source_video_name.split(".")[0] + "_pechakucha.mp4",audio=source_video_name.split(".")[0] + '_audiotrack.mp3')
