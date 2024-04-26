# Deepface (Facial Recognition)
# Function: Facial Verfication (Compares two image and see if the faces are similar)

import sys

# Checks to make sure two image paths as arguments were passed
# Define help message
help_text = """
Error:   This script requires two image paths be passed  as arguments.
Usage:   python facial_verification.py <image_path1> <image_path2>
Example: python facil_verification.py image1.jpg image2.png
"""
# Check for correct number of arguments
if len(sys.argv) != 3:
    print(help_text)
    exit()

# Function: Flatten Nested Dictionary
def flatten_dict(dd, separator ='_', prefix =''):
  return { prefix + separator + k if prefix else k : v
           for kk, vv in dd.items()
           for k, v in flatten_dict(vv, separator, kk).items()
           } if isinstance(dd, dict) else { prefix : dd }

# Imports the Deepface library later because it takes time to initialize
from deepface import DeepFace

# Image paths for comparision
imagePath1 = sys.argv[1]
imagePath2 = sys.argv[2]

# Compare the two images (image1 and image2), this is where most of the processing happens
# Note: The output is stored in a nested dictionary
verifyResults = DeepFace.verify(img1_path = imagePath1, img2_path = imagePath2)

# Flatten nested dictionary output (makes it easier to read)
outputResults = flatten_dict(verifyResults)
# Display the flatten nested dictionary
for key, value in outputResults.items():
  print("-",key,"=",value)

