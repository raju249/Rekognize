
# This is a library that allows to run commands on a terminal using python code
import subprocess

class WebCam():

	# This is the construtor for the class Webcam.
	# It initializes the connection with the webcam connected to rasberry pi
	# Before this ..install the fswebcam package on your PI
	def __init__(self):
		print "Installing Webcam package..."
		subprocess.call(['sudo', 'apt-get', 'install', 'fswebcam'])
		print "Done installing.."


	# This methods click the image and saves it using name 'testimage.jpg'
	# More info on how to do this at this website given here -- https://www.raspberrypi.org/documentation/usage/webcams/
	def clickImage(self):
		#TODO -- Write code to click image by reading instructions on above website
		# Look for __init__ method on how to call a subprocess.
		subprocess.call(['fswebcam','--no-banner','/home/pi/testimage.jpg'])

	# This method convert image to bytes since AWS only accepts base64 encoded image data for rekognition
	# Credits -- http://stackoverflow.com/questions/3715493/encoding-an-image-file-with-base64
	# After clicking the image the ClickImage return filepath which is passed here to this method in main application.py file
	def convertImageToBytes(self):
		with open('/home/pi/testimage.jpg', 'rb') as image:
			data = image.read()
		return data