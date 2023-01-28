# Face-Recognition-Security-Prototype
A facial recognition security system that can recognize the user (presumably the owner of the PC, which it has been trained to recognize.) through the webcam. If it is not the owner, the PC can be instructed to shutdown. <br>

<table border =2>
<tr><th>Object</th><th>Description</th></tr>
<tr><td><b>Training Material</b> </td><td> required script for training a model for yourself</td></tr>
<tr><td><b>transfer_learning_trained_face_cnn_model.h5 </b></td><td> actual model used to recognize me</td></tr>
<tr><td><b>model_data </b></td><td> model that detects a face in a picture and extracts it</td></tr>
<tr><td><b>images </b></td><td> raw images captured from webcam</td></tr>
<tr><td><b>faces </b></td><td> faces extracted from the image in images folder</td></tr>
<tr><td><b>password.txt </b></td><td> for additional security and testing</td></tr>
<tr><td><b>requirements.txt </b></td><td> set of required modules needed to be installed for this project</td></tr>
<tr><td><b>capture.py</b></td><td> face detection and recognition script </td></tr>
</table>
<br>Still a work in progress and will be generalized so anyone can train the model and use the script if you have a set of images of yourself.


### <strike>Currently the code and model are trained to recognize my face only, working on building a seperate file so that users can inpuit their faces too.</strike>

### UPDATE: Training script has been created if anyone wants to fine train a VGG model (through transfer learning) on their own data

## STEPS FOR TRAINING
### Install requirements.txt
```pip install -r requirements.txt```
### Collect images of yourself (prefrebaly taken through a webcam since thats what will be used to detect and verify faces).
 - You can create as many categories possible for _n_ number of people. 
### Extract the faces from these images
 - This is a task of extracting only the faces from these images as shown below.

 ![image](https://user-images.githubusercontent.com/51761306/214843945-f005cf5e-2a60-408d-aa6b-b75c9fe192c6.png)
- This can be done by a lot of different ways although the most common one is the haarcascade_frontalface detection method. Consider this as a learning opportunity and perform the face extraction on your collected dataset. (you can use the links in the bottom to get started)
### Group your dataset accordingly under a predefined structure and zip the 'headshots' folder as shown
  ```|
  |-Headshots.zip
  |   |
  |   |-You
  |   |-Not you
  |   |
  ```
  - Feel free to create more categories as you can add more headshot images of people (minimum 2 required).
### Go to google colab and open the _facerec_2_0_2023.ipynb_ notebook and change runtime type to GPU
- Now upload the Headshots.zip in the notebook directory and run the cells one by one. 
- If you encounter any module error just simply use pip to download that module.
- NOTE: if faced by keras_engine not found error use --> https://stackoverflow.com/a/71379206
- The notebook will propduce an .h5 model file fine-tuned on your data and can be used in place of the provided model.

### Replace the old file and you are good to go.










<b><i>Immense help taken from </i></b> 
- https://github.com/kb22/Create-Face-Data-from-Images
- https://www.codemag.com/Article/2205081/Implementing-Face-Recognition-Using-Deep-Learning-and-Support-Vector-Machines
- https://stackoverflow.com/questions/51337558/how-to-import-keras-engine-topology-in-tensorflow
