# This is the file responsible for making connection request to server
# This paclage has a Request class which takes (url, data, content_type) as params
import urllib2
import os
import subprocess


def send_image_data_and_play_audio(url, data):
	req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
	audio_file = urllib2.urlopen(req)
	with open('test.mp3','wb') as output:
 		output.write(audio_file.read())
 	# Yet to figure out to play data.
 	subprocess.call(['omxplayer', '/home/pi/test.mp3'])

