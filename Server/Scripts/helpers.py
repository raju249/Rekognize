import boto3
import os
from contextlib import closing

rekognition_client = boto3.client('rekognition')
polly_client = boto3.client('polly')

def search_faces_in_collection(collection_id, imageBytes):
	response = rekognition_client.search_faces_by_image(
		CollectionId = collection_id,
		Image = {
				'Bytes':imageBytes
			}
		)
	return response['FaceMatches'][0]['Face']

def search_name(name):
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

def get_name(data):
	