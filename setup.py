from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aitts-maker",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "aitts-maker=aitts_maker.cli:main"
        ]
    },
    author="DOT-007",
    author_email="alosiousbenny7@gmail.com", 
    description="AI and standard TTS voice generator using ttsmp3.com (via scraping)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dot-ser/aitts-maker", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio :: Speech"
    ],
    python_requires='>=3.6',
)
