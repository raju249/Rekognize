from Server.Scripts.helpers import index_face,create_collection
from Server.Model.database_setup import DBSession, Mapping

COLLECTION_NAME = "RASPBERRY"

session = DBSession()

if __name__ == '__main__':
	status = create_collection(COLLECTION_NAME)
	if status:
		print "Collection Created"
	else:
		print "Collection exists already, using that...."

	with open('D:\\Rajendra\\Pictures\\Camera Roll\\test.jpg', 'rb') as image:
		data = image.read()
		encoded_data = data.encode('base64')
	face_id = index_face(COLLECTION_NAME, encoded_data)
	name = raw_input("Enter name: ")
	mapping = Mapping(name = name, face_id = face_id)
	print "Face id " + str(face_id) + " mapped to " + str(name) 
	session.add(mapping)
	session.commit()
	session.close()
	print "Face indexed"
