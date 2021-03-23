# Facial-Expression-Recognition
The main aim of this project is to develop a facial expression recognition system. This system will be used to classify facial expressions into basic emotions namely happy, angry, sad, neutral and surprise.

## Table of contents
* [General info](#general-info)
* [Dataset](#dataset)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Contact](#contact)

## General info
Many different approaches can be used to overcome the problems of Facial Expression Recognition (FER) but the best-suited technique for automated FER is Convolutional Neural Networks(CNN). Thus, a novel CNN architecture is proposed and a combination of multiple datasets such as FER2013, FER+, JAFFE, CK+, and real-time photos are used for training and testing. This helps to improve accuracy and develop a robust real-time system.

## Dataset
A combined dataset is formed by collecting images from different sources. The different datasets used in this project are the FER-2013 and FER+ datasets, Extended Cohn-Kanade(CK+) database, the Japanese Female Facial Expression database(JAFFE), and images collected in real-time. This is done to improve the generalization ability of the model and to take care that the model is not biassed towards a specific group. The datasets used mainly differ in factors like pose, image quality, alignment, clarity, etc.

![Number of images in each dataset](https://user-images.githubusercontent.com/23340235/109894984-78f1c480-7cb4-11eb-9089-a69ae797b44a.png)

## Screenshots
![Output 1](https://user-images.githubusercontent.com/23340235/109897320-89a43980-7cb8-11eb-81a9-3f8130d5dbbb.png)

![Output 2](https://user-images.githubusercontent.com/23340235/109896924-d76c7200-7cb7-11eb-8982-a057e4d3fff6.png)

![Output 3](https://user-images.githubusercontent.com/23340235/109898393-2fa47380-7cba-11eb-983c-24caae37a76f.png)



## Technologies
* Platform - Google Colab
* Python - version 3.6
* Tkinter library
* PyCharm Community Edition 2016.3.2
* OpenCV - stable release 3.4.1
* Keras - stable release 2.3.1

## Setup
The jupyter notebook file has a link to the google colab notebook which can be run on the data files to build the trained CNN model. This model should then be placed in the models directory locally along with the other python scripts present in the project. After setting the appropriate path locations in the python files to the specific model, they will perform their functions seamlessly.

## Features
* Analyse multiple faces in a single frame
* Analyse and determine facial expressions corresponding to five facial emotions
* Real time facial expression recognition system.

## Contact
Created by @amoghsgopadi - feel free to contact me!
