# Deepface (Image Recognition)
# Function: Find Related Images 

import sys

# Checks to make sure the arguments were passed.
# Define help message
HELP_TEXT = """
Error:   This script requires two parameters (image and dir) paths as arguments.
Usage:   python find_related_images.py <image_path> <dir_path>
Example: python find_related_images.py image.jpg ./image_dir/
"""
# Check for correct number of arguments
if len(sys.argv) != 3:
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
imagePath = sys.argv[1]
imageDir = sys.argv[2]

# Compare the two images (image1 and image2), this is where most of the processing happens
# Note: The output is stored in a nested dictionary
print("- Image Path=     ",imagePath)
print("- Image Directory=",imageDir)
verifyResults = DeepFace.find(img_path = imagePath, db_path = imageDir)

# Flatten nested dictionary output (makes it easier to read)
outputResults = flatten_dict(verifyResults)
# Display the flatten nested dictionary
for key, value in outputResults.items():
    print("-",key,"=",value)
