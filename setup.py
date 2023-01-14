from setuptools import setup
from typing import List


# Declaring variables for setup function
PROJECT_NAME='HousingPrediction'
VERSION="0.0.0.1"
AUTHOR="JayantGupta"
DESCRIPTION="This is my first end to end ML Project"
PACKAGE=["housing"]
RESUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirements mention in 
    requirements.txt file
    
    return: This function is going to return list which will contain name of libraries 
    mention in requirements.txt file
    
    """
    with open(RESUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()





setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGE,
    install_requires=get_requirements_list()
)
