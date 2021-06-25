import cv2
import pytesseract
import numpy as np
import os
import datetime
from pytesseract import Output
import csv

#Reading the image from path
img = cv2.imread(((os.path.dirname(os.path.realpath(__file__))+"\\images\\image.jpg")))
results = []

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
img = get_grayscale(img)
img = remove_noise(img)
img = thresholding(img)

#Print the text in the console
#print(pytesseract.image_to_string(img, lang="spa"))

#Show the converted image and the words recognized with boxes
d = pytesseract.image_to_data(img, "spa",output_type=Output.DICT)
n_boxes = len(d['level'])

for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    i_word = d['text'][i]
    i_position = (x, y), (x + w, y + h)
    i_confidence = d['conf'][i]
    if int(i_confidence) > 0 and len(i_word.strip()) >0:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        results.append([i_word, i_position, i_confidence])
    

with open(((os.path.dirname(os.path.realpath(__file__))+"\\results\\text"+str(datetime.datetime.now().timestamp())+".csv")), mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['word', 'position', 'confidence'])
    for x in range(len(results)):
       csv_writer.writerow([results[x][0], results[x][1], results[x][2]])
    

cv2.imwrite(((os.path.dirname(os.path.realpath(__file__))+"\\results\\image"+str(datetime.datetime.now().timestamp())+".jpg")), img)
cv2.imshow('img', img)
cv2.waitKey(0)