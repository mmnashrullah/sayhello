import setuptools

with open("README.md", "r", encoding="utf-8") as fh: 
    long_description = fh.read()
    
setuptools.setup(
    name="Sayhello",
    version="1.0.0",
    author="Maulana Malik Nashrulloh",
    author_email="mmnashrullah@gmail.com",
    description="Just Say hello",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mmnashrulloh/sayhello",
    project_urls={
    "Bug Tracker": "https://github.com/mmnashrulloh/sayhello/issues",
    },
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8"
    )
