import cv2
import pytesseract
import numpy as np
import os
import datetime
from pytesseract import Output
import csv
from statistics import mean
from time import sleep

#Reading the image from path
imgTemplate = cv2.imread(((os.path.dirname(os.path.realpath(__file__))+"\\images\\template.jpg")))
results = []
minCI = 90


processFinish = False

#template matching
def match_template(image, template):
    """Function to find the area of interest within the image.

    Args:
        image: Image to lookup the area of interest.
        template: Image template for looking into the image.

    Returns:
        The cut image according the match template, the original image with a blue rectangle showing the area of interest, the difference in X and Y corners between the original image and the template.

    """
    h, w = template.shape[:2]
    res = cv2.matchTemplate(image,template,1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = min_loc
    dX = top_left[0]
    dY = top_left[1]
    bottom_right = (top_left[0]+w, top_left[1]+h)
    found = image[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]]
    imgP = cv2.rectangle(image,top_left, bottom_right, 255, 2)
    return found, imgP, dX, dY

#Re-scaling the image
def reScaling(image):
    """Function to re-size the image keeping the aspect ratio.

    Args:
        image: The image to resize.

    Returns:
        The image resized to 490px high and the proportional width.

    """
    h, w = image.shape[:2]
    width = int((490 / h)*w)
    height = int(490)

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(image, dsize)
    return output

def cutImage(image):
    """Function to cut the background of the image.

    Args:
        image: The image to cut.

    Returns:
        The cut image without background or borders.

    """
    ## (1) Convert to gray, and threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    ## (2) Morph-op to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
    morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

    ## (3) Find the max-area contour
    cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    cnt = sorted(cnts, key=cv2.contourArea)[-1]

    ## (4) Crop and save it
    x,y,w,h = cv2.boundingRect(cnt)
    dst = image[y:y+h, x:x+w]
    return dst

#Opening and converting the original image 
def processImage(path):
    """Function to process the image and extract the data.

    Args:
        path(str): The absolute path of the image to process.

    Returns:
        True if the process finishes well, False otherwise. The path for the image processed and a list with the data extracted.

    """
    imgOriginal = cv2.imread(path)
    imgProcessed, imgReSized, deltaX, deltaY = match_template(reScaling(cutImage(imgOriginal)),imgTemplate)[:4]
    img = cv2.cvtColor(imgProcessed, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img,3)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 10)
    processFinish, newImg = getData(img, imgReSized, deltaX, deltaY)[:2]

    if processFinish:
        cv2.imwrite(((os.path.dirname(os.path.realpath(__file__))+"\\tmp\\imageTmp.jpg")), newImg)
        return processFinish, (os.path.dirname(os.path.realpath(__file__))+"\\tmp\\imageTmp.jpg"), results
    else:
        return processFinish, 'Error processing the image.', results
    
def writeResults():
    """DISCONTINUED. Function to generate a CSV file with the data extracted."""
    with open(((os.path.dirname(os.path.realpath(__file__))+"\\results\\text"+str(datetime.datetime.now().timestamp())+".csv")), mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['type', 'text', 'confidence'])
        for x in range(len(results)):
            csv_writer.writerow([results[x][0], results[x][1], results[x][2]])
    
def readID(img, imgReSized, deltaX, deltaY):
    """Function to do OCR in an image and extract the ID number.

    Args:
        image: The image to extract the data.
        imgReSized: The re-sized image to draw the rectangle in the ID number position.
        deltaX(int): The difference between the original image and the template in the X axis.
        deltaY(int): The difference between the original image and the template in the Y axis.

    Returns:
        The image with a red or green rectangle in the ID position.

    """
    roi = img[105:145,5:215]
    text = pytesseract.image_to_string(roi, lang='spa', config='digits')
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
 
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(float(i)) for i in txtconf['conf'] if i != '-1' ]
    conf = 0
    if len(txtconf) > 0 and len(text.strip()) > 0:
        conf = mean(txtconf)
        #Drawing red rectangle for low confidence or green rectangle for higher confidence
        if conf >= minCI:
            imgP = cv2.rectangle(imgReSized, (5 + deltaX, 105 + deltaY), (215 + deltaX, 145 + deltaY), (0, 255, 0), 2)
        else:
            imgP = cv2.rectangle(imgReSized, (5 + deltaX, 105 + deltaY), (215 + deltaX, 145 + deltaY), (0, 0, 255), 2)
    else:
        imgP = imgReSized
        conf = 0
    results.append(['ID', text.strip().upper(), conf])
    return imgP
    
def readNames(img, imgReSized, deltaX, deltaY):
    """Function to do OCR in an image and extract the names.

    Args:
        image: The image to extract the data.
        imgReSized: The re-sized image to draw the rectangle in the names position.
        deltaX(int): The difference between the original image and the template in the X axis.
        deltaY(int): The difference between the original image and the template in the Y axis.

    Returns:
        The image with a red or green rectangle in the names position.

    """
    roi = img[100:145,235:470]
    text = pytesseract.image_to_string(roi, config="-l spa")
    text = text.strip().replace("\n", " ")
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
    conf = 0
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(float(i)) for i in txtconf['conf'] if i != '-1' ]
    if len(txtconf) > 0 and len(text.strip()) > 0:
        conf = mean(txtconf)
        #Drawing red rectangle for low confidence or green rectangle for higher confidence
        if conf >= minCI:
            imgP = cv2.rectangle(imgReSized, (235 + deltaX, 100 + deltaY), (470 + deltaX, 145 + deltaY), (0, 255, 0), 2)
        else:
            imgP = cv2.rectangle(imgReSized, (235 + deltaX, 100 + deltaY), (470 + deltaX, 145 + deltaY), (0, 0, 255), 2)
    else:
        imgP = imgReSized
        conf = 0
    results.append(['Names', text.strip().upper(), conf])
    return imgP
    
def readFamilyNames(img, imgReSized, deltaX, deltaY):
    """Function to do OCR in an image and extract the surnames.

    Args:
        image: The image to extract the data.
        imgReSized: The re-sized image to draw the rectangle in the surnames position.
        deltaX(int): The difference between the original image and the template in the X axis.
        deltaY(int): The difference between the original image and the template in the Y axis.

    Returns:
        The image with a red or green rectangle in the surnames position.

    """
    roi = img[160:205,235:470]
    text = pytesseract.image_to_string(roi, config="-l spa")
    text = text.strip().replace("\n", " ")
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
    conf = 0
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(float(i)) for i in txtconf['conf'] if i != '-1' ]
    if len(txtconf) > 0 and len(text.strip()) > 0:
        conf = mean(txtconf)
        #Drawing red rectangle for low confidence or green rectangle for higher confidence
        if conf >= minCI:
            imgP = cv2.rectangle(imgReSized, (235 + deltaX, 160 + deltaY), (470 + deltaX, 205 + deltaY), (0, 255, 0), 2)
        else:
            imgP = cv2.rectangle(imgReSized, (235 + deltaX, 160 + deltaY), (470 + deltaX, 205 + deltaY), (0, 0, 255), 2)
    else:
        imgP = imgReSized
        conf = 0
    results.append(['FamilyNames', text.strip().upper(), conf])
    return imgP

def readGender(img, imgReSized, deltaX, deltaY):
    """Function to do OCR in an image and extract the gender.

    Args:
        image: The image to extract the data.
        imgReSized: The re-sized image to draw the rectangle in the gender position.
        deltaX(int): The difference between the original image and the template in the X axis.
        deltaY(int): The difference between the original image and the template in the Y axis.

    Returns:
        The image with a red or green rectangle in the gender position.

    """
    roi = img[235:265,235:365]
    text = pytesseract.image_to_string(roi, config="-l spa")
    text = text.strip().replace("\n", " ")
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
    conf = 0
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(float(i)) for i in txtconf['conf'] if i != '-1' ]
    if len(txtconf) > 0 and len(text.strip()) > 0:
        conf = mean(txtconf)
        #Drawing red rectangle for low confidence or green rectangle for higher confidence
        if conf >= minCI:
            imgP = cv2.rectangle(imgReSized, (235 + deltaX, 235 + deltaY), (365 + deltaX, 265 + deltaY), (0, 255, 0), 2)
        else:
            imgP = cv2.rectangle(imgReSized, (235 + deltaX, 235 + deltaY), (365 + deltaX, 265 + deltaY), (0, 0, 255), 2)
    else:
        imgP = imgReSized
        conf = 0
    results.append(['Gender', text.strip().upper(), conf])
    return imgP

def readNationality(img, imgReSized, deltaX, deltaY):
    """Function to do OCR in an image and extract the nationality.

    Args:
        image: The image to extract the data.
        imgReSized: The re-sized image to draw the rectangle in the nationality position.
        deltaX(int): The difference between the original image and the template in the X axis.
        deltaY(int): The difference between the original image and the template in the Y axis.

    Returns:
        The image with a red or green rectangle in the nationality position.

    """
    roi = img[280:310,235:470]
    text = pytesseract.image_to_string(roi, config="-l spa")
    text = text.strip().replace("\n", " ")
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
    conf = 0
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(float(i)) for i in txtconf['conf'] if i != '-1' ]
    if len(txtconf) > 0 and len(text.strip()) > 0:
        conf = mean(txtconf)
        #Drawing red rectangle for low confidence or green rectangle for higher confidence
        if conf >= minCI:
            imgP = cv2.rectangle(imgReSized, (235 + deltaX, 280 + deltaY), (470 + deltaX, 310 + deltaY), (0, 255, 0), 2)
        else:
            imgP = cv2.rectangle(imgReSized, (235 + deltaX, 280 + deltaY), (470 + deltaX, 310 + deltaY), (0, 0, 255), 2)
    else:
        imgP = imgReSized
        conf = 0
    results.append(['Nationality', text.strip().upper(), conf])
    return imgP
    
def readDOB(img, imgReSized, deltaX, deltaY):
    """Function to do OCR in an image and extract the date of birth.

    Args:
        image: The image to extract the data.
        imgReSized: The re-sized image to draw the rectangle in the date of birth position.
        deltaX(int): The difference between the original image and the template in the X axis.
        deltaY(int): The difference between the original image and the template in the Y axis.

    Returns:
        The image with a red or green rectangle in the date of birth.

    """
    roi = img[325:360,235:360]
    text = pytesseract.image_to_string(roi, config="-l spa")
    text = text.strip().replace("\n", " ")
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
    conf = 0
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(float(i)) for i in txtconf['conf'] if i != '-1' ]
    if len(txtconf) > 0 and len(text.strip()) > 0:
        conf = mean(txtconf)
        #Drawing red rectangle for low confidence or green rectangle for higher confidence
        if conf >= minCI:
            imgP = cv2.rectangle(imgReSized, (235 + deltaX, 325 + deltaY), (360 + deltaX, 360 + deltaY), (0, 255, 0), 2)
        else:
            imgP = cv2.rectangle(imgReSized, (235 + deltaX, 325 + deltaY), (360 + deltaX, 360 + deltaY), (0, 0, 255), 2)
    else:
        imgP = imgReSized
        conf = 0
    results.append(['DOB', text.strip().upper(), conf])
    return imgP

def getData(img, imgReSized, deltaX, deltaY):
    """Function to do get all data from the image.

    Args:
        image: The image to extract the data.
        imgReSized: The re-sized image to draw the rectangle in the ID number position.
        deltaX(int): The difference between the original image and the template in the X axis.
        deltaY(int): The difference between the original image and the template in the Y axis.

    Returns:
        True if the process finished, False otherwise. The image with the rectangles in the data positions.

    """ 
    imgReSized = readID(img, imgReSized, deltaX, deltaY)
    imgReSized = readNames(img, imgReSized, deltaX, deltaY)
    imgReSized = readFamilyNames(img, imgReSized, deltaX, deltaY)
    imgReSized = readGender(img, imgReSized, deltaX, deltaY)
    imgReSized = readNationality(img, imgReSized, deltaX, deltaY)
    imgReSized = readDOB(img, imgReSized, deltaX, deltaY)
    processFinish = True
    return processFinish, imgReSized