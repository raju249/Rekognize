# import the webcam class to use for raspberry pi
from Scripts.webcam import WebCam

# Helper function for sending data to server
from Scripts.server_connection import send_image_data_and_play_audio

# importing sys for accessing command line arguments
import sys

# importing time for delay in clicking images
import time

# for dumping dict to json
import json

# Server url from command line. Now since we use ngrok for exposing localhost we pass it in command line.
SERVER_URL = str(sys.argv[1]) + '/v/search_face'

# Initialize the WebCam object
webcam = WebCam()

# Utility function for clicking image that uses the webcam object
def click_image_and_convert():
	# Click the image using Webcam method 
	webcam.clickImage()

	# Mechanism for using convertImageBytes method
	data = webcam.convertImageToBytes()

	# Return the bytes
	return data

# Main method to run on PI
def main():
	# Get the image clicked from webcam and get the bytes.
	data = click_image_and_convert()

	# Convert it into json
	data = json.dumps({'image' : data.encode('base64')})

	# Send the data to server and get the audio and play it.
	send_image_data_and_play_audio(SERVER_URL, data)

	# Exit from stack
	return

if __name__ == '__main__':

	# Call it forever with 10 second sleep
	while True:
		try:
			main()
			print "Sleeping for 10 seconds.."
			time.sleep(10)
		except Exception as e:
			print str(e)


