import cv2
import pytesseract
import numpy as np
import os
import datetime
from pytesseract import Output
import csv
from statistics import mean

#Reading the image from path
imgOriginal = cv2.imread(((os.path.dirname(os.path.realpath(__file__))+"\\images\\template.jpg")))
results = []
minCI = 90

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,3)
 
#thresholding
def thresholding(image):
    #return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,10)

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 


#Converting the original image 
img = get_grayscale(imgOriginal)
img = remove_noise(img)
img = thresholding(img)



    

#with open(((os.path.dirname(os.path.realpath(__file__))+"\\results\\text"+str(datetime.datetime.now().timestamp())+".csv")), mode='w', newline='') as csv_file:
 #   csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  #  csv_writer.writerow(['word', 'position', 'confidence'])
   # for x in range(len(results)):
    #   csv_writer.writerow([results[x][0], results[x][1], results[x][2]])
    
def readID():
    #Reading ID
    roi = img[105:140,5:215]
    text = pytesseract.image_to_string(roi, lang='spa', config='digits')
    print(text.strip())
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
 
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(i) for i in txtconf['conf'] if i != '-1' ]
    print(txtconf)
    conf = mean(txtconf)
    print(conf)
    if conf >= minCI:
        cv2.rectangle(imgOriginal, (5,105), (215,140), (0, 255, 0), 2)
    else:
        cv2.rectangle(imgOriginal, (5,105), (215,140), (0, 0, 255), 2)
    
def readNames():
    #Reading Names
    roi = img[100:145,235:470]
    text = pytesseract.image_to_string(roi, config="-l spa")
    print(text.strip().replace("\n", " "))
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
 
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(i) for i in txtconf['conf'] if i != '-1' ]
    print(txtconf)
    conf = mean(txtconf)
    print(conf)
    if conf >= minCI:
        cv2.rectangle(imgOriginal, (235,100), (470,145), (0, 255, 0), 2)
    else:
        cv2.rectangle(imgOriginal, (235,100), (470,145), (0, 0, 255), 2)
    

def readFamilyNames():
    #Reading Family Names
    roi = img[160:205,235:470]
    text = pytesseract.image_to_string(roi, config="-l spa")
    print(text.strip().replace("\n", " "))
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
 
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(i) for i in txtconf['conf'] if i != '-1' ]
    print(txtconf)
    conf = mean(txtconf)
    print(conf)
    if conf >= minCI:
        cv2.rectangle(imgOriginal, (235,160), (470,205), (0, 255, 0), 2)
    else:
        cv2.rectangle(imgOriginal, (235,160), (470,205), (0, 0, 255), 2)

def readGender():
    #Reading Gender
    roi = img[235:265,235:365]
    text = pytesseract.image_to_string(roi, config="-l spa")
    print(text.strip().replace("\n", " "))
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)
 
    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(i) for i in txtconf['conf'] if i != '-1' ]
    print(txtconf)
    conf = mean(txtconf)
    print(conf)
    if conf >= minCI:
        cv2.rectangle(imgOriginal, (235,235), (365,265), (0, 255, 0), 2)
    else:
        cv2.rectangle(imgOriginal, (235,235), (365,265), (0, 0, 255), 2)

def readNationality():
    #Reading Nationality
    roi = img[280:305,235:470]
    text = pytesseract.image_to_string(roi, config="-l spa")
    print(text.strip().replace("\n", " "))
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)

    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(i) for i in txtconf['conf'] if i != '-1' ]
    print(txtconf)
    conf = mean(txtconf)
    print(conf)
    if conf >= minCI:
        cv2.rectangle(imgOriginal, (235,280), (470,305), (0, 255, 0), 2)
    else:
        cv2.rectangle(imgOriginal, (235,280), (470,305), (0, 0, 255), 2)
    
def readDOB():
    #Reading Date of Birth
    roi = img[325:350,235:360]
    text = pytesseract.image_to_string(roi, config="-l spa")
    print(text.strip().replace("\n", " "))
    txtconf = pytesseract.image_to_data(roi, "spa",output_type=Output.DICT)

    #Calculating the confidence level, mean of the CI per character
    txtconf = [int(i) for i in txtconf['conf'] if i != '-1' ]
    print(txtconf)
    conf = mean(txtconf)
    print(conf)
    if conf >= minCI:
        cv2.rectangle(imgOriginal, (235,325), (360,350), (0, 255, 0), 2)
    else:
       cv2.rectangle(imgOriginal, (235,325), (360,350), (0, 0, 255), 2)
    

readID()
readNames()
readFamilyNames()
readGender()
readNationality()
readDOB()
cv2.imwrite(((os.path.dirname(os.path.realpath(__file__))+"\\results\\image"+str(datetime.datetime.now().timestamp())+".jpg")), img)
cv2.imshow('img', imgOriginal)
cv2.waitKey(0)