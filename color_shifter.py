from numpy import copy
import cv2 


path = input("Enter the full path of the image, including filetype : ")
hueshift = int(input("Enter amount of hue shift needed : "))

img = cv2.imread(path,1)
# get the image

dupe = copy(img)
# make a copy for color changing and stuff

#dupe = cv2.resize(img, (0, 0), fx = 1, fy = 1)

dupe = cv2.cvtColor(dupe, cv2.COLOR_BGR2HSV)
# change to HSV becuase then you can easily adjust Hue to change the colors 

h = dupe[:,:,0]
h = h + hueshift
# 70 is a good value for hue shift, but leave it up to the user


dupe[:,:,0] = h%180
# opencv hue range is 0-179 so just make sure it loops around

dupe = cv2.cvtColor(dupe,cv2.COLOR_HSV2BGR)
# convert back into a displayable format

cv2.imshow("original",img)
cv2.imshow("new",dupe)
# could change this to save images or whatever

cv2.waitKey()
