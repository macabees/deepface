# Deepface (Facial Recognition)
# Function: Facial Analysis, displays informaiton about: age, gender, 
#           emotion, and race

# Loads the sys library to extract the parameters
import sys

# Checks to make sure an argument was passed
# Define help message
HELP_TEXT = """
Error:   This script requires one image path to be passed as a argument.
Usage:   python facial_analyze.py <image_path1>
Example: python facil_analyze.py image1.jpg
"""
# Check for correct number of arguments
if len(sys.argv) != 2:
    print(HELP_TEXT)
    sys.exit()

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

# Analyzes the facial characteristics of the image (image1), this is where 
# most of the processing happens
# Note: The output is stored in a nested dictionary embedded in a list
verifyResults = DeepFace.analyze(img_path = \
    imagePath1, actions = ["age", "gender", "emotion", "race"])

# Flatten nested dictionary output (makes it easier to read)
outputResults = flatten_dict(verifyResults[0])
# Display the flatten nested dictionary
for key, value in outputResults.items():
    print("-",key,"=",value)
#print(verifyResults[0]["age"]," years old ",verifyResults[0]["dominant_race"]," ",\
#  verifyResults[0]["dominant_emotion"]," ", verifyResults[0]["gender"])
