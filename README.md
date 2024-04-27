# Introduction to Facial Recognition in Python
This project is meant to provide an introduction to the deepface python library for doing facial recognition,by providing sample python code, data, and instructions on how to use the scripts.
## Background
Deepface is a lightweight face recognition and facial attribute analysis (age, gender, emotion and race) framework for python. It is a hybrid face recognition framework wrapping state-of-the-art models: VGG-Face, Google FaceNet, OpenFace, Facebook DeepFace, DeepID, ArcFace, Dlib, SFace and GhostFaceNet.

Experiments show that human beings have 97.53% accuracy on facial recognition tasks whereas those models already reached and passed that accuracy level.
## Getting Started
- [Deepface Repository](https://github.com/serengil/deepface)
- [PYPI Repository](https://pypi.org/project/deepface/)
- [Installation Instruction](https://github.com/serengil/deepface?tab=readme-ov-file#installation--)
- [Available Test Images](https://github.com/serengil/deepface/tree/master/tests/dataset)
## Available Sample Code
Below are some sample projects that I have created to demonstrate the framework.  These projects are designed to make it easy to get started using the technology right away to reduce the learning curve required to understand it.
- Facial Analysis: `python facial_analysis.py [imagePath]`
  - Description: Displays a facial analysis of image, displays informaiton about: age, gender, emotion, and race.
  - Reqires a file path and name for image to analyze.
- Facial Verification: `python facial_verification.py [imagePath1] [imagePath2]`
  - Description: Compares two faces and verifies if they are similar.
  - Requires two file paths and names of images to compare.
- Find Related Images: `python find_related_images.py [imagePath] [imageDirectory]`
  - Description: Takes a target images and scans a directory for similar ones.
  - Requires a image file path and name and image directory path to search for related images.
