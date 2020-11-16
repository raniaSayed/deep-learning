import face_recognition
import os 
import PIL.Image
import PIL.ImageDraw

faces_encodings = []

def load_image(path):
  images = os.listdir(path)
  print(images)
  for i in np.arange(len(images)):
    # Load the jpg files into numpy arrays
    image = face_recognition.load_image_file(path + "/" + images[i])
    print(images[i])
    # Generate the face encodings
    face_encodings = face_recognition.face_encodings(image)[0]
    faces_encodings.append(face_encodings)

  print("faces is complete encoding\n") 



## load images in folder just write path 
load_image('/content/images')




## upload unknown image 
def recognize_image(path):

    # Load the image we want to check
  unknown_image = face_recognition.load_image_file(path)

  # Get face encodings for any people in the picture
  unknown_face_encodings = face_recognition.face_encodings(unknown_image)
    # There might be more than one person in the photo, so we need to loop over each face we found
  for unknown_face_encoding in unknown_face_encodings:

      # Test if this unknown face encoding matches any of the three people we know
      results = face_recognition.compare_faces(faces_encodings, unknown_face_encoding, tolerance=0.6)
      print(results[0])
      if results[0]:
        name = "ahmed hassan"

        print(f"Found {name} in the photo!")
      else:
        print(f"not Found this image in the photo!")


## upload path of unknown image
recognize_image('/content/unknown_3.jpg')

