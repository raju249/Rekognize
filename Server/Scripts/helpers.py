# Imported libs are used below in the code.
import boto3
import os
from contextlib import closing
from Server.Model.database_setup import Mapping

# Reference for AWS client from boto
rekognition_client = boto3.client('rekognition')
polly_client = boto3.client('polly')


# This method searches for a given image in the collection given by collection id
def search_faces_in_collection(collection_id, imageBytes):
	# Get the response from aws using the search_face_by_image from boto3
	response = rekognition_client.search_faces_by_image(
		# Specify the collection id
		CollectionId = collection_id,
		Image = {
		# specify the image bytes
				'Bytes':imageBytes
			}
		)
	# Return the face matches array and not any other data that we don't need.
	return response['FaceMatches'][0]['Face']

# This method fetches the audio from polly and saves it in grreting.mp3 file.
def build_audio(name):
	try:
		response = polly_client.synthesize_speech(
				OutputFormat = 'mp3',
				Text = 'Hello ' + str(name) + ' How are you doing ?',
				VoiceId = 'Raveena'
			)
		# Access the audio stream from the response
		if "AudioStream" in response:
		    # Note: Closing the stream is important as the service throttles on the
		    # number of parallel connections. Here we are using contextlib.closing to
		    # ensure the close method of the stream object will be called automatically
		    # at the end of the with statement's scope.
		    with closing(response["AudioStream"]) as stream:
		        output = os.path.join("Audio/", "greeting.mp3")

		        try:
		            # Open a file for writing the output as a binary stream
		            with open(output, "wb") as file:
		                file.write(stream.read())
		        except IOError as error:
		            # Could not write to file, exit gracefully
		            print str(error)
		else:
		    # The response didn't contain audio data, exit gracefully
		    print "Could not stream audio"
	except Exception as e:
		raise e


# Searches the database for matching face_id in data variable
def get_name(data, session):
	# get the face id from the data dictionary passed. This data var refers to dict returned by search_faces_in_collection method.
	face_id = data['FaceId']
	# Search it in database using the passed session object.
	image = session.query(Mapping).filter_by(face_id = face_id).first()
	# sanity check for seeing if we have no mathcing person
	if image is not None:
		return str(image.name)
	return None

def index_face(collection_id, image_bytes):
	response = rekognition_client.index_faces(
				CollectionId = collection_id,
				Image = {
					'Bytes' : image_bytes
				}
			)
	return response['FaceRecords'][0]['Face']['FaceId']

def create_collection(name):
	response = rekognition_client.create_collection(
				CollectionId = name
			)
	if response['StatusCode'] == 200:
		return True
	return False