import cv2
import os
os.environ['KERAS_BACKEND'] = 'theano'
import numpy as np
from PIL import Image
from tensorflow import keras



#setting up path to various required directories and images
base_dir = os.path.dirname(__file__)
image_path = str(base_dir +'\\'+'images')
extracted_face_path = str(base_dir +'\\'+'faces')
predictor_path = str(base_dir+'\\'+ 'face_predictor2.0')
prototxt_path = str(base_dir + '\\' + 'model_data\deploy.prototxt')
caffemodel_path = str(base_dir +'\\' + 'model_data\weights.caffemodel')
model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)
input_file =''

cam = cv2.VideoCapture(0)

ret, frame = cam.read()
if not ret:
    print("failed to grab frame")
    
img_counter = str(len(os.listdir(image_path)))
img_name = "picture_{}.png".format(img_counter)
cv2.imwrite('images'+'\\'+img_name, frame)
print("{} written!".format(img_name))

cam.release()

file_to_check = image_path +'\\'+img_name
print(file_to_check)


# make the directory for exracted faces
if not os.path.exists('faces'):
	print("New directory created")
	os.makedirs('faces')

image = cv2.imread(file_to_check)
(h, w) = image.shape[:2]
print(h,w)
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

model.setInput(blob)
detections = model.forward()

# if no faces are detected in the captured image
print('det =',detections.shape[2])
if detections.shape[2] == 0:
    print('No faces detected... trying again')
    
# Identify each face
for i in range(0, detections.shape[2]):
    
    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
    (startX, startY, endX, endY) = box.astype("int")

    confidence = detections[0, 0, i, 2]

    # If confidence > 0.5, save it as a separate file
    if (confidence > 0.5):
        input_file = str(i) + '_' + img_name
        frame = image[startY:endY, startX:endX]
        cv2.imwrite(extracted_face_path + '\\' +  input_file, frame)
###########################################
#MODEL INPUT
##################

face_to_check = Image.open(str(extracted_face_path + '\\' +input_file))
face_to_check = face_to_check.resize((224,224))
face_to_check = np.array(face_to_check)
# face_to_check = face_to_check.reshape((200,200,1))
print(face_to_check)


with open('password.txt') as f:
    correct_password = f.read()

model = keras.models.load_model('transfer_learning_trained_face_cnn_model.h5')
# model = keras.models.load_model('face_predictor2.0')
preds = model.predict(x=np.array([face_to_check]))
print(preds[0])
if preds[0][1]>0.8:
    print('Probability is higher than 50%, welcome anurodh')
else:
    print('This is not anurodh, Please enter correct \
            password or the system will turn off')
    password = int(input('Enter password --> '))
    if password != int(correct_password):
          print('Odds are against you, Turning off system...')
        #   os.system("shutdown /s /t 1")
    else:
          print('Welcome Anurodh')
          

                     
