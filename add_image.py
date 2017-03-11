# Import the custom modules written to help along with Database
from Server.Scripts.helpers import index_face,create_collection,delete_collection
from Server.Model.database_setup import DBSession, Mapping
import os

# Collection name for image metadata collection on AWS.
COLLECTION_NAME = "RASPBERRY"

# Open database connection. This session is shared with all the files in the Folder
session = DBSession()

# Make sure that this file in run explicitly and not called from other module.
if __name__ == '__main__':
	# Create the collection with then above name
	status = create_collection(COLLECTION_NAME)
	# Read on the status 
	# Is true if colleciton is created for first time and False if collection already exists
	if status:
		print "Collection Created"
	else:
		print "Collection exists already, using that...."

	# Pass the image file path here when adding the image. Make sure you rename the image file as test
	with open('D:\\Rajendra\\Pictures\\Camera Roll\\test.jpg', 'rb') as image:
		# Read the image bytes
		data = image.read()
	# Hold the face_id returned from AWS via this function
	face_id = index_face(COLLECTION_NAME, data)

	# Get the name from prompt to map the face id in database
	name = raw_input("Enter name: ")

	# Create the mapping object to store in db
	mapping = Mapping(name = name, face_id = face_id)

	# Print the details
	print "Face id " + str(face_id) + " mapped to " + str(name) 

	# Add it to database using session (open connection)
	session.add(mapping)

	# Commit the changes
	session.commit()

	# Best practice to close the session
	session.close()

	# Delete the image from server
	print "Deleting image from local store..."
	os.remove('D:\\Rajendra\\Pictures\\Camera Roll\\test.jpg')

	# Print confirmation
	print "Face indexed"

	'''print "Deleting Collection.."
				delete_collection(COLLECTION_NAME)'''
