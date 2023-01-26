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


<h3> <strike>Currently the code and model are trained to recognize my face only, working on building a seperate file so that users can inpuit their faces too.</strike></h3><h3>
<br>
UPDATE: Training script has been created if anyone wants to fine train a VGG model (through transfer learning) on their own data  </h3>
<b><i>Immense help taken from --></i></b> https://github.com/kb22/Create-Face-Data-from-Images
