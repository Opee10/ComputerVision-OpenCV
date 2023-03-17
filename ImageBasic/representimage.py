import cv2
import random
img = cv2.imread('barcalogo.jpg',-1)

#chaning pixel in specefic part
for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
print(img)
print(type(img))
print(img.shape) #*suppose output (455, 728, 3) here 455=picture height/rows; 728=width; 3=channels
                                #(blue, green, red) BGR == OpenCV uses this for pixel coloring *#
print(img[321][543])

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()