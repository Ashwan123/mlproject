from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements from the requirements.txt file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        # Read each line, strip whitespace, and remove empty lines
        requirements = [req.strip() for req in file_obj.readlines() if req.strip()]
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Ashwan",
    author_email="ashwan271296@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Read dependencies from requirements.txt
)
