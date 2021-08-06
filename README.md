# ID Reader

ID Reader is a tool that helps users to extract data from images of ID documents. With this tool, users should be able to skip the process of typing the data from the ID image. The OCR engine will extract the data automatically lowering the time and reducing the errors in the transcription process.

### The project functionalities include:
1. A desktop program (with GUI) to process specific ID images for Guatemala. Which includes the next functions:
    1. Reading an image from a local folder.
    1. Extracting the following data by position from the image:
        * ID number
        * First name and middle name
        * Surnames
        * Gender
        * Nationality
        * Date of birth
    1. Given a confidence level (90% by default), showing to the user the word or characters that do not comply with the requirement.
    1. Allow the user to correct the words or characters that do not comply with the confidence level.
    1. Allow the user to consult the data stored previously and search for a specific client (by any filter)
1. Storing the data and images processed into a local database (created and managed by the software).

## Requirements:
Before you run the program, you have to make sure to install the following packages (could be with "pip install") and software required.
_Python packages:_
Package | Version
------------ | -------------
Python |  3.7 or higher
opencv-python | 4.5.2 or higher
pytesseract | 0.3.7 or higher
PyQt6 | 6.1.0 or higher

_Software:_
Tesseract: you have to install tesseract OCR engine in your computer. Follow the next steps to do it:
* Download the installer for Windows here: https://github.com/UB-Mannheim/tesseract/wiki
* Install the software and search the installation folder, usually is in the path: C:\Program Files\Tesseract-OCR
* Add the path to "Path" environment variable

## Installation:
After you install the requirements you can download the program and execute it in your computer.
* Download the program [here](https://www.dropbox.com/s/u07gk3slkad9383/ID%20Reader.zip?dl=0)
* Unzip the files into any location of your computer
* Done!

## Usage:
* Open the installation folder
* Execute the main.exe file
* To learn how to use the ID Reader watch this [video](https://www.youtube.com/watch?v=hlyLoopjNIo)

## Limitations:
1. The program only processes ID images corresponding to Guatemalan IDs.
1. The image received should be in the same direction of the original ID (the program does not support rotation of the images).
1. The image must be in color (not black and white) and meet the minimum quality requirements (no smudges, scratches, wrinkles or less than 300 dpi resolution).

## Acknowledgments:
This project implements the core functionalities based on Tesseract, for more information about this OCR engine plase refer to the Tesseract [repository](https://github.com/tesseract-ocr/tesseract).
