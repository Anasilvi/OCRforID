import cv2
import pytesseract
import numpy as np
import os
import datetime
from pytesseract import Output
import csv


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
# CH: not sure why you're writing a function for what is just a single open CV function
# All you do is hide which kernel size and blur method is used
def remove_noise(image):
    return cv2.medianBlur(image,3)
 
# If you really want a clean yet flexible function interface, I suggest you expose as many args as possible 
# and use your currently hardcode values as defaults. You should also (later) add doc strings ....
def remove_noise_CH(image, size=3):
    '''removes noise by running a median blur filter with a given kernel size''' 
    return cv2.medianBlur(image, size)

#thresholding
def thresholding(image):
    #return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,10)

#thresholding
def thresholding_CH(image, blocksize=11, constant=10):
    #return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # you don't need \ here b/c anything similar to
                                 cv2.THRESH_BINARY,                         # a list, including args, are auto protected in Python
                                 blockSize=blocksize,   # if you put one arg per line you can easily add a comment
                                 C=constant)     # e.g.: subtracted from the mean or weighted sum of the neighbourhood pixels.

# BTW I'm unclear where you got your blocksize and constant values from(?) Are these accepted good values or did you 
# have to experiment with your specific type of input?

#dilation
def dilate(image, size=3):
    kernel = np.ones((size,size),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image, size=3):
    kernel = np.ones((size,size),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image, size=3):
    kernel = np.ones((size,size),np.uint8)
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


def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)


# https://github.com/pedrofrodenas/image-thresholding-OCR
def adaptative_thresholding(img, threshold):  # not my spelling :)
    
    # Original image size
    orignrows, origncols = img.shape
    
    # Windows size
    M = int(np.floor(orignrows/16) + 1)
    N = int(np.floor(origncols/16) + 1)
    
    # Image border padding related to windows size
    Mextend = round(M/2)-1
    Nextend = round(N/2)-1
    
    # Padding image
    aux =cv2.copyMakeBorder(img, top=Mextend, bottom=Mextend, left=Nextend,
                            right=Nextend, borderType=cv2.BORDER_REFLECT)
    
    windows = np.zeros((M,N),np.int32)
    
    # Image integral calculation
    imageIntegral = cv2.integral(aux, windows,-1)
    
    # Integral image size
    nrows, ncols = imageIntegral.shape
    
    # Memory allocation for cumulative region image
    result = np.zeros((orignrows, origncols))
    
    # Image cumulative pixels in windows size calculation
    for i in range(nrows-M):
        for j in range(ncols-N):
        
            result[i, j] = imageIntegral[i+M, j+N] - imageIntegral[i, j+N]+ imageIntegral[i, j] - imageIntegral[i+M,j]
     
    # Output binary image memory allocation    
    binar = np.ones((orignrows, origncols), dtype=np.bool)
    
    # Gray image weighted by windows size
    graymult = img.astype('float64') * M * N
    
    # Output image binarization
    binar[graymult <= result*(100.0 - threshold)/100.0] = False
    
    # binary image to UINT8 conversion
    binar = (255*binar).astype(np.uint8)
    
    return binar

from PIL import Image # for better debug viewing ...


#Reading the image from path
img = cv2.imread(((os.path.dirname(os.path.realpath(__file__))+"\\images\\image.jpg")))
#img = cv2.imread(((os.path.dirname(os.path.realpath(__file__))+"\\images\\image_exposure_rotated.png")))
img_col = img.copy()
results = []


red = img[:,:,2]  # get red channel and use as grayscale image



#Converting the original image 
img = get_grayscale(img)
#Image.fromarray(img).show()



img = adjust_gamma(img, 1.5 ) # increase contrast
#Image.fromarray(img).show()

#img = remove_noise_CH(img, size=3)
#Image.fromarray(img).show()

img = adaptative_thresholding(img, 10)  #?10 to 50?
# img = thresholding_CH(img, blocksize=11) 
#Image.fromarray(img).show()

#img = deskew(img)  # that doesn't seem to do anything ...
#Image.fromarray(img).show()

# CH those might help but your current image is just too low res ...

# Opening
#img = opening(img)
#Image.fromarray(img).show()

# Closing
#img = dilate(img)
#img = erode(img)
#Image.fromarray(img).show()

#Print the text in the console
#print(pytesseract.image_to_string(img, lang="spa"))

#Show the converted image and the words recognized with boxes
d = pytesseract.image_to_data(img, "spa",output_type=Output.DICT)
n_boxes = len(d['level'])

for i in range(n_boxes):
    x, y, w, h = d['left'][i], d['top'][i], d['width'][i], d['height'][i]
    i_word = d['text'][i]
    i_position = (x, y), (x + w, y + h)
    i_confidence = int(float(d['conf'][i])) # confidence was a float e.g. 95.0000000
    if i_confidence > 50 and len(i_word.strip()) > 0:   
        cv2.rectangle(img_col, (x, y), (x + w, y + h), (0,0, 255-(i_confidence*2.55)), 2) # color by confidence blue to black
        results.append([i_word, i_position, i_confidence])
    
Image.fromarray(img_col).show()

with open(((os.path.dirname(os.path.realpath(__file__))+"\\results\\text"+str(datetime.datetime.now().timestamp())+".csv")), mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['word', 'position', 'confidence'])
    for x in range(len(results)):
       csv_writer.writerow([results[x][0], results[x][1], results[x][2]])
    

cv2.imwrite(((os.path.dirname(os.path.realpath(__file__))+"\\results\\image"+str(datetime.datetime.now().timestamp())+".jpg")), img)
cv2.imwrite(r"results\image" + str(datetime.datetime.now().timestamp()) + ".jpg", img) # use relative path!
cv2.imshow('img', img)
cv2.waitKey(0)