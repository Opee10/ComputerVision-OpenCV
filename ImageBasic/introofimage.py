import cv2

img = cv2.imread('barcalogo.jpg', 1) #1 or -1 for the color image, 0 for the grey image

#imgres = cv2.resize(img, (400,400)) #the another way
imgres = cv2.resize(img, (0,0), fx=1.5, fy=1.5)
imgrot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('new_img.jpg', img)

cv2.imshow('Image', img)
cv2.imshow('Image', imgres)
#cv2.imshow('Image', imgrot)
cv2.waitKey(0)
cv2.destroyAllWindows()