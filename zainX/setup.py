from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the contents of your requirements file
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name='fingrecon',
    version='1.0.0',
    author='MacabreCerberus', # Replace with your name/username
    description='A simple OSINT tool for username reconnaissance.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/YOUR_USERNAME/fingrecon', # Replace with your repo URL
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'fingrecon=fingrecon.fingrecon:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)