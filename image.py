import cv2

image = cv2.imread('jurassic-park-tour-jeep.jpg')
print(image.shape)
cv2.imshow("original", image)
cv2.waitKey(0)
