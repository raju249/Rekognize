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
		imageBytes = data['image']
		meta_data = search_faces_in_collection(collection_id, imageBytes)
		name = get_name(meta_data, session)
		build_audio(name)
		return send_file(
				'Audio/greeting.mp3',
				mimetype = 'audio/mp3',
				as_attachment = True,
				attachment_filename = "greeting.mp3")
	else:
		return jsonify({"status" : "Error"})