from numpy import copy
import cv2 


img = cv2.imread("C:/Users/lenovo/Desktop/Educate/DIP/Programs/Images/map.png",1)
# get the image, change the path to whatever you need

dupe = copy(img)
# make a copy for color changing and stuff

#dupe = cv2.resize(img, (0, 0), fx = 1, fy = 1)

dupe = cv2.cvtColor(dupe, cv2.COLOR_BGR2HSV)
# change to HSV becuase then you can easily adjust Hue to change the colors 

h = dupe[:,:,0]
h = h+70
# adding 70 here to convert a red-darkgreen chart to lightgreen-darkblue


dupe[:,:,0] = h%180
# opencv hue range is 0-179 so just make sure it loops around

dupe = cv2.cvtColor(dupe,cv2.COLOR_HSV2BGR)
# convert back into a displayable format

cv2.imshow("original",img)
cv2.imshow("new",dupe)
# could change this to save images or whatever

cv2.waitKey()
