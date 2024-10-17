
# setup.py
from setuptools import setup, find_packages

# requirements.txt
# transformers==4.28.1
# torch==1.13.1
# tqdm==4.65.0
# numpy==1.24.3
# pandas==2.0.1
# scikit-learn==1.2.2
# matplotlib==3.7.1
# seaborn==0.12.2

setup(name="medical_summarizer",
      version="0.1.0", 
      packages=find_packages(),
      install_requires=[ 
        "transformers==4.28.1", 
        "torch==1.13.1",         
        "tqdm==4.65.0", 
        "numpy==1.24.3", 
        "pandas==2.0.1", 
        "scikit-learn==1.2.2", 
        "matplotlib==3.7.1", 
        "seaborn==0.12.2", 
    ], 
    author="Your Name",
    author_email="your.email@example.com",
    description="An advanced medical lecture summarizer using Flan-T5-Large",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/advanced-medical-lecturesummarizer",
)
