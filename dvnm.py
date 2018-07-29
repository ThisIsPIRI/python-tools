"""
The "best" quality youtube-dl automatically downloads videos at might not actually be the best: Youtube usually doesn't provide FHD videos with audio.
Thus, youtube-dl downloads the "best" format that contains both the video and audio by default, which is not the best in most cases.
To download videos at the true best quality, we have to download the video AND audio in most cases("youtube-dl -f bestvideo" and "youtube-dl -f bestaudio")
then merge the two with ffmpeg or similar tools. This script automates that cumbersome process.
"""
helpString = """
Downloads a video from Youtube at the highest resolution possible, with audio.
Requires youtube-dl and ffmpeg in a Path.
Pass the IDs of the videos you want to download after the name of the script(dvnm.py).
To supply additional arguments to youtube-dl or ffmpeg, pass them after -yd or -ff and write "end" at the end of arguments.
The additional arguments must come before any video IDs.
Example: python dvnm.py -ff -muxers -y -yd --match-title (.+) end jNQXAC9IVRw
The filenames of the resulting videos will be (video ID).mp4. If a file of same name exists in the working directory, the video will be skipped.
"""
import os
from pathlib import Path
import subprocess
import sys

def getNextOf(what, inString):
	"""Returns the word next of what inString. Returns None when the word couldn't be found or was the last one inString."""
	nextIsName = False
	for word in inString.split():
		if word == what:
			nextIsName = True
		elif nextIsName:
			return word
	return None
	

if len(sys.argv) < 2:
	print("Not enough arguments. Try -? for help.")
	exit()
elif sys.argv[1] == "-?":
	print(helpString)
	exit()
	
# Identify additional arguments for youtube-dl and ffmpeg
idStart = 1
moreArgs = {"-yd": [], "-ff": []}
while sys.argv[idStart] != "end":
	if sys.argv[idStart] in moreArgs:
		key = sys.argv[idStart]
		idStart += 1
		while sys.argv[idStart] not in moreArgs and sys.argv[idStart] != "end":
			moreArgs[key].append(sys.argv[idStart])
			idStart += 1
	else: break
# The condition below is necessary; there may be no "end" if the user doesn't specify any additional arguments.
if sys.argv[idStart] == "end": idStart += 1

for index, videoId in enumerate(sys.argv[idStart:]): #Loop through all ids supplied from the command line.
	if Path(os.path.join(os.getcwd(), (videoId + ".mp4"))).is_file():
		print(f"The {index}th video already exists in this directory. Proceeding to the next video.")
		continue
	print(f"Downloading {index}th video...")
	# Download the video and audio.
	videoURL = "https://www.youtube.com/watch?v=" + videoId
	videoResult = subprocess.run(["youtube-dl",  "-o", "video_%(id)s.%(ext)s", "-f", "bestvideo", videoURL] + moreArgs["-yd"], stdout=subprocess.PIPE).stdout
	print("Completed downloading the video")
	audioResult = subprocess.run(["youtube-dl", "-o", "audio_%(id)s.%(ext)s", "-f", "bestaudio", videoURL] + moreArgs["-yd"], stdout=subprocess.PIPE).stdout #Make the audio's filename differ from that of the video's so the video and audio don't collide.
	print("Completed downloading the audio")

	# Parse the output to get the filenames. We cannot use videoId for this as we don't know the format.
	try:
		videoFile = getNextOf(b'Destination:', videoResult).decode("utf-8") #subprocess gives bytes by default. They have to be decoded into strings to be passed to subprocess.run().
		audioFile = getNextOf(b'Destination:', audioResult).decode("utf-8")
	except AttributeError: #Thrown if the destination filename wasn't found in one of the results.
		print(f"Couldn't find the files for {index}th video. Proceeding to the next video.")
		continue

	subprocess.run(["ffmpeg", "-y", "-i", videoFile, "-i", audioFile, "-crf", "0", "-c:v", "copy", "-c:a", "aac", "-strict", "experimental", f"{videoId}.mp4", "-hide_banner"] + moreArgs["-ff"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	print("Completed merging the two")
	os.remove(videoFile)
	os.remove(audioFile)