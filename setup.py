from setuptools import setup, find_packages

setup(
    name="Tutek",                      # Replace with your project name
    version="0.0.2",                        # Version of your package
    author="Dawid Zadlo",
    author_email="dawidzadlo12@gmail.com",
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",

    packages=find_packages(),              # Automatically find packages
    install_requires=[
        # Add dependencies here, e.g.:
        # "numpy>=1.21.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",               # Minimum Python version
)

