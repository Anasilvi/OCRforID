# Developer's documentation

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

## Tools:
Knowledge about the following packages and software is essential to manipulate the program code.

_Python packages:_
Package | Purpose
------------ | -------------
PyQt6 |  GUI implementation
opencv-python | Images manipulation
pytesseract | OCR engine
sqlite3 | Database management

_Software:_

* Tesseract: you have to install tesseract OCR engine in your computer. Follow the next steps to do it:
    * Download the installer for Windows [here](https://github.com/UB-Mannheim/tesseract/wiki)
    * Install the software and search the installation folder, usually is in the path: C:\Program Files\Tesseract-OCR
    * Add the path to "Path" environment variable

You don't need to have extense knowledge about OCR, but minimum knowledge about image manipulation is required.

## User workflow:
The following diagram represents the user activity flow within the software. The main tasks are amplified to exemplify the program's functionalities.

![User workflow diagram](/doc/userflow.png)

## Technical flow:
The following diagram represents the technical flow within the software. All tasks are included to show the complete scenario of use.

![Thechnical workflow diagram](/doc/uml.png)

## Classes diagram:
A Model-View-Controller (MVC) architecture pattern was used to implement the classes in the code. The three main logical components are: the model (which will contain the logic and the data model), the view (which will contain the GUI) and the controller (which will be the orchestrator between the model and the view).
The following diagram shows a summarized architecture of the software.

![Classes diagram](/doc/classes.jpg)

## Methods documentation:
Please consult the following documents for the methods documentation.
*   [Main class](https://github.com/Anasilvi/OCRforID/tree/main/doc/main.html)
*   [Core class](https://github.com/Anasilvi/OCRforID/tree/main/doc/core.html)
*   [Data class](https://github.com/Anasilvi/OCRforID/tree/main/doc/data.html)

## Future work:
An administrator module must be implemented. The admin has to be allowed to configure more types of documents by templates and positions. This will improve the current work and permit it to expand to more applications and businesses. 