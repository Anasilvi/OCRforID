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
#imgOriginal = cv2.imread(((os.path.dirname(os.path.realpath(__file__))+"\\images\\image2.jpg")))
imgTemplate = cv2.imread(((os.path.dirname(os.path.realpath(__file__))+"\\images\\template.jpg")))
results = []
minCI = 90


processFinish = False

#template matching
def match_template(image, template):
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
    h, w = image.shape[:2]
    #calculate the 50 percent of original dimensions
    width = int((490 / h)*w)
    height = int(490)

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(image, dsize)
    return output

def cutImage(image):
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
    with open(((os.path.dirname(os.path.realpath(__file__))+"\\results\\text"+str(datetime.datetime.now().timestamp())+".csv")), mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['type', 'text', 'confidence'])
        for x in range(len(results)):
            csv_writer.writerow([results[x][0], results[x][1], results[x][2]])
    
def readID(img, imgReSized, deltaX, deltaY):
    #Reading ID
    roi = img[105:145,5:215]
    text = pytesseract.image_to_string(roi, lang='spa', config='digits')
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
 
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(i) for i in txtconf['conf'] if i != '-1' ]
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
    #Reading Names
    roi = img[100:145,235:470]
    text = pytesseract.image_to_string(roi, config="-l spa")
    text = text.strip().replace("\n", " ")
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
    conf = 0
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(i) for i in txtconf['conf'] if i != '-1' ]
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
    #Reading Family Names
    roi = img[160:205,235:470]
    text = pytesseract.image_to_string(roi, config="-l spa")
    text = text.strip().replace("\n", " ")
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
    conf = 0
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(i) for i in txtconf['conf'] if i != '-1' ]
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
    #Reading Gender
    roi = img[235:265,235:365]
    text = pytesseract.image_to_string(roi, config="-l spa")
    text = text.strip().replace("\n", " ")
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
    conf = 0
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(i) for i in txtconf['conf'] if i != '-1' ]
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
    #Reading Nationality
    roi = img[280:310,235:470]
    text = pytesseract.image_to_string(roi, config="-l spa")
    text = text.strip().replace("\n", " ")
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
    conf = 0
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(i) for i in txtconf['conf'] if i != '-1' ]
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
    #Reading Date of Birth
    roi = img[325:360,235:360]
    text = pytesseract.image_to_string(roi, config="-l spa")
    text = text.strip().replace("\n", " ")
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
    conf = 0
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(i) for i in txtconf['conf'] if i != '-1' ]
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
    imgReSized = readID(img, imgReSized, deltaX, deltaY)
    imgReSized = readNames(img, imgReSized, deltaX, deltaY)
    imgReSized = readFamilyNames(img, imgReSized, deltaX, deltaY)
    imgReSized = readGender(img, imgReSized, deltaX, deltaY)
    imgReSized = readNationality(img, imgReSized, deltaX, deltaY)
    imgReSized = readDOB(img, imgReSized, deltaX, deltaY)
    processFinish = True
    return processFinish, imgReSized
    
    
    

#writeResults()
#cv2.imwrite(((os.path.dirname(os.path.realpath(__file__))+"\\results\\image"+str(datetime.datetime.now().timestamp())+".jpg")), img)
#cv2.imshow('img', imgReSized)
#cv2.waitKey(0)
