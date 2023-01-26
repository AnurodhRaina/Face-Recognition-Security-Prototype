# Face-Recognition-Security-Prototype
A facial recognition security system that can recognize the user (presumably the owner of the PC, which it has been trained to recognize.) through the webcam. If it is not the owner, the PC can be instructed to shutdown. <br>
<br><b>face_predictor/ face_predictor2.0 --></b> Experiment model trained to recognize me
transfer_learning_trained_face_cnn_model.h5 --> Actual model used to recognize me
<br><b>model_data --> </b>model that detects a face in a picture and extracts it
<br><b>images --> </b>raw images captured from webcam
<br><b>faces --> </b>faces extracted from the image in images folder
<br><b>password.txt --> </b>for additional security and testing
<br> Still a work in progress and will be generalized so anyone can train the model and use the script if you have a set of images of yourself.


<h3> Currently the code and model are trained to recognize my face only, working on building a seperate file so that users can inpuit their faces too.</h3>

<b><i>Immense help taken from --></i></b> https://github.com/kb22/Create-Face-Data-from-Images
