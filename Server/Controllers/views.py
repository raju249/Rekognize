# Below modules are important for reading requests and sending a json response to server
from flask import request, jsonify, send_file
import json
from Scripts.helpers import *

def search_face():
	if request.method == "POST":
		data = json.loads(request.data)
		imageBytes = data['image']
		meta_data = search_faces_in_collection(collection_id, imageBytes)
		name = get_name(meta_data)
		search_name(name)
		return send_file(
				'Audio/greeting.mp3',
				mimetype = 'audio/mp3',
				as_attachment = True,
				attachment_filename = "greeting.mp3")
	else:
		return jsonify({"status" : "Error"})