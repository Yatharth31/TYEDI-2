import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img.tif")
cv2.imshow("img",img)
cv2.waitKey(0) 
  
# closing all open windows 
cv2.destroyAllWindows()  