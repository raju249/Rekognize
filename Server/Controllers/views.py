# Below modules are important for reading requests and sending a json response to server
from flask import request, jsonify, send_file

# To read the json data sent in the request
import json

# Importing the helper functions to interaact with AWS.
from Scripts.helpers import *

# Database connection to access the face_id and name mapping in sqlite file
from Model.database_setup import DBSession

# A view that returns the audio file for the requested image
def search_face():

	# Check if the request is POST and not GET, PUT or any other
	if request.method == "POST":

		# Open a session connection to database
		session = DBSession()

		# Load the data sent in the request as json
		data = json.loads(request.data)

		# Read the image bytes is the json data
		imageBytes = data['image']

		# Search for the face from a given collection_id and above image bytes
		meta_data = search_faces_in_collection(collection_id, imageBytes)

		# Search for the name from the data received above
		name = get_name(meta_data, session)

		# Best practice to clode the current session
		session.close()
		
		# Create the appropriate audio file that is sent to PI
		build_audio(name)

		# Send the file to PI
		return send_file(
				'Audio/greeting.mp3',
				mimetype = 'audio/mp3',
				as_attachment = True,
				attachment_filename = "greeting.mp3")
	else:
		# Handle errored cases
		return jsonify({"status" : "Error"})