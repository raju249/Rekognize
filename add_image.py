from Server.Scripts.helpers import index_face,create_collection,delete_collection
from Server.Model.database_setup import DBSession, Mapping
import os

COLLECTION_NAME = "RASPBERRY"

session = DBSession()

if __name__ == '__main__':
	status = create_collection(COLLECTION_NAME)
	if status:
		print "Collection Created"
	else:
		print "Collection exists already, using that...."

	# Pass the image file path here when adding the image. Make sure you rename the image file as test
	with open('D:\\Rajendra\\Pictures\\Camera Roll\\test.jpg', 'rb') as image:
		data = image.read()
	face_id = index_face(COLLECTION_NAME, data)
	name = raw_input("Enter name: ")
	mapping = Mapping(name = name, face_id = face_id)
	print "Face id " + str(face_id) + " mapped to " + str(name) 
	session.add(mapping)
	session.commit()
	session.close()
	print "Deleting image from local store..."
	os.remove('D:\\Rajendra\\Pictures\\Camera Roll\\test.jpg')
	print "Face indexed"
	print "Deleting Collection.."
	delete_collection(COLLECTION_NAME)
