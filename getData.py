import numpy as np # NumPy is a array-processing package that deals with multidimensional array/ matrix                   #
                   # in very less time, as it provides high performance objects and tools to do so.
                   # since python is bit slow , therefore it takes time to process multi dimensnl array
                   # here Numpy helps to do this in much more faster way.

import cv2      # OpenCV is a huge open-source library for computer vision, machine learning, and image processing
                # It can process images and videos to identify objects, faces, or even the handwriting of a human
                # cv2.imread() method loads an image from the specified file
                # returns matrix of image  if present else return empty matrix that shows us ERROR 
import os
import sys

PATH = os.getcwd()+'\\'     # Return a unicode string representing the current working directory
cap = cv2.VideoCapture(0)   # VideoCapture is a Class to capture livestream from camera
# -1 or 0: default device index for camera, 1 for another device , 2 for anoter one and so on 
# we can give the path inside ("") of video with extension eg: nitb.avi , iiitb.mp4

label = sys.argv[1]
#sys.argv is a parameter: it return lists of arguments passed
#we are using [1] means argument at index 1 will be stored in 'label'

SAVE_PATH = os.path.join(PATH, label) # join is used to join two different paths in a optimal way
 
try:
    os.mkdir(SAVE_PATH) # mkdir is used to make a folder/directory of name SAVE_PATH
except FileExistsError:
    pass

ct = int(sys.argv[2])
maxCt = int(sys.argv[3])+1
print("Hit Space to Capture Image")

while True:   # it is used to capture the frame continously/ indefinetly that is why we pass TRUE
    ret, frame = cap.read() 
    # read() return true if the frame is available otherwise false
    # if true then it saves frame into 'frame' variable
    # and true/false saves inside 'ret' variable

    cv2.imshow('Get Data : '+label,frame[50:350,100:450])   
    #to show the captured image inside the window -> use 'imshow'


    # .waaitkey is used to wait untill user presa a key in keyboard
    #0xFF is mask for 64bit machines , ord('q') is used to check whether the 'q' is pressed or not
    if cv2.waitKey(1) & 0xFF == ord(' '):  
        cv2.imwrite(SAVE_PATH+'\\'+label+'{}.jpg'.format(ct),frame[50:350,100:450])
        #imwrite is used to save an image , it takes two argument (filename(str), image(numpy array))
        print(SAVE_PATH+'\\'+label+'{}.jpg Captured'.format(ct))
        ct+=1
    if ct >= maxCt:
        break

cap.release()
cv2.destroyAllWindows()